"""
Write an algebraic root-solver for quadratic equations (ax^2 + bx + c = 0). Request coefficients a, b, and c.
Using the mathematical discriminant (D = b^2 - 4ac), map distinct conditional pathways to handle and format
two real roots, one repeated real root, or complex imaginary roots.
Sample Input: a = 1, b = -5, c = 6 | a = 1, b = 2, c = 5
Expected Output: Roots: 3.0 and 2.0 | Roots: -1+2j and -1-2j
"""

import math
import cmath

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

D = b**2 - 4*a*c

if D > 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)

    print("Two Real Roots:")
    print(root1, "and", root2)

elif D == 0:
    root = -b / (2*a)

    print("One Repeated Real Root:")
    print(root)

else:
    root1 = (-b + cmath.sqrt(D)) / (2*a)
    root2 = (-b - cmath.sqrt(D)) / (2*a)

    print("Complex Roots:")
    print(root1, "and", root2)