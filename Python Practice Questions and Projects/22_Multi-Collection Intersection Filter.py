"""
Given three separate list arrays containing integers, construct an optimized Set-based filtration routine that
extracts a list containing elements that appear in *at least two* out of the three input arrays.
Sample Input: L1 = [1, 2, 3], L2 = [2, 3, 4], L3 = [3, 4, 5]
Expected Output: Filtered Elements: [2, 3, 4]
"""

L1 = [1, 2, 3] 
L2 = [2, 3, 4] 
L3 = [3, 5, 6]

filtered_element = []

for i in L1:
    if i in L2 or i in L3:
        filtered_element.append(i)
    else:
        pass

for j in L2:
    if j in L1 or j in L3:
        filtered_element.append(j)
    else:
        pass

for k in L3:
    if k in L1 or k in L2:
        filtered_element.append(k)
    else:
        pass

filter_set = set(filtered_element)

print(list(filter_set))