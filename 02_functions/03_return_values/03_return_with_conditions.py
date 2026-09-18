# Return values with conditions
def check_age(age):
    if age >= 18:
        return True
    return False

result = check_age(25)
print(result)

def check_login(username, password):
    if username == "admin" and password == "python123":
        return True
    return False


if check_login("admin", "python123"):
    print("Login successful.")
else:
    print("Login failed.")


# Returning different values
def get_grade(marks):
    if marks >= 70:
        return "A"

    if marks >= 60:
        return "B"

    if marks >= 50:
        return "C"

    if marks >= 40:
        return "D"

    return "F"


grade = get_grade(75)
print("Grade:", grade)