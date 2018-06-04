import turtle

def main():
    ## Draw the flag of Burkina Faso.
    t = turtle.Turtle()
    t.hideturtle()
    t.down()
    drawFilledRectangle(t, 0, 50, 150, 50, "red", "red")
    drawFilledRectangle(t, 0, 0, 150, 50, "forest green", "forest green")
    drawFivePointStar(t, 65, 33, 40, "yellow", "yellow")

def drawFivePointStar(t, x, y, lenthOfSide, colorP="black",
                      colorF="white"):
    # Drawing begins at (x, y) and moves in a north-east direction.
    t.pencolor(colorP)
    t.fillcolor(colorF)
    t.up()
    t.goto(x, y)
    t.setheading(0)
    t.left(36)
    t.down()
    t.begin_fill()
    for i in range(6):
        t.forward(lenthOfSide)
        t.left(144)   # 144 = 180 - 36
    t.end_fill()
    
def drawFilledRectangle(t, x, y, w, h, colorP="black", colorF="black"):
    ## Draw a filled rectangle with bottom-left corner (x, y),
    ## width w, height h, pen color colorP, and fill color colorF.
    t.pencolor(colorP)
    t.fillcolor(colorF)
    t.up()
    t.goto(x, y)          # start at bottom-left corner of rectangle
    t.down()
    t.begin_fill()
    t.goto(x + w, y)      # draw line to bottom-right corner
    t.goto(x + w, y + h)  # draw line to top-right corner
    t.goto(x, y + h)      # draw line to top-left corner
    t.goto(x, y)          # draw line to bottom-left corner
    t.end_fill()
    
main()        
