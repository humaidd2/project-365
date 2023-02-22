import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 3
        self.all_cars = []

    def create_car(self):
        if random.randint(0, 7) == 4:
            car = Turtle("square")
            car.penup()
            car.goto(290, random.randint(-250, 250))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.setheading(180)
            car.forward(self.STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT
