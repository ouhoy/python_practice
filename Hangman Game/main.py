import random

word_list = ["raccoon", "banana", "camel", "fish"]
chosen_word = list(random.choice(word_list))
print(chosen_word)
gussed_letter = input("Guess a letter: ").lower()

# for letter in chosen_word:
#     if gussed_letter == letter:
#         print(True)
#         chosen_word.remove(gussed_letter)
#         print(chosen_word)
#         break
#     else:
#         print(False)    

if gussed_letter in chosen_word:
    chosen_word.remove(gussed_letter)
print("".join(chosen_word))        