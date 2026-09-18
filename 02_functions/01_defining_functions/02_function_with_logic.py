
def check_age():
    age = 20
    if age >= 18:
        print("User can register.")
    else:
        print("User cannot register.")

check_age()


def check_login():
    is_authenticated = True

    if is_authenticated:
        print("Welcome to your dashboard.")
    else:
        print("Please log in.")


check_login()
