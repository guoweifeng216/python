
import turtle

def main():
    ## Draw flag of Japan.
    t = turtle.Turtle()
    t.hideturtle()
    drawSolidRectangle(t, 0, 0, 150, 100, "black", "white")
    t.up()
    t.goto(75,50)
    t.color("red")
    t.dot(62)
    
def drawSolidRectangle(t, x, y, w, h, colorP="black", colorF="black"):
    ## Draw a solid rectangle with bottom-left corner (x, y),
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
        




