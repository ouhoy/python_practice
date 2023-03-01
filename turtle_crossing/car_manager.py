from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        self.penup()
        self.shape("square")
        self.shapesize(20, 40)
        self.goto(0, 0)

    def move(self):
        self.forward(MOVE_INCREMENT)
