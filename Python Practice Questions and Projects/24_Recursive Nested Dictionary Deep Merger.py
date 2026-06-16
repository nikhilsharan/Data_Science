"""
Write a deep-merge function for Python dictionaries. Given dict1 and dict2, combine them recursively. If a
key maps to another dictionary in both objects, merge those inner structures. If a key maps to a primitive
value, dict2's value overrides dict1.
Sample Input: d1 = {'a': 1, 'b': {'x': 10}}, d2 = {'b': {'y': 20}, 'c': 3}
Expected Output: Merged: {'a': 1, 'b': {'x': 10, 'y': 20}, 'c': 3}
"""

def deep_merge(d1, d2):

    merged = d1.copy()

    for key, value in d2.items():

        if (
            key in merged and
            isinstance(merged[key], dict) and
            isinstance(value, dict)
        ):
            merged[key] = deep_merge(merged[key], value)

        else:
            merged[key] = value

    return merged

print(deep_merge({'a': 1, 'b': {'x': 10}}, {'b': {'y': 20}, 'c': 3}))