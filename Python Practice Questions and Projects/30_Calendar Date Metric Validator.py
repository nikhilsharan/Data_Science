"""
Accept three individual integers representing Day, Month, and Year. Write a comprehensive conditional
validation suite that checks if this combination forms a physically real calendar date. Factor in variable month
lengths (28, 30, 31 days) and Leap Year exceptions for February.
Sample Input: Day = 29, Month = 2, Year = 2021
Expected Output: Date Validity: False (2021 is not a leap year)
"""

day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

# Check leap year
if year % 400 == 0:
    leap = True
elif year % 100 == 0:
    leap = False
elif year % 4 == 0:
    leap = True
else:
    leap = False

valid = True

# Check month
if month < 1 or month > 12:
    valid = False

else:
    # Determine maximum days in the month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31

    elif month in [4, 6, 9, 11]:
        max_days = 30

    else:  # February
        if leap:
            max_days = 29
        else:
            max_days = 28

    # Validate day
    if day < 1 or day > max_days:
        valid = False

if valid:
    print("Date Validity: True")
else:
    print("Date Validity: False")