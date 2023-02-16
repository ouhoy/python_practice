from circle import Circle
from turtle import Screen

screen = Screen()

screen.setup(width=600, height=600)
screen.title("Circle")

red_circle = Circle(20, (0, 0), "red")

red_circle.move((200, 20))
red_circle.draw(29)

blue_circle = Circle(10, (0, 0), "blue")

screen.exitonclick()
