function addToCart(productName, quantity) {

    // Retrieve the current cart from local storage

    let cart = JSON.parse(localStorage.getItem("cart"));

    

    // If the cart doesn't exist in local storage, create a new one

    if (!cart) {

        cart = {};

    }

    

    // Update the cart with the selected item and quantity

    cart[productName] = quantity;

    

    // Save the updated cart to local storage

    localStorage.setItem("cart", JSON.stringify(cart));

}

function viewCart() {
    // Retrieve the current cart from local storage
    let cart = JSON.parse(localStorage.getItem("cart"));
    
    // If the cart doesn't exist in local storage, display an error message
    if (!cart) {
        alert("Your cart is empty.");
        return;
    }
    
    // Loop through the items in the cart and display their details
    let totalCost = 0;
    for (let productName in cart) {
        let product = products.find(p => p.name === productName);
        let quantity = cart[productName];
        let itemCost = product.price * quantity;
        totalCost += itemCost;
        
        // Display the item details and cost
        console.log(product.name + " x" + quantity + ": $" + itemCost);
    }
    
    // Display the total cost of the items in the cart
    console.log("Total: $" + totalCost);
}


function generateBill() {
    // Display the cart details
    viewCart();
    
    // Display the bill
    console.log("Thank you for shopping with us!");
}
