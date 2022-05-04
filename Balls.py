#Ball 1
ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("circle")
ball1.color("white")
ball1.penup()
ball1.goto(0,0)
ball1.dx = 2
ball1.dy = -2

#Ball 2
ball2 = turtleTurtle()
ball2.speed(0)
ball2.shape("circle")
ball2.color("white")
ball2.penup()
ball2.goto(0,0)
ball2.dx = -2
ball2.dy = -2

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0  Player 2: 0", align="center")