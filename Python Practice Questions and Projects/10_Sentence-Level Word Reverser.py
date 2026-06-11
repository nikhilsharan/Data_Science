"""
Given an input sentence string, reverse the absolute order of the words while keeping the internal characters
of each individual word perfectly intact. Ensure trailing/leading spaces are handled gracefully.
Sample Input: Sentence = 'Data Science with Python is powerful'
Expected Output: Reversed Sentence: 'powerful is Python with Science Data'
"""

str1 = input("Enter your sentence: ")
str_lst = str1.split(" ")

str_lst = str_lst[::-1]
str2 = " ".join(str_lst)

print(str2)

