import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()

    #   Detect turtle end cross
    if turtle.ycor() > 270:
        turtle.reset_turtle()
        scoreboard.increase_score()
        cars.increase_speed()

    # Detect Collision with cars

    for car in cars.all_cars:
        if car.distance(turtle) < 20:
            scoreboard.game_over()
            game_is_on = False
