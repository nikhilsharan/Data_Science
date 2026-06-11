"""
Implement a basic string compression algorithm using the counts of repeated consecutive characters. For example, 'aabcccccaaa' becomes 'a2b1c5a3'. Constraint: If the 'compressed' string would not become strictly shorter than the original string, your program must return the original string.
Sample Input: String = 'aabcccccaaa' | String = 'abcd'
Expected Output: Result: 'a2b1c5a3' | Result: 'abcd'
"""

def compress_string(string):
    compressed = ""
    count = 1

    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
        else:
            compressed = compressed + string[i] + str(count)
            count = 1

    # Add the last character and its count
    compressed = compressed + string[-1] + str(count)

    # Return the shorter string
    if len(compressed) < len(string):
        return compressed
    else:
        return string


# Examples
print(compress_string("aabcccccaaa"))
print(compress_string("abcd"))


"""
string = "aabcccccaaa"

counts = {}

for char in string:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1

print(counts)
"""