import random
import os
from game_data import data
from art import logo, vs

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def random_account(account):
    return random.choice(account)

account_a = random_account(data)
account_b = random_account(data)
score = 0
def get_data(data):
    name = data["name"]
    description = data["description"]
    country = data["country"]
    return f"{name}, a {description}, from {country}"

def compare_followers(guess, a ,b):
    if a > b:
        return guess == "a"
    else:
        return guess == "b"    

has_lost = False  

while not has_lost:
    cls()
    print(logo)
    if score > 0: print(f"You are right! Current score: {score}")
    while account_a == account_b:
       account_b: random_account(data)
    print("Compare A: ",get_data(account_a))
    print(vs, f"\n Against B: {get_data(account_b)}")
    comparison = input("Who has more followers? Type 'A' or 'B': ").lower().strip()

    if comparison != "a" and comparison != "b":
        continue
    is_right_answer = compare_followers(comparison, account_a["follower_count"], account_b["follower_count"])
    if is_right_answer:
        if account_a["follower_count"] >= account_b["follower_count"]: 
            account_b =  random_account(data)
        else: 
            account_a =  account_b
            account_b = random_account(data)
        score += 1
        
    else:
        print(f"Sorry that's worng. Final score {score}")
        print(f'''{account_a["name"]} has {account_a["follower_count"]}M followers while {account_b["name"]} has {account_b["follower_count"]}M followers.''')   
        has_lost = True 