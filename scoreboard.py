from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("dataa.txt") as data:`
            self.high_score = data.read()
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.write(f"score = {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"score = {self.score} high_score = {self.high_score}", align="center", font=("Arial", 16, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score > self.high_score:
            self.score = self.high_score
            with open("dataa.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_score()

    def score_increase(self):
        self.score += 1
        # self.clear()
        self.update_score()
