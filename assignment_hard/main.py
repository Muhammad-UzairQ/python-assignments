from hangman import hangman
from utils import *
import random as r
from constants import *

words_list = get_list_from_file('words_list.csv')
word = list(r.choice(words_list))

#print(word) #For testing purpose, if you want to see what the word is, uncomment this line

copied_word = list(word)
guessed_word_list = ["_"] * len(word)

print("Welcome to Hangman!")
print("You will be Guessing the word, total 6 Wrong Guesses allowed.")
print("Good luck!")
hangman(WRONG_GUESSES)
print(' '.join(guessed_word_list))

while True:
    if WRONG_GUESSES == WRONG_GUESSES_ALLOWED:
        print("You lose! The word was", ' '.join(word))
        break
    elif guessed_word_list == word:
        print("You won! The word was", ' '.join(word))
        break
    else:
        guess = input("Guess a letter: ")
        copied_word,guessed_word_list,IS_GUESS_CORRECT = compare_list(copied_word, guessed_word_list,guess)
        if IS_GUESS_CORRECT:
            print("Correct!")
            print(' '.join(guessed_word_list))
            hangman(WRONG_GUESSES)
        else:
            print("Incorrect!")
            print(' '.join(guessed_word_list))
            WRONG_GUESSES += 1
            hangman(WRONG_GUESSES)




