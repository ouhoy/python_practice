from turtle import Turtle


class Paddle(Turtle):
    STEPS = 20
    SCREEN_EDGE = 240

    def __init__(self):
        super().__init__()
        self.create_pong()

    def create_pong(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

        self.goto(x=350, y=0)

    def up(self):
        if self.ycor() == self.SCREEN_EDGE:
            return

        new_ycor = self.ycor() + self.STEPS
        self.goto(self.xcor(), new_ycor)

    def down(self):
        if self.ycor() == -self.SCREEN_EDGE:
            return
        new_ycor = self.ycor() - self.STEPS
        self.goto(self.xcor(), new_ycor)
