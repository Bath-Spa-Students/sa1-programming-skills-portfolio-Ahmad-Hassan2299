# Define the correct password
correct_password = "12345"
# Initialize the number of attempts
attempts = 0
max_attempts = 5
# Loop until the password is correct or maximum attempts are reached
while attempts < max_attempts:
    # Ask the user to enter the password
entered_password = input("Enter the password: ")
    # Check if the entered password is correct
    if entered_password == correct_password:
        print("Password correct. Access granted.")
        break
    else:
        # Increment the number of attempts
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        # Check if maximum attempts have been reached
        if attempts == max_attempts:
            print("Maximum attempts reached. Authorities have been alerted.")
