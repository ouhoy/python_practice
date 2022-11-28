import os

# hello_world = 1
# print("hello_world")
# print("123")
# print(89.6)

# house = 35.0
# rate = 12.50
# pay = house * rate
# print(pay)

# x = 0.6
# x = 3.9 * x * (1-x),
# print(x)

# ddd = "1" +"1"
# print(type(ddd))
# x = 1 > 2 
# print(x)

# name = input("Who are you? ")
# print(f"Welcome back {name}!!")

# inp = input("Europe Floor? ")
# usf = int(inp) + 1
# print(f"US floor {usf}")
is_valid = True

while is_valid:
    try:
        working_hours = float(input("How many working hours? ").strip())
        worker_rate = float(input("Enter the rate: ").strip())
        if working_hours > 40:
            over_working_hours = working_hours - 40
            over_hours_rate = worker_rate * 1.5
            over_hours_payment = 40 * worker_rate + (over_working_hours * over_hours_rate)
            print(f"Your payment is going to be ${over_hours_payment}")
        else:
            pay = working_hours * worker_rate
            print(f"Your payment is going to be ${pay}")
        is_valid = False
    except:
        print("Please put a valid number")
