# Women Who Code (Python) Challenge No. 11
# Write a program to print the multiplication table of a given number.

import time

def displayIntro():
    print('''I can recite my multiplication table. Do you want to see?''')

def mult_table(number):
    print(f'Multiplication Table for {number}:')
    for i in range(1, 11):
        result = number * i
        print(f'{number} x {i} = {result}')

playAgain = 'yes'
while playAgain=='yes' or playAgain == 'y':
    displayIntro()
    number = int(input('Enter a number: '))
    mult_table(number)
    time.sleep(2)
    print('Do you want to give me another number? (yes or no)')
    playAgain=input()
