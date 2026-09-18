# String formatting

username = "kelvin"
age = 250

message = "Username: {}, Age: {}".format(username, age)
print(message)

# Named placeholders
message = "User {username} is {age} years old."

print(
    message.format(
        username=username,
        age=age
    )
)