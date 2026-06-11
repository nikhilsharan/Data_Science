"""
Read a positive integer in base-10 and convert it into its binary (base-2) equivalent string. Constraint: You
are forbidden from using the built-in bin() function, formatting expressions like f'{num:b}', or pre-existing
string casting methods. Use arithmetic, modulo, and floor division operators manually.
Sample Input: Integer = 13
Expected Output: Binary String: '1101'
"""

num = int(input("Enter a positive integer: "))

binary = ""

while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary
    num = num // 2

print("Binary String:", binary)