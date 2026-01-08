from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Product, Cart, CartItem, Order


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def login_page(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('/')
    return render(request, 'login.html')


def signup_page(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        return redirect('/login/')
    return render(request, 'signup.html')


def logout_page(request):
    logout(request)
    return redirect('login')


@login_required
def add_to_cart(request, pid):
    product = get_object_or_404(Product, id=pid)
    cart, _ = Cart.objects.get_or_create(user=request.user)

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        item.quantity += 1
    item.save()

    return redirect('cart')


@login_required
def cart_page(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)

    total = sum(i.product.price * i.quantity for i in items)

    return render(request, 'cart.html', {
        'items': items,
        'total': total
    })

@login_required
def update_qty(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)

    if request.method == "POST":
        qty = int(request.POST.get('quantity', 1))
        if qty > 0:
            item.quantity = qty
            item.save()

    return redirect('cart')

@login_required
def checkout_page(request):
    cart = Cart.objects.get(user=request.user)
    items = CartItem.objects.filter(cart=cart)

    total = sum(i.product.price * i.quantity for i in items)

    if request.method == "POST":
        items.delete()   # payment success → clear cart
        return redirect('success')

    return render(request, 'checkout.html', {
        'items': items,
        'total': total
    })

@login_required
def success_page(request):
    return render(request, 'success.html')


@login_required
def orders_page(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders.html', {'orders': orders})
