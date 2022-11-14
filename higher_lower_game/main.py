import random

from game_data import data
from art import logo, vs


# data.index(random_choice_a)

def get_data(data):
    name = random.choice(data)["name"]
    description = random.choice(data)["description"]
    country = random.choice(data)["country"]
    return f"{name}, a {description}, from {country}"
def compare_followers(guess, a ,b):
    if guess >= a: return True
    elif guess >= b: return True
    else: return False


print(logo)

print("Compare A: ",get_data(data=data))
print(vs, f"\n Against {get_data(data=data)}")
