import random

'''
Stone Paper Scissor Game
1 for Stone(s)
-1 for Paper(p)
0 for Scissor(sc)
'''
value = [-1, 0, 1]
computer = random.choice(value)
print("Enter s for stone\np for paper\nsc for scissor")
youStr = input("Enter your choice: ")
youDict = {"s": 1, "p": -1, "sc": 0} #refer the comment above
reverseDictionaryToPrint = {-1: "paper", 0: "scissor", 1: "stone"}

you = youDict[youStr]

print(f"You chose {reverseDictionaryToPrint[you]}\nComputer chose {reverseDictionaryToPrint[computer]}")

'''
Stone Paper Scissor Game
1 for Stone(s)
-1 for Paper(p)
0 for Scissor(sc)
'''

if (computer == you):
    print("It is a Draw")

else:
    
    if(computer == -1 and you == 1): 
        print("You lose!")

    elif(computer == -1 and you == 0):
        print("You Win!")

    elif(computer == 1 and you == -1):
        print("You win!")

    elif(computer == 1 and you == 0):
        print("You lose!")

    elif(computer == 0 and you == -1):
        print("You lose!")

    elif(computer == 0 and you == 1):
        print("You win!")

    else:
        print("Something went wrong!")

