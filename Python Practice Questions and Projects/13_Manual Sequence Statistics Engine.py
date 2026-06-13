"""
Given a list of numeric values, compute the maximum element, minimum element, and the mathematical
average. Constraint: You are forbidden from using the built-in functions max(), min(), or sum(). Traverse the
sequence manually.
Sample Input: List = [23, 45, 12, 56, 89, 34]
Expected Output: Max: 89, Min: 12, Average: 43.83
"""

lst = []

n = int(input("Enter the number of elements: "))

sum = 0

for i in range(n):
    num = int(input())
    lst.append(num)

max = lst[0]
min = lst[0]

for j in lst:
    if j > max:
        max = j
    if j < min:
        min = j

    sum = sum + j

avg = round((sum / n),2)

print(f"Max: {max}, Min: {min}, Average: {avg}")