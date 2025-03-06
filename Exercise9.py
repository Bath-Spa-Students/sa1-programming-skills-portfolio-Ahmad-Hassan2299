def is_even_or_odd(number):
    # Check if the number is even or odd
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."
def main():
    try:
        # Ask the user to enter a number
        number = int(input("Please enter a number: "))
        # Determine if the number is even or odd
        result = is_even_or_odd(number)
        # Print the result
        print(result)
    except ValueError:
        # Handle the case where the input is not an integer
        print("Invalid input. Please enter an integer.")
if __name__ == "__main__":
    # Call the main function
    main()