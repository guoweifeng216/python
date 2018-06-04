import turtle

def main():
    ## Draw an American flag.
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(10)
    drawRectangle(t, -200, 0, 380, 200, "red", "red")
    for i in range(1, 13, 2): 
        drawRectangle(t, -200, (200/13)*i , 380, (200/13), "red", "white") 
    drawRectangle(t, -200, (200/13)*6, (2/5)*380, (200/13)*7, "blue", "blue")
    for i in range(5):
        y = 180 - (20 * i)
        for j in range(6):
            x = -190 + 25*j
            drawFivePointStar(t, x, y, 8, "white") 
    for i in range(4):
        y = 170 - (20 * i)
        for j in range(5):
            x = -177 + 25*j
            drawFivePointStar(t, x, y, 8, "white")
            
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

main()        
