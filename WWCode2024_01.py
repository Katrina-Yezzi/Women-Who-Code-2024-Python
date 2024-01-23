# WWCode Day 1 Python Challenge...
# Create a program that swaps the values of two variables.

# Ask for user for two values
var1= input('Enter the value of the 1st variable: ')
var2 = input('Enter the value of the 2nd variable: ')

# Print the results
print('\nOriginal values of the variables:') #The \n creates a new line
print('Variable 1 = ', var1)
print('Variable 2 = ', var2)

# Swap
tmp = var1 #You need to create a temporary holder for the var 1 since you change its value in the next line.
var1 = var2
var2 = tmp

# Print the results
print('\nThe new values are as follows...')
print('Variable 1 = ', var1)
print('Variable 2 = ', var2)

### Another way to do it...

#Create a program that swaps the values of two variables.

print('\nLet\'s try a different way...')

def swap_value(a, b):
  a,b = b, a
  print('\nWith the swap, we have...,', a, b)

# Ask for user for two values
var1= input('Enter the value of the 1st variable: ')
var2 = input('Enter the value of the 2nd variable: ')

# Print the results
print('\nOriginal values of the variables:') #The \n creates a new line
print('Variable 1 = ', var1)
print('Variable 2 = ', var2)

swap_value(var1, var2)





 
