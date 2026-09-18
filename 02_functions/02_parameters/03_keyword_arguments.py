# Keyword arguments
def create_user(username, email, age):
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Age: {age}")


# Positional arguments
create_user(
    "kelvin",
    "kelvin@example.com",
    25
)

# Keyword arguments
create_user(
    username="kelvin",
    email="kelvin@example.com",
    age=25
)

# Keyword arguments can make calls easier to understand
create_user(
    email="jane@example.com",
    age=22,
    username="jane"
)