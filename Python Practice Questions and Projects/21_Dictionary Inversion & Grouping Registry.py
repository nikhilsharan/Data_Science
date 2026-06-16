"""
Write an algorithm to invert a dictionary's layout, transforming old values into new unique keys. If multiple
source keys shared the exact same value, group those source keys together into a structured list under that
inverted key value.
Sample Input: Data = {'Apple': 'Fruit', 'Carrot': 'Veg', 'Banana': 'Fruit'}
Expected Output: Inverted: {'Fruit': ['Apple', 'Banana'], 'Veg': ['Carrot']}
"""

data = {'Apple': 'Fruit', 'Carrot': 'Veg', 'Banana': 'Fruit'}

inverted = {}

for key, value in data.items():

    if value not in inverted:
        inverted[value] = [key]

    else:
        inverted[value].append(key)

print(inverted)