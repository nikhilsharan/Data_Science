"""
Create a script that requests two integers from the user and calculates their sum, difference, product, exact
quotient, floor quotient, and remainder using standard python operators.
Sample Input: Num1 = 15, Num2 = 4
Expected Output: Sum: 19, Diff: 11, Prod: 60, Div: 3.75, Floor Div: 3, Modulo: 3
"""

n1 = int(input("enter first number: "))
n2 = int(input("enter second number: "))

print(f"Sum: {n1+n2}, Diff: {n1-n2}, Prod: {n1*n2}, Div: {n1/n2}, Floor Div: {n1//n2}, Modulo: {n1%n2}")