"""
Write a program that cleans a list by removing all duplicate entries. Constraint: You must preserve the exact
chronological sequence order of the elements as they appeared originally. Do not rely on casting to a
standard unordered set.
Sample Input: List = [1, 3, 2, 1, 4, 3, 2, 5]
Expected Output: Cleaned List: [1, 3, 2, 4, 5]
"""

# lst = [1, 3, 2, 1, 4, 3, 2, 5]
# st = set(lst)
# print(st)

lst = [1, 3, 2, 1, 4, 3, 2, 5]
new_lst = []

for i in lst:
    if i in new_lst:
        pass
    else:
        new_lst.append(i)

print(lst)
print(new_lst)