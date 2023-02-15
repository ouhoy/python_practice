from turtle import Screen, Turtle
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

snake_head = segments[0]
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    start = len(segments) - 1
    stop = 0
    step = -1

    for segment_num in range(start, stop, step):
        new_x = segments[segment_num - 1].xcor()
        new_y = segments[segment_num - 1].ycor()

        segments[segment_num].goto(new_x, new_y)

    snake_head.forward(20)
    snake_head.left(90)

screen.exitonclick()
