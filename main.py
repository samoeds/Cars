import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle vs Cars")

player = Player()
scoreboard = Scoreboard()
cars_manager = CarManager()


screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars_manager.create_car()
    cars_manager.move_cars()

    # detect collision with a car
    for car in cars_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


    # detect collision with the top wall
    if player.is_at_finish():
        scoreboard.update_level()
        player.go_start()
        cars_manager.level_up()


screen.exitonclick()
