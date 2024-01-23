# Women Who Code (Python) Challenge No. 3
# Write a function to count the number of vowels in a given string.

from collections import Counter
import time

def displayIntro():
    print('Type a phrase and I will tell you how many vowels are in that sentence.')
    
def vowelcount(phrase):
    counts=Counter()
    phrase=phrase.lower()

    for char in phrase:
        if char in 'aeiou':
            counts[char]+=1

    return counts
    
playAgain = 'yes'
while playAgain=='yes' or playAgain == 'y':
    displayIntro()
    phrase=input()
    print(vowelcount(phrase))
    time.sleep(2)
    print('Do you want to try another phrase? (yes or no)')
    playAgain=input()

