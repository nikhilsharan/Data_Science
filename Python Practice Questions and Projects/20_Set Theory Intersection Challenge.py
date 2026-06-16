"""
Given two lists of student database IDs, cast them into Python sets and extract: 1) IDs present in both
databases, 2) IDs present in only the first database, and 3) All unique elements across both lists combined.
Sample Input: ListA = [1, 2, 3, 4], ListB = [3, 4, 5, 6]
Expected Output: Both: {3, 4}, Only A: {1, 2}, Combined: {1, 2, 3, 4, 5, 6}
&   # intersection
|   # union
-   # difference
^   # symmetric difference
"""

ListA = [1, 2, 3, 4]
ListB = [3, 4, 5, 6]

setA = set(ListA)
setB = set(ListB)

both = setA & setB
onlyA = setA - setB
combined = setA | setB
symm_diff = setA ^ setB

print(f"Both: {both}, Only A: {onlyA}, Combined: {combined}, symmetric difference: {symm_diff}")