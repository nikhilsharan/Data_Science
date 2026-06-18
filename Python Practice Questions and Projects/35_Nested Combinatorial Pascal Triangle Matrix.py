"""
Write a nested looping program that generates Pascal's Triangle down to an arbitrary N depth rows.
Represent rows as lists nested within an encompassing list structure, mapping binomial coefficient sums.
Sample Input: Rows = 5
Expected Output: Triangle: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
"""

rows = int(input("Enter rows: "))

triangle = [[1]]

for i in range(1, rows):

    prev = triangle[i - 1]

    current = [1]

    for j in range(len(prev) - 1):
        current.append(prev[j] + prev[j + 1])

    current.append(1)

    triangle.append(current)

print(triangle)