from turtle import Turtle

tim = Turtle()


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
    deg = 360/sides
    for _ in range(sides):
        tim.right(deg)
        tim.forward(100)


def triangle():
    for _ in range(3):
        tim.right(120)
        tim.forward(100)


triangle()
square()
for num in range(5, 9):
    pentagon(num)

