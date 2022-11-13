import random

easy_level = 10
hard_level = 5
numbers = []

game_mode = input("10 guesses in easy mode, only 5 guesses in hard mode. type 'easy' or 'hard' ").lower().strip()
guessed_number = int(input("Guess a number from 1 to 100 ").strip())

for i in range(1, 101):
    numbers.append(i)
answer = random.choice(numbers)

def play_game(mode, guessed_num):
    if mode == 0: 
        print(f"You lost, the right number was {answer}.")
        return 
    if guessed_num == answer: 
        print(f"You got the right number {answer}.")
        return 
    elif guessed_num > answer:
        mode -=1
        print(f"Too high")
        new_num = int(input(f"You have {mode} tries left. Guess another number: ").strip())
        return play_game(mode, new_num)
    elif guessed_num < answer:
        mode -=1
        print(f"Too low")
        new_num = int(input(f"You have {mode} tries left. Guess another number: ").strip())
        return play_game(mode, new_num)
if game_mode == 5:
    play_game(5, guessed_number)
else:
    play_game(10, guessed_number)
