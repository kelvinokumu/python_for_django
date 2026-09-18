# Type conversion / Type casting

# Input from a user is always a string
age = input("Enter your age: ")

print(type(age))

# Convert string to integer
age = int(age)

print(type(age))
print("Next year:", age + 1)

# String to float
price = "1500.50"
price = float(price)

print(price)
print(type(price))

# Number to string
user_id = 1001

user_id = str(user_id)

print(user_id)
print(type(user_id))