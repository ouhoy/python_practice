import random
from turtle import Turtle

tim = Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]


def dashed_line():
    for _ in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


def square():
    for _ in range(4):
        tim.right(90)
        tim.forward(100)


def pentagon(sides):
    deg = 360 / sides
    for _ in range(sides):
        tim.right(deg)
        tim.forward(100)


def triangle():
    for _ in range(3):
        tim.right(120)
        tim.forward(100)


def draw_shape(sides_num):
    deg = 360 / sides_num
    for _ in range(sides_num):
        tim.forward(100)
        tim.right(deg)


"""for number_of_sides in range(3, 11):
    draw_shape(number_of_sides)"""

# deprecated code
"""def tim_directions(des, deg):
    directions_list = ["forward", "back", "right", "left"]
    random_direction = random.choice(directions_list)
    if random_direction == "forward":
        tim.forward(des)
    elif random_direction == "back":
        tim.back(des)
    elif random_direction == "right":
        tim.right(deg)
    elif random_direction == "left":
        tim.left(deg)


for _ in range(0, 50):
    tim.color(random.choice(colors))
    tim_directions(des=50, deg=120)
"""


def random_walk(steps):
    tim.pensize(15)
    tim.speed("fastest")
    for _ in range(steps):
        tim.color(random.choice(colors))
        tim.forward(30)
        tim.setheading(random.choice(directions))


random_walk(200)
