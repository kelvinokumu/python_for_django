# Iterating through dictionaries
user = {
    "username": "kelvin",
    "email": "kelvin@example.com",
    "is_active": True
}

for key, value in user.items():
    print(f"{key}: {value}")

# Multiple users
users = {
    "user1": {
        "username": "kelvin",
        "age": 25
    },
    "user2": {
        "username": "jane",
        "age": 22
    }
}

for user_id, user_data in users.items():
    print(user_id)
    print(user_data)