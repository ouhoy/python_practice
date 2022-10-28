import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps_graphs = [rock, scissors ,paper]
rock_paper_scissors = ["rock", "scissors", "paper"]

user_input = int(input("Type 0 for Rock, 1 for Paper or 2 Scissors "))
print(rps_graphs[user_input])

user_choice = rock_paper_scissors[user_input]
randint = random.randint(0,2)
computer_choice = rock_paper_scissors[randint]
print(f"Computer Choose: \n{rps_graphs[randint]}")


if user_choice == computer_choice:
    print("It's a draw")
elif (user_choice == "rock" and computer_choice == "scissors") or ( user_choice == "scissors" and computer_choice == "paper" ) or ( user_choice == "paper" and computer_choice == "rock" ):
    print(f"You won!")
else:
    print("You lose!")

