import turtle

t = turtle.Turtle()
t.hideturtle()
t.color("red", "red")
t.up()
t.goto(-30, -40)
t.down()
t.begin_fill()
t.goto(-30, 60)
t.goto(50, 60)
t.goto(50, -40)
t.goto(-30, -40)
t.end_fill()
