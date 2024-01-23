# Women Who Code (Python) Challenge No. 2
# Create a program to calculate the area of a circle given its radius

from math import pi
import time

def displayIntro():
    print('''Please allow me to help you calculate the area of a circle based on its radius.
Please tell me, what is the radius of the circle?''')

def areaCirc(radius):
    area=pi*radius**2
    print(f'The area of the circle with radius {radius} is {round(area)}.')
    
playAgain = 'yes'
while playAgain=='yes' or playAgain == 'y':
    displayIntro()
    radius=float(input())
    areaCirc(radius)
    time.sleep(2)

    print('Do you want to try another? (yes or no)')
    playAgain=input()

    

