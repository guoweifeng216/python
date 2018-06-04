import turtle

def main():
    ## Draw a partial moon.
    t = turtle.Turtle()
    t.hideturtle()
    drawDot(t, 0, 0, 200, "orange")    # Draw moon.
    drawDot(t, -100, 0, 200, "white")  # Take bite out of moon.
        
def drawDot(t, x, y, diameter, colorP):
    ## Draw dot with center (x, y) having color colorP.
    t.up()
    t.goto(x, y)
    t.dot(diameter, colorP)    
    
main()        
