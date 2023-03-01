import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkeypress(player.move, "Up")

loop_counter = 0
car_list = []
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    loop_counter += 1
    if loop_counter % 6 == 0:
        car_list.append(CarManager())
        for car in car_list:
            car.move()
