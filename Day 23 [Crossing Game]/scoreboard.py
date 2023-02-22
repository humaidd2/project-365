from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 280)
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.level}", font=FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT)
