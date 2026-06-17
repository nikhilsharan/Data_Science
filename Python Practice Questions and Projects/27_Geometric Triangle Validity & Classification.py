"""
Accept three floating-point lengths representing triangle sides. First, confirm if they satisfy the Triangle
Inequality Theorem (a+b>c). If valid, further classify the structure as Equilateral, Isosceles, or Scalene using
conditional statements.
Sample Input: Sides = 5.0, 5.0, 8.0
Expected Output: Valid Status: True | Classification: Isosceles Triangle
"""

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:

    print("Valid Status: True")

    if a == b == c:
        print("Classification: Equilateral Triangle")

    elif a == b or b == c or a == c:
        print("Classification: Isosceles Triangle")

    else:
        print("Classification: Scalene Triangle")

else:
    print("Valid Status: False")