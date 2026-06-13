"""
Given an unsorted list of integers and a target total integer, isolate all completely unique pairs of numbers
within the list whose summation precisely matches the target value. Avoid duplicate pairs in your final list.
Sample Input: List = [2, 4, 3, 5, 7, 8, 9], Target = 7
Expected Output: Unique Pairs: [(2, 5), (3, 4)]
"""
numbers = [2, 4, 3, 5, 7, 8, 9]
target = 7

pairs = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            
            # Store the pair in ascending order
            if numbers[i] < numbers[j]:
                pair = (numbers[i], numbers[j])
            else:
                pair = (numbers[j], numbers[i])

            # Avoid duplicate pairs
            if pair not in pairs:
                pairs.append(pair)

print("Unique Pairs:", pairs)