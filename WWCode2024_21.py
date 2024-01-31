# Women Who Code (Python) Challenge No. 21
# Create a program to remove a specific element from a set.

# Function
def remove_element(unique_set, element_to_remove):
    try:
        unique_set.remove(element_to_remove)
        print(f'{element_to_remove} removed successfully.')
    except KeyError:
        print(f'{element_to_remove} not found in the set.')

# Get list from user - convert to set
user_input = input('Create a set by entering elements separated by spaces: ')
user_list = user_input.split(' ')
unique_set = set(user_list)

# Get element to remove from user
element_to_remove = input('Which element would you like me to remove: ')

# Remove element
remove_element(unique_set, element_to_remove)

# Print results
print(f'Original list: {user_list}')
print(f'Set with removed element: {unique_set}. \nNote: Any duplicates were also removed.')
