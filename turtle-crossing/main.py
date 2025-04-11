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
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move_cars()

    if car_manager.collision_with(player):
        game_is_on = False
        scoreboard.game_over()

    if player.has_finished():
        player.reset_player()
        scoreboard.increase_level()
        car_manager.increase_speed()

screen.update()
screen.exitonclick()
