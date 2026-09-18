# Returning multiple values
def get_user():
    username = "kelvin"
    email = "kelvin@example.com"

    return username, email

username, email = get_user()
print("Username:", username)
print("Email:", email)

def calculate_price(price, quantity):
    subtotal = price * quantity
    tax = subtotal * 0.16
    total = subtotal + tax

    return subtotal, tax, total


subtotal, tax, total = calculate_price(1000, 2)

print("Subtotal:", subtotal)
print("Tax:", tax)
print("Total:", total)