"""
Develop a progressive income tax engine based on these tax tiers: Up to $10,000 -> 0% Tax; next $40,000
($10,001 to $50,000) -> 10% Tax; next $50,000 ($50,001 to $100,000) -> 20% Tax; Earnings above
$100,000 -> 30% Tax. Given an income, compute exact total tax due.
Sample Input: Income = $65,000
Expected Output: Total Calculated Tax: $7,000 (0 + 4000 + 3000)
"""

income = float(input("Enter income: "))

tax = 0

if income <= 10000:
    tax = 0

elif income <= 50000:
    tax = (income - 10000) * 0.10

elif income <= 100000:
    tax = 40000 * 0.10
    tax += (income - 50000) * 0.20

else:
    tax = 40000 * 0.10
    tax += 50000 * 0.20
    tax += (income - 100000) * 0.30

print("Total Tax:", tax)