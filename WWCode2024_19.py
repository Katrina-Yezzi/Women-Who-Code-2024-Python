# Women Who Code (Python) Challenge No. 19
# Write a function to calculate the factorial of a number.

#Function
def factorial_num(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_num(n - 1)

# Ask for user input
n = int(input('Enter a non-negative number and I will calculate its factorial: '))

#Call function to calculate factorial
result = factorial_num(n)

#Print result
print(f'The factorial of {n} is: {result}')

'''
Note that there is a built in function for calculating factorials in Python.

import math
math.factorial(n)

You can use this to check your work.
'''
