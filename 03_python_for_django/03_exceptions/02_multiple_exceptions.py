"""
Handling different types of exceptions.
"""
try:
    number = int(input("Enter a number: "))

    result = 100 / number

    print("Result:", result)

except ValueError:

    print("Please enter a valid number.")

except ZeroDivisionError:

    print("You cannot divide by zero.")