import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard()

paddle1 = Paddle()
paddle1.goto(350, 0)

paddle2 = Paddle()
paddle2.goto(-350, 0)

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.ball_movement()

    # Collision with wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    # Collision with paddle1
    if ball.distance(paddle1) < 40 and ball.xcor() > 300 or ball.distance(paddle2) < 40 and ball.xcor() < -300:
        ball.bounce_x()

#     Paddle1 Miss
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.increase_l_score()

    # Paddle2 Miss
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.increase_r_score()


screen.exitonclick()
