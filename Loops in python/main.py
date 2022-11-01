'''
### For In Array ###

fruits = ["Apple", "Orange", "Peach"]
for fruit in fruits:
    print(fruit)


### Find The Highest Number Without Using The Max() Function. ###
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

max_score = 0;

for score in student_scores:
    if score > max_score:
        max_score = score

print(f"The highest score in the class is: {max_score}")
'''
### Fizz Buzz Game ###

for number in range(1,100):
    if not ((number % 3 ==0 and number % 5 == 0) or ( number % 3 == 0) or (number % 5 == 0)) :
            print(number)
    else:
            if ( number % 3 == 0) and (number % 5 == 0):
                print("FizzBuzz")
            elif number % 3 == 0:
                print("Fizz")   
            elif number % 5 == 0:
                print("Buzz")

