number = input("Enter a number : ")

try:
    for i in range (1, 11):
        print(f"{int(number)} X {i} = {int(number) * i}")
except Exception as e:
    print(e)

print("Some important lines of code")

print("End of code")