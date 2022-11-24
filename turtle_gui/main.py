from turtle import Turtle

tim = Turtle()

# Draw a Square
for _ in range(4):
    tim.forward(100)
    tim.left(90)

# Draw a Dashed Line
for _ in range(15):
    tim.forward(10)
    tim.color("white", "black")
    tim.forward(10)
    tim.color("black")

