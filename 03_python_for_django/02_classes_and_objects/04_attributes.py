"""
Attributes

Attributes represent data belonging to an object.
"""


class Product:

    def __init__(self, name, price, quantity):

        self.name = name
        self.price = price
        self.quantity = quantity


product = Product(
    "Laptop",
    80000,
    5
)


print("Name:", product.name)
print("Price:", product.price)
print("Quantity:", product.quantity)


# Change an attribute

product.price = 75000

print("Updated price:", product.price)


# Calculate inventory value

value = product.price * product.quantity

print("Inventory value:", value)