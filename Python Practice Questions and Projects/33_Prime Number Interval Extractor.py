"""
Write a program utilizing nested loops that checks an interval span between integer start and integer end,
and outputs a formatted list tracking every prime number within that range.
Sample Input: Start = 10, End = 30
Expected Output: Identified Primes: [11, 13, 17, 19, 23, 29]
"""

start = int(input("Enter start: "))
end = int(input("Enter end: "))

primes = []

for num in range(start, end + 1):

    if num < 2:
        continue

    is_prime = True

    for i in range(2, num):

        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)

print("Identified Primes:", primes)

