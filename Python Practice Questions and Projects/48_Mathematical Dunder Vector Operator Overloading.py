"""
Write a structural multi-dimensional class `Vector`. Use special magic methods (dunder systems) to overload
standard mathematical operations: `__add__` to perform standard element-wise coordinate additions, and
`__mul__` to calculate dot products between independent Vector structures.
Sample Input: v1 = Vector(2, 4), v2 = Vector(1, 3); v1 + v2 | v1 * v2
Expected Output: Vector(3, 7) | 14 (since 2*1 + 4*3 = 14)
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload + operator for vector addition
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Overload * operator for dot product
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    # String representation
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


# Sample Input
v1 = Vector(2, 4)
v2 = Vector(1, 3)

# Output
print(v1 + v2)
print(v1 * v2)