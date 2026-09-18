# Dictionary methods

user = {
    "username": "kelvin",
    "email": "kelvin@example.com",
    "is_active": True
}

# get()
print(user.get("username"))

# Useful when key may not exist
print(user.get("phone"))

# keys()
print(user.keys())

# values()
print(user.values())

# items()
print(user.items())

# Update
user.update({
    "age": 25,
    "country": "Kenya"
})

print(user)