"""
Write an algorithm that takes an M x N 2D matrix (represented as nested lists) and computes its
mathematical transpose (turning rows into columns and vice-versa) resulting in an N x M matrix structure.
Constraint: Do not import NumPy or any external matrix library.
Sample Input: Matrix = [[1, 2, 3], [4, 5, 6]]
Expected Output: Transpose: [[1, 4], [2, 5], [3, 6]]
"""

matrix = [[1, 2, 3], [4, 5, 6]]

transpose = []

for col in range(len(matrix[0])):
    new_row = []

    for row in range(len(matrix)):
        new_row.append(matrix[row][col])

    transpose.append(new_row)

print(transpose)