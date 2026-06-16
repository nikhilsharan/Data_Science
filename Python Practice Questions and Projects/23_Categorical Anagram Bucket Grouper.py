"""
Given an array collection of string words, design a dictionary grouping structure that buckets words together
that are anagrams of one another. The keys of your dictionary should represent the normalized sorted
character baseline.
Sample Input: Words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
Expected Output: Grouped: {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'],
'abt': ['bat']}
"""

words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

grouped = {}

for word in words:
    key = ''.join(sorted(word))

    if key not in grouped:
        grouped[key] = [word]
    else:
        grouped[key].append(word)

print(grouped)