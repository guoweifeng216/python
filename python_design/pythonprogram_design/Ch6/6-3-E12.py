import turtle

def main():
    t = turtle.Turtle()
    t.hideturtle()
    drawDot(t, 0, 0, 300, "blue")
    drawDot(t, 0, 0, 200, "white")  
    drawDot(t, 0, 0, 100, "blue")
    
def drawDot(t, x, y, diameter, colorP):
    ## Draw dot with center (x, y) having color colorP.
    t.up()
    t.goto(x, y)
    t.dot(diameter, colorP)    
    
main()        
