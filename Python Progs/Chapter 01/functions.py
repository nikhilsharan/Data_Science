def avgOfThreeNumbers():
    
    num1 = int(input("Enter you number: "))
    num2 = int(input("Enter you number: "))
    num3 = int(input("Enter you number: "))

    average = int((num1 + num2 + num3)/3)

    return average


value = avgOfThreeNumbers()

print(value)