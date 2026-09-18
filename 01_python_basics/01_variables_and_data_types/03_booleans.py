# Boolean values

is_authenticated = True
is_staff = False
is_active = True

print(is_authenticated)
print(is_staff)
print(is_active)

# Using booleans in conditions
if is_authenticated:
    print("User is logged in.")

if is_active:
    print("Account is active.")

if not is_staff:
    print("User is not a staff member.")