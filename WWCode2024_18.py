# Women Who Code (Python) Challenge No. 18
# Create a program to find the largest among three numbers.

# Function
def largest_number(numbers):
    largest = max(numbers)
    return largest

# Get user input
numbers = [float(x) for x in input("Enter three numbers separated by spaces and I will find the largest among them: ").split()]

# Print results
if len(numbers) != 3:
    print("Please enter exactly three numbers.")
else:
    largest = largest_number(numbers)
    print(f"The largest number is: {largest}")

