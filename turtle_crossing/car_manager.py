from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STAMP_SIZE = 20
HEIGHT = 20
WIDTH = 40
START_LINE_X = 310


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        self.shape("square")
        self.color(random.choice(COLORS))
        self.right(-90)
        self.penup()
        self.shapesize(WIDTH / STAMP_SIZE, HEIGHT / STAMP_SIZE)
        self.goto(START_LINE_X, random.randint(-240, 240))

    def move(self):
        x_cord = self.xcor() - MOVE_INCREMENT
        if x_cord == -START_LINE_X:
            self.color("white")
            return
        self.goto(x_cord, self.ycor())
