import re #regex library

def word_frequency(word):
    word_dictionary= re.split(r'[ .,]+', word)
    word_dictionary = [item.lower() for item in word_dictionary]
    frequency = {}
    for i in word_dictionary:
        count = 0
        for n in word_dictionary:
            if n == i:
                count += 1
            frequency[i] = count
    print(frequency)
    return frequency

try:
    with open("../files/word_file.txt", "r") as file:
        content = file.read()
        word_frequency(content)
except FileNotFoundError:
    print(f"Error: The file word_file.txt was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
