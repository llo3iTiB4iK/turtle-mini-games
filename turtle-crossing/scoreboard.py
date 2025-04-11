from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.penup()
        self.goto(x=-280, y=260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Level: {self.current_level}", font=FONT)

    def increase_level(self):
        self.current_level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align="center", font=FONT)
