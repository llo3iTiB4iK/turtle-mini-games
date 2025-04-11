from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.sety(260)
        self.update_scoreboard()
        self.hideturtle()

    def increase_left(self):
        self.left_score += 1
        self.update_scoreboard()

    def increase_right(self):
        self.right_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.left_score} : {self.right_score}", align=ALIGNMENT, font=FONT)
