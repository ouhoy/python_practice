import random

from game_data import data
from art import logo, vs

# data.index(random_choice_a)
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
    if guess == "a" and a >= b or guess == "b" and b >= a: return True 
    else: return False

has_lost = False  
while not has_lost:
    print(logo)
    print("Compare A: ",get_data(account_a))
    print(vs, f"\n Against B: {get_data(account_b)}")

    comparison = input("Type 'A' or 'B' ").lower().strip()
    if compare_followers(comparison, account_a["follower_count"], account_b["follower_count"]):
        score += 1
        if account_a["follower_count"] >= account_b["follower_count"]:
            account_b =  random_account(data)
        else:
            account_a =  random_account(data)    
        print(f"Your score is {score}") 
    
    else:
        print("You have lost")   
        has_lost = True 