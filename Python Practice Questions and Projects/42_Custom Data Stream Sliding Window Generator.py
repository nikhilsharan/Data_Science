"""
Implement a memory-efficient generator function `sliding_window` using the `yield` statement. It must take
an iterable sequence and an integer window width length, yielding consecutive sliding subset chunks from
the stream without copying massive sequences in memory layout.
Sample Input: list(sliding_window([1, 2, 3, 4, 5], size=3))
Expected Output: [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
"""

def sliding_window(sequence, size):

    for i in range(len(sequence) - size + 1):
        yield sequence[i:i+size]


print(list(sliding_window([1, 2, 3, 4, 5], 3)))