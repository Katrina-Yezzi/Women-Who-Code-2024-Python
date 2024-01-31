# Women Who Code (Python) Challenge No. 20
# Write a function that takes a list of numbers and returns a new list containing only the even numbers.

# Function
def filter_even_numbers(numbers):
    even_numbers = [int(num) for num in numbers if int(num) % 2 == 0]
    return even_numbers

# Get user input
numbers = input('Enter a series of numbers separated by spaces, and I will return a list containing only the even numbers: ').split(' ')

# Filter numbers
result = filter_even_numbers(numbers)

# Print results
print(f'Original list: {numbers}')

if result:
    print(f'List with only even numbers: {result}')
else:
    print(f'No even numbers found in the original list.')

