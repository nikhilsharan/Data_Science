"""
Write a program to calculate the compound interest of an investment. The script should request the principal
amount (P), annual interest rate (r), time in years (t), and number of times interest is compounded per year
(n). Output the final accrued amount rounded to exactly two decimal places.
Sample Input: P = 5000, r = 5% (0.05), t = 3, n = 4
Expected Output: Total Accrued Amount: $5803.77

A=P*(1+(r/n))**(nt) 
"""

p = int(input("enter principal: "))
r = int(input("enter rate: "))
t = int(input("enter time: "))
n = int(input("enter number of times int is compounded: "))

r = r/100

a = p*(1+(r/n))**(n*t)
rounded_amount = round(a, 2)

print(f"Total Accrued Amount: {rounded_amount}")