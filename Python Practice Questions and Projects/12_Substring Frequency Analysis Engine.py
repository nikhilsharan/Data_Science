"""
Write a program that counts how many times a specific substring occurs inside a parent body of text.
Constraint: Do not use the built-in string method .count(). You must build your own traversal window using
manual string slicing and loops.
Sample Input: Text = 'ABCDCDC', Substring = 'CDC'
Expected Output: Total Occurrences: 2 (Note: Overlapping instances must be counted)
"""

text = "ABCDCDC"
substring = "CDC"

count = 0

for i in range(len(text) - len(substring) + 1):
    if text[i:i + len(substring)] == substring:
        count += 1

print("Total Occurrences:", count)

"""
text = "ABCDCDC"
substring = "CDC"

print(text.count(substring))
"""