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
    "money": 0
}
is_working = True


def check_resources(drink):
    water = MENU[drink]["ingredients"]["water"]
    coffee = MENU[drink]["ingredients"]["coffee"]
    if "milk" in MENU[drink]["ingredients"]: 
        milk = MENU[drink]["ingredients"]["milk"]
        if milk > resources["milk"]:
            print(f"Sorry there is not enough milk")
            return False

    if water > resources["water"]:
        print(f"Sorry there is not enough water")
        return False
    if coffee > resources["coffee"]:
        print(f"Sorry there is not enough coffee")
        return False
    return True 

def change_resources(drink):
    drink_cost = MENU[drink]["cost"]
    water = MENU[drink]["ingredients"]["water"]
    coffee = MENU[drink]["ingredients"]["coffee"]
    if "milk" in MENU[drink]["ingredients"]: 
        milk = MENU[drink]["ingredients"]["milk"]
        resources["milk"] -= milk 
    resources["water"] -=  water
    resources["coffee"] -=  coffee
    resources["money"] +=  drink_cost

while is_working:
    drink_type = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
    if drink_type == "off":
        
        print("Turning off the machine...")
        is_working = False
        break
    if drink_type == "report":
        print(f'''
    Water: {resources["water"]}ml
    Milk: {resources["milk"]}ml
    Coffee: {resources["coffee"]}g
    Money: ${resources["money"]}
    ''')   
        continue
    if not (drink_type == "espresso" or  drink_type == "latte" or drink_type == "cappuccino"):
        print("Please make sure you put a valid drink...")  
        continue
    if check_resources(drink_type):
        quaters = float(input("How many quaters?: ")) * 0.25
        dimes = float(input("How many dimes?: ")) * 0.10
        nickles = float(input("How many nickles?: ")) * 0.05
        pennies = float(input("How many pennies?: ")) * 0.01
        inserted_coins = quaters + dimes + nickles + pennies
        drink_cost = MENU[drink_type]["cost"]
    if drink_cost > inserted_coins:
        inserted_coins = 0
        print("Sorry that's not enough money. Money refunded.")
    elif drink_cost < inserted_coins:
        change = inserted_coins - drink_cost
        change_resources(drink_type)
        print(f"“Here is ${round(change, 2)} dollars in change.")
        print(f"Here is your {drink_type}. Enjoy!")
    else:
         change_resources(drink_type)
         print(f"Here is your {drink_type}. Enjoy!")

