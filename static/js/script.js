// Add product to cart
function addToCart(name, price) {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];

    cart.push({ name: name, price: price });
    localStorage.setItem("cart", JSON.stringify(cart));

    alert("✅ " + name + " added to cart!");
}

// Load cart items on cart page
function loadCart() {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    let container = document.getElementById("cart-items");
    let total = 0;

    if (cart.length === 0) {
        container.innerHTML = "<p>Your cart is empty.</p>";
        return;
    }

    container.innerHTML = "";
    cart.forEach((item, index) => {
        total += item.price;
        container.innerHTML += `
            <div class="cart-item">
                <span>${item.name}</span>
                <span>₹ ${item.price}</span>
            </div>
        `;
    });

    document.getElementById("total").innerText = "Total: ₹ " + total;
}
