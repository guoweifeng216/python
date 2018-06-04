import turtle

def main():
    ## Draw a blue square containing the underlined word PYTHON.
    t = turtle.Turtle()
    t.hideturtle()
    drawFilledRectangel(t, 0, 0, 200, 200, "blue", "blue")    # Square
    drawFilledRectangel(t, 15, 75, 165, 5, "white", "white")  # Underline
    t.up()
    t.goto(100, 80)
    t.pencolor("white")
    t.write("PYTHON", align="center", font=("Arial", 25, "bold"))

def drawFilledRectangel(t, x, y, w, h, colorP="black", colorF="white"):
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
    
main()        
