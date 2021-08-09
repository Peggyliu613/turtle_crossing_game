import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")

screen.listen()

game_is_on = True
time_sleep = 0.1
create_car = 1
while game_is_on:
    time.sleep(time_sleep)
    screen.update()

    if create_car % 5 == 0:
        car_manager.create_car()
    create_car += 1
    car_manager.drive_car()

    if player.ycor() > 280:
        player.go_to_next_level()
        scoreboard.go_to_next_level()
        car_manager.go_to_next_level()
        time_sleep *= 0.8

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()