# *args allows a function to receive
# any number of positional arguments.

def calculate_total(*prices):
    total = 0
    for price in prices:
        total += price

    return total


print(calculate_total(100, 200))
print(calculate_total(100, 200, 300))
print(calculate_total(100, 200, 300, 400))


def greet_users(*usernames):

    for username in usernames:
        print(f"Welcome, {username}!")


greet_users(
    "James",
    "Smith",
    "Jane",
)