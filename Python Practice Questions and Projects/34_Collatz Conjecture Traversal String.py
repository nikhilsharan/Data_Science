"""
Design an indefinite while loop system tracking the Collatz Conjecture: Start with positive integer n. If n is
even, divide it by 2; if odd, multiply it by 3 and add 1. Repeat this operational track until n reaches 1. Print out
the full trail path sequence and total steps taken.
Sample Input: Initial n = 6
Expected Output: Path: 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 | Total Steps: 8
"""

n = int(input("Enter a positive number: "))

path = [n]
steps = 0

while n > 1:

    if n % 2 == 0:
        n = n // 2

    else:
        n = 3 * n + 1

    path.append(n)
    steps += 1

print("Path:", " -> ".join(map(str, path)))
print("Total Steps:", steps)