"""
Extract the first 3 characters and the last 3 characters of an input string and concatenate them together. If
the input string contains fewer than 6 characters, return a message saying 'String too short'.
Sample Input: String = 'PythonProgramming'
Expected Output: Extracted String: 'Pyting'
"""

sample_string = input("Enter string: ")
str1 = ""
str2 = ""

if len(sample_string) <= 6:
    print("String too short")
else:
    str1 = sample_string[0:3]
    #str2 = sample_string[-1:-4:-1] #reversing the last 3 characters
    #str2 = sample_string[-3:-1]# if -1 is given then last element wont be counted
    str2 = sample_string[-3:]
    print(str1+str2)