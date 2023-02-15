from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.initiate_snake()
        self.snake_head = self.segments[0]

    def initiate_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        start = len(self.segments) - 1
        stop = 0
        step = -1

        for segment_num in range(start, stop, step):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()

            self.segments[segment_num].goto(new_x, new_y)

        self.snake_head.forward(MOVE_DISTANCE)
