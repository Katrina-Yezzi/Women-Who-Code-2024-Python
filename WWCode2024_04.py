# Women Who Code (Python) Challenge No. 4
# Write a program to find the sum of all elements in a list.

import time

def displayIntro():
    print('''Enter a list of numbers and I will add all the numbers for you.''')

   
def sum_elements(ls):
    listSum = 0
    for i in ls:
        listSum += int(i)
        
    return listSum
    
playAgain = 'yes'
while playAgain=='yes' or playAgain == 'y':
    displayIntro()
    ls=input().split(' ')
    print(f'The sum of your numbers is: {sum_elements(ls)}')
    time.sleep(2)
    print('Do you want to try another phrase? (yes or no)')
    playAgain=input()

