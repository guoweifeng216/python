import turtle

def main():
    # Draw flag of Niger.
    t = turtle.Turtle()
    t.hideturtle()
    drawFilledRectangle2(t, (0,0), 150, 33, "green")
    drawFilledRectangle2(t, (0,33), 150, 33, "white")
    drawFilledRectangle2(t, (0,66), 150, 33, "orange")
    t.up()
    t.goto(75,50)
    t.color("orange")
    t.dot(20)

def drawFilledRectangle2(t, startPoint, width, height, color):
    t.up()
    t.setheading(0)
    (x, y) = startPoint
    t.fillcolor(color)
    #t.color(color)   #replacement for above line for Swiss flag
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
        




