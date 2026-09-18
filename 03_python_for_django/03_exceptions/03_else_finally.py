"""
try, except, else and finally
"""

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

else:
    print("You entered:", number)

finally:
    print("Program finished.")