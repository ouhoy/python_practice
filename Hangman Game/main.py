import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
right_combonation = False
lives = len(stages)
word_list = ["raccoon", "banana", "camel", "fish"]
chosen_word = list(random.choice(word_list))
display = []
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
        lives -= 1
        print(stages[lives])
        if lives <= 0:
            right_combonation = True
            print("You lose!")