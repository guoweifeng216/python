import turtle

def main():
    ## Draw a dot inside a square.
    t = turtle.Turtle()
    t.hideturtle()
    drawFilledRectangle(t, 0, 0, 100, 100, "red", "yellow")
    drawDot(t, 50, 50, 100, "blue")

def drawFilledRectangle(t, x, y, w, h, colorP="black", colorF="white"):
    # Draw a filled rectangle with bottom-left corner (x, y),
    # width w, height h, pencolor colorP, and fill color colorF.
    t.pencolor(colorP)
    t.fillcolor(colorF)
    t.up()                # Disable drawing of lines.
    t.goto(x , y)         # bottom-left corner of rectangle
    t.down()              # Enable drawing of lines.
    t.begin_fill()
    t.goto(x + w, y)      # Draw line to bottom-right corner of rectangle.
    t.goto(x + w, y + h)  # Draw line to top-right corner of rectangle.
    t.goto(x, y + h)      # Draw line to top-left corner of rectangle.
    t.goto(x , y)         # Draw line to bottom-left corner of rectangle.
    t.end_fill()

def drawDot(t, x, y, diameter, colorP):
    # draw dot with center (x, y) having color colorP
    t.up()
    t.goto(x, y)
    t.dot(diameter, colorP)    
    
main()        
