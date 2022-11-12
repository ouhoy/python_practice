import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

rand_computer_cards  = [random.choice(cards), random.choice(cards)]
rand_user_cards  = [random.choice(cards), random.choice(cards)]

def calc_score(score):
    score_sum = 0
    for i in score:
        score_sum += i
    return score_sum

def get_another_card():
    rand_computer_cards.append(random.choice(cards))
    rand_user_cards.append(random.choice(cards))
    start_game()

def have_ace(cards_list):
    if not 11 in cards_list:
        return False
    if 11 in cards_list:
        if sum(cards_list) - 10 > 21:
            return False
        else:
            return True 


def start_game():
    computer_score = calc_score(rand_computer_cards)
    user_score = calc_score(rand_user_cards)
    if user_score == 21:
        print("user wins")
        return
    if computer_score == 21:
        print("computer wins")
        return
    else:
        if user_score > 21:
            if not have_ace(user_score):
                print("Lose")
            else:
                wanna_draw = input("Do you want to get another card? if yes type y otherwise type n ").lower().strip()
                if wanna_draw == "y":
                    get_another_card()
                # if wanna_draw == "no":