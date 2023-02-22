from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        with open("high_score.txt") as content:
            self.high_score = int(content.read())
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.high_score:
            with open("high_score.txt", mode="w") as content:
                content.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()
    #
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align="center", font=("Arial", 20, "normal"))
