import turtle

def main():
    t = turtle.Turtle()
    t.hideturtle()
    t.up()
    drawDot(t, 0,0, 200, "red")
    drawDot(t, -120,120, 200, "white")
   
def drawDot(t, x, y, diameter, colorP):
    # draw dot with center (x, y) having color colorP
    t.up()
    t.goto(x, y)
    t.dot(diameter, colorP)    
    
main()        
