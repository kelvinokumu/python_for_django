# Nested loops
users = [
    "Kelvin",
    "Jane",
    "Peter"
]

products = [
    "Laptop",
    "Phone"
]
for user in users:
    print(f"\nUser: {user}")
    for product in products:
        print(f"  Product: {product}")