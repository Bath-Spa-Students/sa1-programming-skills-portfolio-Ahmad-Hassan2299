# Dictionary mapping month numbers to the number of days in each month
days_in_month = {
    1: 31,
    2: 28,  # Default for February, will adjust for leap years
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
# Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  return True
    return False
# Ask the user to input the month number
month = int(input("Enter the month number (1-12): "))
# Check if the input month number is valid
if 1 <= month <= 12:
    # If the month is February, ask if it's a leap year
    if month == 2:
        year = int(input("Enter the year: "))
        if is_leap_year(year):
            print("29 days")
        else:
            print("28 days")
    else:
        print(f"{days_in_month[month]} days")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
