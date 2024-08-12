# Crossy-road imitation game created by Alexander Peng on 2024/08/12.
# Uses Turtle graphics and Object-Oriented Programming.

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
manager = CarManager()

screen.listen()

screen.onkeypress(fun=player.move_forward, key="Up")
screen.onkeypress(fun=player.move_backward, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(0.01)

    screen.update()

    manager.create_car()
    manager.move()

    for car in manager.cars:
        if abs(car.xcor() - player.xcor()) < 29 and abs(car.ycor() - player.ycor()) < 23:
            game_is_on = False
        elif car.xcor() < -350:
            manager.delete_car(car)

    if player.at_finish_line():
        player.reset_position()
        scoreboard.increase_level()
        manager.increase_speed()

scoreboard.game_over()

screen.exitonclick()
