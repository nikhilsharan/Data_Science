"""
You are given a tuple containing student records, where each record is itself a tuple of (Name, Score). Write
a program to sort this collection in descending order based exclusively on their scores, producing a sorted
tuple of tuples.
Sample Input: Records = (('Alice', 88), ('Bob', 95), ('Charlie', 78))
Expected Output: Sorted: (('Bob', 95), ('Alice', 88), ('Charlie', 78))
"""

student = (('Alice', 88),('Bob', 95),('Charlie', 78))

student_list = list(student)

for i in range(len(student_list)):
    for j in range(len(student_list) - 1):
        if student_list[j][1] < student_list[j + 1][1]:
            student_list[j], student_list[j + 1] = (student_list[j + 1],student_list[j])

sorted_student = tuple(student_list)

print(sorted_student)
