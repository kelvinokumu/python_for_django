
username = "  John  "

# Remove spaces
username = username.strip()
print(username)

# Change case
print(username.upper())
print(username.lower())
print(username.title())

# Check content
email = "John@example.com"

print(email.startswith("John"))
print(email.endswith(".com"))

# Replace text
message = "Welcome to our website."

print(message.replace("website", "application"))

# Split text
full_name = "John Doe"
names = full_name.split(" ")
print(names)

# Check if text exists
email = "kelvin@example.com"

if "@" in email:
    print("Valid-looking email")