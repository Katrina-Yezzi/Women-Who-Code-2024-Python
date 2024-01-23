# Women Who Code (Python) Challenge No. 10
# Write a program to remove duplicates from a list.

import time

def displayIntro():
    print('''Do you have duplicates in your list? Let me help you your remove them.''')

def dupes(list1):
    list2 = list(set(list1))

    print(f'Original List: {sorted(list1)}')
    print(f'List after removing duplicates: {sorted(list2)}')

playAgain = 'yes'
while playAgain=='yes' or playAgain == 'y':
    displayIntro()
    list1 = input('Enter your list here (separated by commas or spaces): ').strip().split(' ')
    dupes(list1)
    time.sleep(2)
    print('Do you want to try another phrase? (yes or no)')
    playAgain=input()
