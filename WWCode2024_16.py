# Women Who Code (Python) Challenge No. 16
# Write a function that counts the frequency of each word in a sentence.

# Function
def count_words(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Create an empty dictionary to store word frequencies
    word_frequency = {}

    # Reformat input
    for word in words:
        word = word.strip(".,!?()[]{}:;\"'")
        word = word.lower()

        # Get frequencies, update dictionary
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    return word_frequency

# Get user input
sentence = input('''Please type a sentence and I will count the frequency of each word in that sentence: ''')

# Get results
answer = count_words(sentence)

# Print results
for word, frequency in answer.items():
    print(f"{word}: {frequency}")
