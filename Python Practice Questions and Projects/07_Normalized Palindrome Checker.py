"""
Write a program to determine if a given string is a palindrome. The program must be case-insensitive and
ignore all spaces and punctuation marks.
Sample Input: String = 'A man a plan a canal Panama'
Expected Output: Result: True (It is a palindrome)
"""

str1 = input("Enter a string: ")
str1 = str1.lower()
spaces = ""
str2 = ""
str3 = ""

for char in str1:
    if char in [" ","!","@","#","$","%","^","&","*"]:
        spaces = spaces + char
    else:
        str2 = str2 + char

for char1 in range(len(str1) - 1, -1, -1):
    if str1[char1] in [" ","!","@","#","$","%","^","&","*"]:
        spaces = spaces + str1[char1]
    else:
        str3 = str3 + str1[char1]

if str2 == str3:
    print("True (It is a palindrome)")
    print(str2,str3)
else:
    print("False (It is a not palindrome)")
    print(str2,str3)