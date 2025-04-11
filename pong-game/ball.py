from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_shift = 10
        self.y_shift = 10
        self.move_speed = 0.05

    def move(self):
        self.goto(self.xcor() + self.x_shift, self.ycor() + self.y_shift)

    def wall_bounce(self):
        self.y_shift *= -1

    def paddle_bounce(self):
        self.x_shift *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.hideturtle()
        self.home()
        self.showturtle()
        self.paddle_bounce()
        self.move_speed = 0.05
