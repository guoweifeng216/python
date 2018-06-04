import turtle

def main():
    ## Draw nested set of five squares.
    t = turtle.Turtle()
    t.hideturtle()
    for i in range(1, 6):
        drawRectangle(t, -10 * i, -10 * i, 20 * i, 20 * i, "blue") 

def drawRectangle(t, x, y, w, h, colorP="black"):
    ## Draw a rectangle with bottom-left corner (x, y),
    ## width w, height h, and pencolor colorP.
    t.pencolor(colorP)
    t.up()
    t.goto(x, y)          # start at bottom-left corner of rectangle
    t.down()
    t.goto(x + w, y)      # draw line to bottom-right corner
    t.goto(x + w, y + h)  # draw line to top-right corner
    t.goto(x, y + h)      # draw line to top-left corner
    t.goto(x, y)          # draw line to bottom-left corner

main()
