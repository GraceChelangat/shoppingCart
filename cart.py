import random

class Product:
    def __init__(self, name, price, quantity_available):
        """Initializes the product with name, price, and quantity available."""
        self.name = name
        self.price = price
        self.quantity_available = quantity_available

    def get_info(self):
        """Returns the product details."""
        return f"{self.name}: ${self.price:.2f} (Available: {self.quantity_available})"

    def is_available(self, quantity):
        """Checks if the requested quantity is available."""
        return quantity <= self.quantity_available

    def update_quantity(self, quantity):
        """Updates the available quantity of the product."""
        self.quantity_available -= quantity


class Cart:
    def __init__(self):
        """Initializes an empty cart."""
        self.items = []
        self.total_price = 0.0

    def add_product(self, product, quantity):
        """Adds a product to the cart if available."""
        if product.is_available(quantity):
            self.items.append((product, quantity))
            product.update_quantity(quantity)  # Update available quantity
            print(f"Added {quantity} of {product.name} to the cart.")
        else:
            print(f"Sorry, only {product.quantity_available} of {product.name} available.")

    def remove_product(self, product_name):
        """Removes a product from the cart."""
        for item in self.items:
            if item[0].name == product_name:
                self.items.remove(item)
                print(f"Removed {product_name} from the cart.")
                return
        print(f"{product_name} not found in the cart.")

    def calculate_total(self):
        """Calculates the total price of items in the cart."""
        self.total_price = sum(product.price * quantity for product, quantity in self.items)
        return self.total_price

    def checkout(self):
        """Finalizes the purchase and displays the total."""
        total = self.calculate_total()
        print(f"Your total is: ${total:.2f}. Thank you for your purchase!")
        self.items.clear()  # Clear the cart after checkout


class User:
    def __init__(self, username):
        """Initializes the user with a username and an empty cart."""
        self.username = username
        self.cart = Cart()

    def view_cart(self):
        """Displays the items in the user's cart."""
        if not self.cart.items:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for product, quantity in self.cart.items:
                print(f"{product.get_info()} (Quantity: {quantity})")

    def add_to_cart(self, product, quantity):
        """Adds a specified product to the user's cart."""
        self.cart.add_product(product, quantity)

    def checkout(self):
        """Completes the purchase for the user."""
        self.cart.checkout()


# Main Function to Add Items Manually and Interact with Cart
def main():
    # Create some products
    products = [
        Product("Laptop", 999.99, 5),
        Product("Smartphone", 499.99, 10),
        Product("Headphones", 199.99, 20),
        Product("Camera", 299.99, 3),
        Product("Monitor", 150.00, 7)
    ]

    # Create a user
    username = input("Enter your username: ")
    user = User(username)

    # Main Loop to add items manually
    while True:
        print("\nAvailable products:")
        for idx, product in enumerate(products):
            print(f"{idx + 1}. {product.get_info()}")

        # User selects a product by number
        try:
            product_choice = int(input("\nSelect a product number to add to your cart (or 0 to checkout): "))
            if product_choice == 0:
                break  # Checkout and exit loop
            elif 1 <= product_choice <= len(products):
                product = products[product_choice - 1]
                quantity = int(input(f"Enter quantity for {product.name}: "))
                user.add_to_cart(product, quantity)
            else:
                print("Invalid product number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

        # View Cart
        user.view_cart()

    # Checkout
    user.checkout()


# Run the main function
if __name__ == "__main__":
    main()
