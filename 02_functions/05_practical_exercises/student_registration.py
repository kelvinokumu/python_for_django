
def register_student(name, email, age, course):
    student = {
        "name": name,
        "email": email,
        "age": age,
        "course": course
    }

    return student


def display_student(student):
    print("\nStudent Information")

    print("Name:", student["name"])
    print("Email:", student["email"])
    print("Age:", student["age"])
    print("Course:", student["course"])


student = register_student(
    "Jason",
    "jason@example.com",
    25,
    "Computer Science"
)

display_student(student)