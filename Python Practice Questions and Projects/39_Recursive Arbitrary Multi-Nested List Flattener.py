"""
Write a recursive function `flatten_list` that accepts a multi-dimensional array structure (lists containing
integers or other nested lists at infinite depths) and reduces it down into a completely flat uniform singledimensional
list.
Sample Input: flatten_list([1, [2, [3, 4], 5], 6, [7]])
Expected Output: Flattened List: [1, 2, 3, 4, 5, 6, 7]
"""

def flatten_list(lst):

    result = []

    for item in lst:

        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result


data = [1, [2, [3, 4], 5], 6, [7]]

print(flatten_list(data))