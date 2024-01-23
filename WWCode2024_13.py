# Women Who Code (Python) Challenge No. 13
# Write a program to shuffle the elements of a list randomly.

import time
import random

def displayIntro():
    print('''If you give me a string of numbers or letters, I can return it to you in reverse.''')

def shuffle(list1):
    list2 = list1.copy()
    random.shuffle(list2)

    print(f"Here's your original List: {list1}")
    print(f"Here's your shuffled List: {list2}")

    return list2

playAgain = 'yes'
while playAgain=='yes' or playAgain == 'y':
    displayIntro()
    list1 = list(input('Enter a list of characters: ').strip().split(" "))
    shuffle(list1)
    time.sleep(2)
    print('Do you want to do another? (yes or no)')
    playAgain=input()
