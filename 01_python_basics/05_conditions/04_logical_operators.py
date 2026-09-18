# Logical operators
is_authenticated = True
is_active = True

# AND
if is_authenticated and is_active:
    print("User can access the application.")

# OR
is_staff = False
is_superuser = True
if is_staff or is_superuser:
    print("User has administrative access.")

# NOT
is_logged_in = False
if not is_logged_in:
    print("Please log in.")

# Combining conditions
age = 25
has_account = True

if age >= 18 and has_account:
    print("User can register.")