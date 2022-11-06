import random

from hangman_words import word_list
from hangman_art import logo, stages
stages = stages
print(logo)
right_combonation = False
lives = len(stages)
word_list = word_list
chosen_word = list(random.choice(word_list))
display = []
wrong_gussed_letter = []

for num in range(0, len(chosen_word)):
    display.append("_")

while not right_combonation:
    gussed_letter = input("Guess a letter: ").lower()
    for i in range(0, len(chosen_word)):
        if gussed_letter == chosen_word[i]:
            display[i] = chosen_word[i]
    print("Getting close: ","".join(display))
    if "_" not in display:
        right_combonation = True
        print("You won!!")
    if gussed_letter not in chosen_word:
        if gussed_letter in wrong_gussed_letter:
            print("You have already gussed that letter!")
        else:    
            wrong_gussed_letter.append(gussed_letter)
            lives -= 1
            print(stages[lives])
            print(f'The letter "{gussed_letter.upper()}" is not in the word. You lose a life.')
            if lives <= 0:
                right_combonation = True
                print(f"You lost!")
                print("The word you were looking for was: ", "".join(chosen_word).upper())