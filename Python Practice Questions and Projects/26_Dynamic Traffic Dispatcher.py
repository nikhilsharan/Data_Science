"""
Write an if-elif-else routing network that accepts a string representing a current light status ('Red', 'Yellow',
'Green') and a Boolean flag denoting an approaching Emergency Vehicle. Dispatch actions appropriately.
Sample Input: Light = 'Red', Emergency = True
Expected Output: Action: 'Halt non-emergency lane. Override signal for Emergency
Vehicle.'
"""

light = input()
emergency = bool(input())

if light == 'red' and emergency == True:
    print("Halt non-emergency lane. Override signal for Emergency vehicle")
elif light == 'yellow' and emergency == True:
    print("Halt non-emergency lane. Override signal for Emergency vehicle")
elif light == 'red' and emergency == False:
    print("Stop")
else:
    print("Green light, Go!!!")