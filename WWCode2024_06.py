# Women Who Code (Python) Challenge No. 6
# Write a program to count the occurrences of a specific character in a string.

import time

def displayIntro():
    print('''I can tell you how many times a character appears in a sentence.''')

def occurrence(sentence, char):
    count=0

    for character in sentence:
        if character == char:
            count += 1

    print(f'The instances of {char} in this sentence is: {count}.')

    return count
    
playAgain = 'yes'
while playAgain=='yes' or playAgain == 'y':
    displayIntro()
    sentence = input('Enter a sentence: ').lower()
    char = input('Enter a character to count: ').lower()
    occurrence(sentence, char)
    time.sleep(2)
    print('Do you want to try another phrase? (yes or no)')
    playAgain=input()
