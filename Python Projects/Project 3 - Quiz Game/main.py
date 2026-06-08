"""
3. Quiz Game Application (Intermediate)

Real-world analogy: Online quiz apps

What you'll build:
Multiple questions with options 
User selects answers 
Final score displayed

Concepts you'll use:
Lists of dictionaries → questions database 
Strings → questions & answers 
Loops → ask all questions 
If-else → check answers 
Variables → score tracking

Example structure:
questions = [
  {"q": "Capital of India?", "a": "Delhi"},
]

Why it's powerful:
You start thinking in terms of data + logic together.
"""

questions_list = [
  {'q': "Capital of India?", 'a': "Delhi"},
  {'q': "IT Capital of India?", 'a': "Bangalore"},
  {'q': "2000 + 5000", 'a': '7000'}
]

options_list = [
  ['Delhi','Bangalore','Mumbai','Kolkata'],
  ['Delhi','Bangalore','Mumbai','Kolkata'],
  ['5000', '7000', '4000','3000']
]

for i in range(len(questions_list)):
  print(questions_list[i]['q'])
  print(options_list[i])
  ans = input()
  if ans == questions_list[i]['a']:
    print("Correct")
  else:
    print("Incorrect")