import random
'''
Snake Water Gun Game
1 for Snake
-1 for Water
0 for Gun
'''
value = [-1, 0, 1]
computer = random.choice(value)
youStr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDictionaryToPrint = {-1: "water", 0: "gun", 1: "snake"}

you = youDict[youStr]

print(f"You chose {reverseDictionaryToPrint[you]}\nComputer chose {reverseDictionaryToPrint[computer]}")

'''
Snake Water Gun Game
1 for Snake
-1 for Water
0 for Gun
'''

if (computer == you):
    print("It is a Draw")

else:
    
    if(computer == -1 and you == 1): 
        print("You win!")

    elif(computer == -1 and you == 0):
        print("You Lose!")

    elif(computer == 1 and you == -1):
        print("You lose!")

    elif(computer == 1 and you == 0):
        print("You Win!")

    elif(computer == 0 and you == -1):
        print("You Win!")

    elif(computer == 0 and you == 1):
        print("You Lose!")

    else:
        print("Something went wrong!")

