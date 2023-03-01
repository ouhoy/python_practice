from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.right(-90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

        # When the turtle hits the top edge of the screen
        y_position = self.ycor()
        if y_position > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
