# Women Who Code (Python) Challenge No. 17
# Create a program that capitalizes the first letter of each word in a sentence.

# Function
def capitalize_first_letter(sentence):
    capitalized_sentence = sentence.title()
    return capitalized_sentence

# Get user input
sentence = input('Please type a sentence and I will capitalize every word: ')

# Get and print result
result = capitalize_first_letter(sentence)
print(result)
