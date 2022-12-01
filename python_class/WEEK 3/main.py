hours = float(input("How many hours? "))
rate = float(input("Rate "))


def compute_pay(working_hours, worker_rate):
    if working_hours > 40:
        over_working_hours = working_hours - 40
        over_hours_rate = worker_rate * 1.5
        pay = 40 * worker_rate + (over_working_hours * over_hours_rate)
        return pay

    else:
        pay = working_hours * worker_rate
        return pay


print(f"Your payment is going to be ${compute_pay(hours, rate)}")

# is_valid = True

# while is_valid:
#     try:
#         working_hours = float(input("How many working hours? ").strip())
#         worker_rate = float(input("Enter the rate: ").strip())
#         if working_hours > 40:
#             over_working_hours = working_hours - 40
#             over_hours_rate = worker_rate * 1.5
#             over_hours_payment = 40 * worker_rate + (over_working_hours * over_hours_rate)
#             print(f"Your payment is going to be ${over_hours_payment}")
#         else:
#             pay = working_hours * worker_rate
#             print(f"Your payment is going to be ${pay}")
#         is_valid = False
#     except:
#         print("Please put a valid number")
#
#
#
