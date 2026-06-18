"""
Write a program using an indefinite while loop that computes the mathematical factorial (N!) of a given user
input integer. Avoid any recursive function calls.
Sample Input: Number = 5
Expected Output: 5! Result: 120
"""

n = int(input())
f = 1

while n > 0:
    f = f * n
    n = n - 1

print(f)
    
