"""
The __init__ method

The constructor is called automatically
when an object is created.
"""


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

user1 = User(
    "kelvin",
    "kelvin@example.com"
)

user2 = User(
    "jane",
    "jane@example.com"
)

print(user1.username)
print(user1.email)

print(user2.username)
print(user2.email)