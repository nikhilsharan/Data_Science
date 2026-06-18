"""
Given a list of dictionary elements representing products with 'name' and 'price' fields, use Python's built-in
sorted() mapping engine bound alongside an inline custom anonymous `lambda` expression to sort the
objects by price in ascending order.
Sample Input: [{'name': 'A', 'price': 50}, {'name': 'B', 'price': 20}]
Expected Output: [{'name': 'B', 'price': 20}, {'name': 'A', 'price': 50}]
"""
products = [
    {'name': 'A', 'price': 50},
    {'name': 'B', 'price': 20}
]

sorted_products = sorted(products, key=lambda x: x['price'])

print(sorted_products)