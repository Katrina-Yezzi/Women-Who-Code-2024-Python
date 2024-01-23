# Women Who Code (Python) Challenge No. 12
# Write a program to reverse a given string.

import time

def displayIntro():
    print('''If you give me a string of numbers or letters, I can return it to you in reverse.''')

def reverse(string):
    reversed_string = string[::-1]
    print(f'Here it is in reverse: {reversed_string}')
    return reversed_string

playAgain = 'yes'
while playAgain=='yes' or playAgain == 'y':
    displayIntro()
    string = input('Enter a string: ')
    reverse(string)
    time.sleep(2)
    print('Do you want to give me another number? (yes or no)')
    playAgain=input()
