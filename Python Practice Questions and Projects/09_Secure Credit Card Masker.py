"""
Implement a privacy compliance utility that takes a 16-digit credit card number string. It must replace the first
12 characters with asterisks (*) and format the output so there is a hyphen breaking up every group of 4
digits.
Sample Input: Card = '1234567812345678'
Expected Output: Masked Format: '****-****-****-5678'
"""

credit_card = input("Enter your 16 digit credit card numbe: ")

if len(credit_card) == 16:
    masked = '****-****-****-' + credit_card[12:16]
    print(f"Masked Format: {masked}")
else:
    print('Enter correct value')