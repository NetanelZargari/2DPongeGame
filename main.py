from turtle import Turtle, Screen
from players import Players
from ball import Ball
import time
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

player1 = Players((350, 0))
player2 = Players((-350, 0))
ball = Ball()
score = Score()


screen.listen()
screen.onkey(player1.go_up, "Left")
screen.onkey(player1.go_down, "Right")
screen.onkey(player2.go_up, "d")
screen.onkey(player2.go_down, "a")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # paddle
    if ball.distance(player1) < 50 and ball.xcor() > 320 or ball.distance(player2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # right side
    if ball.xcor() > 380:
        score.l_point()
        ball.reset_ball()

    # left side
    if ball.xcor() < -380:
        score.r_point()
        ball.reset_ball()


screen.exitonclick()
