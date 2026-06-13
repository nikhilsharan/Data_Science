"""
Design a routine to perform a left cyclic rotation on a list by an integer factor of k. This means elements are
shifted leftward, wrapping around to the tail. Handle large inputs where k is vastly greater than the list's total
length.
Sample Input: List = [10, 20, 30, 40, 50], k = 2
Expected Output: Rotated List: [30, 40, 50, 10, 20]
"""

lst = [10, 20, 30, 40, 50]
k = int(input())

if k > len(lst):
    effective_k = k % len(lst)
else:
    effective_k = k

rotated = lst[effective_k:] + lst[:effective_k]
print(rotated)

