from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.write(f"{self.l_score} : {self.r_score}", font=("Arial", 24, "normal"))

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.update_score()
