# Positional parameters
def greet_user(username):
    print(f"Welcome, {username}!")

greet_user("Kelvin")
greet_user("Jane")


# More than one parameter
def display_user(username, email):
    print(f"Username: {username}")
    print(f"Email: {email}")

display_user("kelvin","kelvin@example.com")


def calculate_total(price, quantity):
    total = price * quantity
    print(f"Total: {total}")

calculate_total(1500, 3)
