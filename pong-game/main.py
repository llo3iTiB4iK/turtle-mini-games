import time
from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

scoreboard = Scoreboard()
left_paddle = Paddle(x_pos=-450)
right_paddle = Paddle(x_pos=450)
ball = Ball()

screen.update()
screen.listen()
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.tracer(1)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.wall_bounce()
    collided_left_paddle = ball.distance(left_paddle) < 50 and -450 < ball.xcor() < -420
    collided_right_paddle = ball.distance(right_paddle) < 50 and 420 < ball.xcor() < 450
    if collided_left_paddle or collided_right_paddle:
        ball.paddle_bounce()
    if ball.xcor() >= 500:
        scoreboard.increase_left()
        ball.reset_position()
    if ball.xcor() <= -500:
        scoreboard.increase_right()
        ball.reset_position()

screen.exitonclick()
