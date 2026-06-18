"""
Given an completely unsorted input list array of integers, construct a loop tracking routine that scans the list
and determines the longest consecutive run length of numbers found anywhere inside the collection.
Sample Input: List = [100, 4, 200, 1, 3, 2]
Expected Output: Longest Consecutive Sequence Length: 4 (Sequence: [1, 2, 3, 4])
"""

nums = [100, 4, 200, 1, 3, 2]

nums.sort()

current = 1
longest = 1

for i in range(1, len(nums)):

    if nums[i] == nums[i - 1] + 1:
        current += 1

    elif nums[i] == nums[i - 1]:
        pass

    else:
        current = 1

    if current > longest:
        longest = current

print("Longest Consecutive Sequence Length:", longest)