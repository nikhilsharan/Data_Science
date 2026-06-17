"""
Build an absolute date-logic evaluator to check if a provided year is a leap year. A year is a leap year if it is
divisible by 4, but not by 100, unless it is also perfectly divisible by 400.
Sample Input: Year = 2000 | Year = 1900
Expected Output: True | False
"""

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("True")
else:
    print("False")