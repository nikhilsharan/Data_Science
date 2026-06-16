"""
Write a script that processes an input string sentence and returns a dictionary where keys represent unique
characters and values capture their exact frequency count. Exclude empty space characters.
Sample Input: Text = 'hello world'
Expected Output: Dictionary: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd':1}
"""

txt = 'hello world'
result = {}

for ch in txt:
    if ch == ' ':
        pass
    else:
        if ch not in result:
            result[ch] = 1
        else:
            result[ch] += 1

print (result)