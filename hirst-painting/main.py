import random
import turtle as turtle_module

tim = turtle_module.Turtle()
screen = turtle_module.Screen()
screen.colormode(255)
color_list = [(238, 242, 247), (247, 241, 244), (243, 247, 245), (133, 168, 205), (26, 40, 63), (233, 151, 98),
              (214, 131, 140), (235, 210, 92), (35, 114, 162), (31, 60, 55), (177, 58, 47), (51, 40, 44), (167, 29, 33),
              (239, 168, 153), (230, 164, 169), (159, 32, 29), (141, 184, 171), (213, 75, 64), (152, 60, 65),
              (26, 61, 114), (12, 90, 66), (173, 189, 218), (64, 108, 88), (112, 126, 160), (57, 51, 47),
              (213, 94, 100), (3, 88, 119), (148, 202, 232), (173, 201, 190)]

tim.hideturtle()
tim.penup()
tim.speed("fastest")
tim.setheading(225)
tim.forward(250)
tim.setheading(0)

for i in range(200):
    if i != 0 and i % 20 == 0:
        tim.right(-90)
        tim.forward(40)
        tim.right(90)
        tim.back(400)
    if i % 2 == 0:
        random_color = random.choice(color_list)
        tim.dot(20, random_color)
    else:
        tim.penup()
    tim.forward(20)

screen.exitonclick()
