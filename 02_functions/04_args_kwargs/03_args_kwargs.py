# Using *args and **kwargs together
# *args - positional arguments
# **kwargs - keyword arguments

def create_order(*products, **customer):
    print("Products:")

    for product in products:
        print("-", product)

    print("\nCustomer:")

    for key, value in customer.items():
        print(f"{key}: {value}")


create_order(
    "Laptop",
    "Mouse",
    "Keyboard",
    username="kelvin",
    email="kelvin@example.com"
)
