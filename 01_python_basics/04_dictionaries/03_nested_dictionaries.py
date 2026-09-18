# Nested dictionaries
user = {
    "username": "kelvin",
    "profile": {
        "first_name": "John",
        "last_name": "Doe",
        "country": "Kenya"
    }
}

print(user["username"])

print(user["profile"]["first_name"])

print(user["profile"]["country"])

# Change nested data

user["profile"]["country"] = "Kenya"

print(user)