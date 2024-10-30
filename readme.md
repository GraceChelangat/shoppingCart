# System Documentation
## System Name: Online Shopping Cart

This Python-based Online Shopping Cart system allows users to interactively browse, add, view, and purchase products. It applies Object-Oriented Programming (OOP) principles, including encapsulation, inheritance, and polymorphism.

## Purpose
The system mimics a simple e-commerce setup where a user can select items to add to a shopping cart, view the cart, and check out to complete the purchase. The classes (Product, Cart, and User) and their attributes/methods make the program modular and easy to extend.

## Class Descriptions

### Product Class

**Purpose**: Represents an individual product available for purchase.

- **Attributes**:
  - `name` (str): The name of the product (e.g., "Laptop").
  - `price` (float): The price of the product (e.g., 999.99).
  - `quantity_available` (int): The available stock of the product.

- **Methods**:
  - `get_info()`: Returns a string with the product's details (name, price, and available stock).
  - `is_available(quantity)`: Checks if the requested quantity is available.
  - `update_quantity(quantity)`: Decreases `quantity_available` by the specified amount to reflect items purchased.

### Cart Class

**Purpose**: Manages the user's shopping cart, holding products added for purchase and calculating the total cost.

- **Attributes**:
  - `items` (list): Stores tuples of (product, quantity) for each item in the cart.
  - `total_price` (float): Stores the total price of the items in the cart.

- **Methods**:
  - `add_product(product, quantity)`: Adds a specified quantity of a product to the cart if stock is available.
  - `remove_product(product_name)`: Removes a specified product from the cart by name.
  - `calculate_total()`: Calculates and returns the total price of all items in the cart.
  - `checkout()`: Finalizes the purchase, displays the total price, and clears the cart.

### User Class

**Purpose**: Represents a user in the system with a unique username and their own shopping cart.

- **Attributes**:
  - `username` (str): The user’s name.
  - `cart` (Cart): Each user has a cart instance to manage their selected products.

- **Methods**:
  - `view_cart()`: Displays the current contents of the cart.
  - `add_to_cart(product, quantity)`: Adds a product with a specified quantity to the user's cart.
  - `checkout()`: Completes the purchase by calling the `checkout()` method on the user's cart.

## Main Function (`main`)
The `main()` function serves as the system’s entry point and user interface. It allows the user to:

- Enter their username.
- View a list of available products.
- Add items to their cart by selecting a product and specifying the quantity.
- View their cart contents after each addition.
- Check out to finalize the purchase, calculate the total cost, and clear the cart.

The system uses input prompts for user interaction, making it intuitive and straightforward to use.

## Conclusion
This Online Shopping Cart system demonstrates key OOP concepts in a practical application. It provides a simple yet effective e-commerce experience that could be extended further by adding more features or more complex products with specialized attributes.
