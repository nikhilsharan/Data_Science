"""
Write a function `calculate_invoice` that computes a billing total. It should accept a variable number of
unique item prices via `*args`, and discount or tax metadata settings via `**kwargs`. Ensure it safely extracts
optional arguments like 'discount_rate' or 'tax_rate' with robust fallback defaults.
Sample Input: calculate_invoice(100, 50, 25, discount_rate=0.10, tax_rate=0.05)
Expected Output: Final Total: 165.375
"""

def calculate_invoice(*args, **kwargs):

    subtotal = sum(args)

    discount_rate = kwargs.get('discount_rate', 0)
    tax_rate = kwargs.get('tax_rate', 0)

    subtotal = subtotal - (subtotal * discount_rate)

    total = subtotal + (subtotal * tax_rate)

    return total


result = calculate_invoice(
    100,
    50,
    25,
    discount_rate=0.10,
    tax_rate=0.05
)

print("Final Total:", result)