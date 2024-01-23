# Women Who Code (Python) Challenge No. 7
# Write a program to check if a number is positive, negative, or zero.

import time

def displayIntro():
    print('''If you give me a number, I'll tell you whether it's positive, negative, or zero.''')

def sign(num):
    if num > 0:
        print('This number is positive.')

    elif num < 0:
        print('This number is negative.')

    else:
        print('This number is zero.')

playAgain = 'yes'
while playAgain=='yes' or playAgain == 'y':
    displayIntro()
    num = float(input('Enter a number: '))
    sign(num)
    time.sleep(2)
    print('Do you want to try another phrase? (yes or no)')
    playAgain=input()
