"""
Handling exceptions with try and except.
"""
try:

    age = int(input("Enter your age: "))

    print("Age:", age)

except ValueError:

    print("Please enter a valid number.")