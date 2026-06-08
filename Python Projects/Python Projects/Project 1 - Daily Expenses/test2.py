# n = int(input())

# for i in range(1,n+1):
#   print()
#   for j in range(1,i+1):
#     print(i, end='')


# this also gives the same pattern
n = int(input())

# Loop through from 1 to n
for i in range(1, n + 1):
    # Print the number 'i' repeated 'i' times
    print(str(i) * i)