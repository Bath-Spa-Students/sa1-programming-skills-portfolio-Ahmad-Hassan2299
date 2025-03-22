# This program stores and prints your name, hometown, and age using a dictionary
# Function to get user input and validate age
def get_user_input():
     # Get user input for name, hometown, and age
    name = input("Enter your name: ")
    hometown = input("Enter your hometown: ")
    # Validate age input
    while True:
      age = input("Enter your age: ")
        if age.isdigit():
            age = int(age)
            break
      else:
            print("Please enter a valid age (intiger value).")
    return name, hometown, age
# Geting user input
name, hometown, age = get_user_input()
# Saveing the information in a dictionary
biography = {
    "Name": name,
    "Hometown": hometown,
    "Age": age
}
# Printing the values on separate lines using a single print() statement
print(f"Name: {biography['Name']}\nHometown: {biography['Hometown']}\nAge: {biography['Age']}")
