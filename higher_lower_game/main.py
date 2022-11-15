import random

from game_data import data
from art import logo, vs

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
    global account_a, account_b
    if guess == "a" and a >= b or guess == "b" and b >= a: 
        if a >= b:
            account_b =  random_account(data)
        else:
            account_a =  random_account(data)    
        return True 
    else: return False

has_lost = False  
print(logo)
while not has_lost:
    print("Compare A: ",get_data(account_a))
    print(vs, f"\n Against B: {get_data(account_b)}")

    comparison = input("Type 'A' or 'B' ").lower().strip()
    if comparison != "a" and comparison != "b":
        continue
    if compare_followers(comparison, account_a["follower_count"], account_b["follower_count"]):
        score += 1
        print(f"Your score is {score}") 

    else:
        print(f'''You have lost {account_a["name"]} has {account_a["follower_count"]} followers and {account_b["name"]} has {account_b["follower_count"]} followers''')   
        has_lost = True 