import random
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.starting_x = 0
        self.starting_y = random.randint(-250, 250)
        self.goto(self.starting_x, self.starting_y)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def ball_movement(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(self.starting_x, self.starting_y)
        self.move_speed = 0.1
        self.bounce_x()
