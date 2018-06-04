import turtle

def main():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(10)
    t.down()
    drawRectangle(t, 0, 0, 150, 100, colorP="black")
    drawRectangle(t, 75, 50, 75, 50, colorP="red", colorF="red")
    drawRectangle(t, 0, 0, 75, 50, colorP="blue", colorF="blue")
    drawFivePointStar(t, 30, 65, 20, "blue", "blue")
    drawFivePointStar(t, 105, 15, 20, "red", "red")

def drawFivePointStar(t, x, y, lenthOfSide, colorP="black", colorF="white"):    
    t.up()
    t.goto(x, y)
    t.setheading(0)
    t.pencolor(colorP)
    t.fillcolor(colorF)
    t.left(36)
    t.down()
    t.begin_fill()
    for i in range(6):
        t.forward(lenthOfSide)
        t.left(144)
    t.end_fill()
    
def drawRectangle(t, x, y, w, h, colorP="black", colorF="white"):
    # Draw a rectangle with bottom-left corner (x, y),
    # width w, height h, pencolor colorP, and fill color colorF.
    originalPenColor = t.pencolor()
    originalFillColor = t.fillcolor()
    t.pencolor(colorP)
    t.fillcolor(colorF)
    t.up()
    t.goto(x , y)         # bottom-left corner of rectangle
    t.down()
    t.begin_fill()
    t.goto(x + w, y)      # bottom-right corner of rectangle
    t.goto(x + w, y + h)  # top-right corner of rectangle
    t.goto(x, y + h)      # top-left corner of rectangle
    t.goto(x , y)         # bottom-left corner of rectangle
    t.end_fill()
    t.pencolor(originalPenColor)
    t.fillcolor(originalFillColor)

def drawDot(t, x, y, diameter, colorP):
    # draw dot with center (x, y) having color colorP
    t.up()
    t.goto(x, y)
    t.dot(diameter, colorP)    
    
main()        
