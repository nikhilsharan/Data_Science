"""
Real-world analogy: School grade system

What you'll build:
Add student names and marks 
Calculate average 
Assign grades (A, B, C…)

Concepts you'll use:
Dictionaries → {student_name: [marks]} 
Loops → iterate through students 
If-else → grading logic 
Operators → average calculation 
Strings → names, grade labels 

Stretch idea:
Find topper, lowest scorer.
"""

student_data = {
    "Akash": 79,
    "Abhinav": 80,
    "Binod": 54,
    "Naveen": 68,
    "Vidur": 97
}

total = 0
average = 0

A = []
B = []
C = []

print(student_data.items())


for key,value in student_data.items():
    if value >= 80:
        A.append(key)
    elif value < 80 and value >= 60:
        B.append(key)
    else:
        C.append(key)

print("The students with 80% and above i.e. with grade A are", A)
print("The students with 60% and above i.e. with grade B are", B)
print("The students with 60% and less i.e. with grade C are", C)

for key,value in student_data.items():
    total = total + value
    average = total/len(student_data)

print("The average score of the class is", average)

topper = ""
max_marks = 0

for key,value in student_data.items():
    if max_marks < value:
        max_marks = value
        topper = key

print(f"Topper of the class is {topper} with {max_marks} marks")
