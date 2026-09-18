"""
Grade Calculator
"""

def calculate_average(*marks):
    total = sum(marks)
    return total / len(marks)

def get_grade(average):
    if average >= 70:
        return "A"

    elif average >= 60:
        return "B"

    elif average >= 50:
        return "C"

    elif average >= 40:
        return "D"

    else:
        return "F"

def display_result(name, average, grade):
    print("\nStudent Result")
    print("Name:", name)
    print("Average:", average)
    print("Grade:", grade)

name = "Shawn"
average = calculate_average(75, 68, 82, 70)

grade = get_grade(average)
display_result(
    name,
    average,
    grade
)