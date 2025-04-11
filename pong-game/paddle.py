from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.setx(x_pos)

    def move_up(self):
        self.sety(self.ycor()+20)

    def move_down(self):
        self.sety(self.ycor()-20)
