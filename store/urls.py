from django.urls import path
from . import views 
urlpatterns = [
    path('', views.home),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('logout/', views.logout_page, name='logout'),

    path('add/<int:pid>/', views.add_to_cart),
    path('cart/', views.cart_page, name='cart'),
    path('checkout/', views.checkout_page, name='checkout'),
    path('success/', views.success_page, name='success'),
    path('orders/', views.orders_page, name='orders'),
    path('update-qty/<int:item_id>/', views.update_qty, name='update_qty'),

]

