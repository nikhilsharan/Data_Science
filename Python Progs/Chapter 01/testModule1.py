def printKuchBhi(stringVariable):
    print(f"Ye string humko de de Thakur : {stringVariable}")

def galatAddition(number1, number2):
    return number1 + number2 + 5


if __name__ == '__main__': # if we do not include this condition then whenever any other module imports testModule1 these functions also will be executed even if we dont want them to get executed
    print(printKuchBhi("Nhi"))
    valueOfAddition = galatAddition(5,5)
    print(valueOfAddition)







