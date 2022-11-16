MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
is_working = True
money = 0
def en_res(res):
    if res >  resources[res]:
        print(f"Sorry you don't have enough {res}")
        return False
    else: return True

def check_resources(drink):
    water = MENU[drink]["ingredients"]["water"]
    coffee = MENU[drink]["ingredients"]["coffee"]
    if "milk" in MENU[drink]["ingredients"]: milk = MENU[drink]["ingredients"]["milk"]
    res = {water, milk, coffee}
    if water > resources["water"]:
        print(f"Sorry there is not enough water")
        return False
    if milk > resources["milk"] and drink !="espresso":
        print(f"Sorry there is not enough milk")
        return False
    if coffee > resources["coffee"]:
        print(f"Sorry there is not enough coffee")
        return False
    return True 
print(check_resources("espresso"))

drink_type = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
if drink_type == "off":
    is_working = False
if drink_type == "report":
    print(f'''
Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: {money}
 ''')   
    
