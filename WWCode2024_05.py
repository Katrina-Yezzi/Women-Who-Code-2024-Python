# Women Who Code (Python) Challenge No. 5
# Write a program to find the maximum and minimum values in a list.

import time

def displayIntro():
    print('''Enter a list of numbers and I will identify the smallest and largest numbers in the list.''')

   
def minmax(ls):
    m= int(ls[0])
    s= int(ls[0])
    
    for i in ls:
        num=int(i)
        if num > m:
            m=num
        if num < s:
            s=num
    print(f'The results are: {s} and {m}')            

    return s, m
    
playAgain = 'yes'
while playAgain=='yes' or playAgain == 'y':
    displayIntro()
    ls=input().split(' ')
    minmax(ls)
    time.sleep(2)
    print('Do you want to try another phrase? (yes or no)')
    playAgain=input()
