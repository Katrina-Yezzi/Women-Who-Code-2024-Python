# Women Who Code (Python) Challenge No. 8
# Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.

import time

def displayIntro():
    print('''Type a sentence and I will tell you how many uppercase letters there are and how many lowercase letters there are in your sentence.''')

def count_case(sentence):
    upper_count = 0
    lower_count = 0

    for char in sentence:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    print(f'The number of uppercase letters is {upper_count}')
    print(f'The number of lowercase letters is {lower_count}')

    return upper_count, lower_count

playAgain = 'yes'
while playAgain=='yes' or playAgain == 'y':
    displayIntro()
    sentence = input("Enter a sentence: ")
    count_case(sentence)
    time.sleep(2)
    print('Do you want to try another phrase? (yes or no)')
    playAgain = input()
