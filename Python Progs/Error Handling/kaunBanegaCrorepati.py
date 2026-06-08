myListOfQues = [
    ["Who is called the father of Computers", "Charles Babbage", "Albert Einstein", "M K Gandhi", "SRK", 1],

    ["Who is the PM of India", "Amit Shah", "Narendra Modi", "M K Gandhi", "SRK", 2],

    ["Number of bones in adult", 205, 210, 410, 206, 4],

    ["Who is called the father of Economics", "Adam Smith", "Albert Einstein", "M K Gandhi", "SRK", 1],

    ["Who deriveed the formula E=mc^2", "Charles Babbage", "Albert Einstein", "M K Gandhi", "SRK", 2],

    ["Who is called the father of Computers", "Charles Babbage", "Albert Einstein", "M K Gandhi", "SRK", 1],

    ["Who is called the father of Computers", "Charles Babbage", "Albert Einstein", "M K Gandhi", "SRK", 1],

    ["Who is called the father of Computers", "Charles Babbage", "Albert Einstein", "M K Gandhi", "SRK", 1],

    ["Who is called the father of Computers", "Charles Babbage", "Albert Einstein", "M K Gandhi", "SRK", 1],

    ["Who is called the father of Computers", "Charles Babbage", "Albert Einstein", "M K Gandhi", "SRK", 1],

    ["Who is called the father of Computers", "Charles Babbage", "Albert Einstein", "M K Gandhi", "SRK", 1],

    ["Who is called the father of Computers", "Charles Babbage", "Albert Einstein", "M K Gandhi", "SRK", 1],

    ["Who is called the father of Computers", "Charles Babbage", "Albert Einstein", "M K Gandhi", "SRK", 1],

    ["Who is called the father of Computers", "Charles Babbage", "Albert Einstein", "M K Gandhi", "SRK", 1],

    ["Who is called the father of Computers", "Charles Babbage", "Albert Einstein", "M K Gandhi", "SRK", 1]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]

money = 0
i = 0

for i in range(len(myListOfQues)):
    questionsOnComp = myListOfQues[i]
    print(f"Question for Rs. {levels[i]}")
    print(questionsOnComp[0])
    print(f"a. {questionsOnComp[1]}  b. {questionsOnComp[2]}")
    print(f"c. {questionsOnComp[3]}  d. {questionsOnComp[4]}")
    response = int(input("Enter your answer (1-4) and 0 to quit"))
    if ( response == 0 ):
        print("Hum aapko anumati dete h game quit karne k liye")
        break
    else:
        if (response == questionsOnComp[-1]):
            print(f"Sahi Jawab, Aap jitte hain Rs. {levels[i]}")
            if (i == 4):
                money = 10000
            elif (i == 9):
                money = 320000
            elif (i == 14):
                money = 10000000
        else:
            print("Afsos! Galat Jawab")
            break

print(f"Aap aaj yahan se le jaate h {money} dhanrashi")