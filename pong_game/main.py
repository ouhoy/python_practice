from turtle import Screen
from paddle import Paddle

screen = Screen()
paddle = Paddle()

screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
screen.onkeypress(paddle.up, "Up")
screen.onkeypress(paddle.down, "Down")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()
