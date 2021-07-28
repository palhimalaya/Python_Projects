import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.move, "Up")

while scoreboard.is_game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detect Collision with car
    for cars in car_manager.all_car:
        if player.distance(cars) < 20:
            scoreboard.game_over()

    # Detect player is on finish line
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
        car_manager.move_speed()

screen.exitonclick()
