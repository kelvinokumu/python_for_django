"""
raise statement allows us to create our own exceptions.
"""

def register_user(username, age):

    if age < 18:
        raise ValueError(
            "User must be at least 18 years old."
        )

    if not username:
        raise ValueError("Username cannot be empty.")

    print(f"User {username} registered successfully.")


try:
    register_user("kelvin",25)
except ValueError as error:
    print("Registration error:", error)