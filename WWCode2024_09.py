# Women Who Code (Python) Challenge No. 9
# Write a program to check if a number is even or odd.

import time

def displayIntro():
    print('''Enter a number and I will tell you whether it is even or odd.''')

def even_odd(number):
    if number % 2 == 0:
        print(f'{number} is an even number.')
    else:
        print(f'{number} is an odd number.')

playAgain = 'yes'
while playAgain=='yes' or playAgain == 'y':
    displayIntro()
    number = int(input('Enter a number: '))
    even_odd(number)
    time.sleep(2)
    print('Do you want to try another phrase? (yes or no)')
    playAgain=input()
