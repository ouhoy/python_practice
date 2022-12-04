from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
