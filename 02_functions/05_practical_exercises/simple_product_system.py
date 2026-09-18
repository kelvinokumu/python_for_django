
products = []
def add_product(name, price, quantity):
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    products.append(product)

def display_products():
    print("\nProducts")
    for product in products:

        print(
            f"{product['name']} - "
            f"KES {product['price']} - "
            f"Quantity: {product['quantity']}"
        )

def calculate_inventory_value():
    total = 0

    for product in products:
        value = (product["price"] * product["quantity"])
        total += value

    return total

# Add products
add_product("Laptop", 80000, 5)
add_product("Mouse", 1500, 10)
add_product("Keyboard", 3000, 7)

# Display products
display_products()

# Calculate inventory value
total = calculate_inventory_value()
print("\nTotal inventory value:", total)