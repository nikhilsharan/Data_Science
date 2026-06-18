"""
Write a script utilizing a definite for loop to calculate and display the first N sequence terms of the historical
Fibonacci progression sequence (0, 1, 1, 2, 3, 5, 8, ...).
Sample Input: N = 7
Expected Output: Sequence Output: [0, 1, 1, 2, 3, 5, 8]
"""

n = int(input())

if n <= 0:
    print("Enter value greater than 0")
elif n == 1:
    print('[0]')
elif n == 2:
    print('[0,1]')
else:
    fib = [0,1]
    for i in range(2,n):
        fib.append(fib[i-1] + fib[i-2])
    print(fib)
        



