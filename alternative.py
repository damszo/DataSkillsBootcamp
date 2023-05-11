# Asking user for input string.

input_sentence = input("Write a sentence to be converted: ")

# Blank string to store the string with alternate letters capital and smaller.

alternate_string = ""

# Loop to convert letters to upper case and lower case.

for i in range(len(input_sentence)):
    if i % 2 == 0:
        alternate_string += input_sentence[i].upper()
    else:
        alternate_string += input_sentence[i].lower()

print(alternate_string)

# Starting with the same input string, but making each alternative word lower and upper case.
# Input string is first split into a list of words. And a blank list is created to store modified words.

words = input_sentence.split()
modified_words = []

# For loop iterates over each word in the 'words' list and checks its index using enumerate funcion. If even=converts to lowercase, if odd=uppercase.

for i, word in enumerate(words):
    if i % 2 == 0:
        modified_words.append(word.lower())
    else:
        modified_words.append(word.upper())

# Modified words in the 'modified_words' list are joined creating a modified string, which is printed.

modified_string = " ".join(modified_words)
print(modified_string)