from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()

    def up(self):
        move_cor_y = self.ycor() + 20
        x_cor = self.xcor()
        self.goto(x_cor, move_cor_y)

    def down(self):
        move_cor_y = self.ycor() - 20
        x_cor = self.xcor()
        self.goto(x_cor, move_cor_y)
