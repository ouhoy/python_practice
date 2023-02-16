from turtle import Turtle


class Circle(Turtle):
    def __init__(self, rad: int, center: tuple[float, float], circle_color: str):
        super().__init__()
        self.rad = rad
        self.center = center
        self.circle_color = circle_color
        self.make_circle()

    def make_circle(self):
        self.color(self.circle_color)
        self.circle(self.rad)
        self.move(self.center)

    def move(self, center: tuple[float, float]):
        self.goto(center)
        self.penup()

    def draw(self, rad: int):
        self.pendown()
        self.circle(rad)
