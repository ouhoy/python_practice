import random
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
screen.onkeypress(player.go_up, "Up")

car_list = []

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    random_chance = random.randint(1, 6)
    if random_chance == 1:
        car_list.append(CarManager())
    for car in car_list:
        car.move_car()
