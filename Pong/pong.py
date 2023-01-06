import turtle
import winsound

score_a = 0
score_b = 0

end_score = int(input("Enter the winning score: "))

win = turtle.Screen()
win.title("Pong Game")
win.bgcolor("black")
win.setup(800, 600)
win.tracer(0)

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.penup()
paddle_b.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 15, "bold"))


def paddle_a_up():
    y = paddle_a.ycor()
    y += 25
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 25
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 25
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 25
    paddle_b.sety(y)


win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

while (score_a < end_score) and (score_b < end_score):
    win.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("PongSound.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("PongSound.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 15, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 15, "bold"))

    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("PongSound.wav", winsound.SND_ASYNC)

    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("PongSound.wav", winsound.SND_ASYNC)
