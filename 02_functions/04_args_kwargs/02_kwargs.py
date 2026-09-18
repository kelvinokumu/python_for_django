# **kwargs allows a function to receive
# any number of keyword arguments.


def display_user(**user):

    for key, value in user.items():
        print(f"{key}: {value}")


display_user(
    username="kelvin",
    email="kelvin@example.com",
    age=25
)

def create_profile(**details):

    print("User Profile")

    for key, value in details.items():
        print(f"{key}: {value}")


create_profile(
    username="kelvin",
    country="Kenya",
    is_active=True
)