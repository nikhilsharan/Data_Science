"""
Write a highly optimized program that checks whether a given positive integer is a perfect power of two.
Constraint: You must achieve this using only bitwise operators (&, |, ^, ~, <<, >>) without any loops, math libraries, or conditional statements for the computation logic.

Sample Input: Number = 16 | Number = 18
Expected Output: True | False
"""

def is_power_of_two(n):
    if n <= 0:
        return False
    
    if (n & (n - 1)) == 0:
        return True
    else:
        return False


# Examples
print(is_power_of_two(16))  # True
print(is_power_of_two(18))  # False