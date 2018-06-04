import turtle

def main():
    #switzerland
    t = turtle.Turtle()
    t.hideturtle()
    drawRectangle2(t, (0,0), 100, 100, "red")
    drawRectangle2(t, (20,40), 60, 20, "white")
    drawRectangle2(t, (40,20), 20, 60, "white")

def drawRectangle2(t, startPoint, width, height, color):
    t.up()
    t.setheading(0)
    (x, y) = startPoint
    t.color(color)
    t.begin_fill()
    t.goto(x, y)
    t.down()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.end_fill()
    
main()    
        




