import turtle

wf = [59, 74, 73, 77]   # well off financially
mp = [60, 43, 44, 51]   # meaningful philosophy

def main():
    t = turtle.Turtle()
    t.hideturtle()
    drawLine(t, 0, 0, 200, 0)    # x-axis
    drawLine(t, 0, 0, 0, 200)    # y-axis
    for i in range(3):
        drawLineWithDots(t, 20 + (50 * i), 2 * wf[i], 70 + 50 * i,
                         2 * wf[i+1], "black")
    for i in range(3):
        drawLineWithDots(t, 20 + (50 * i), 2 * mp[i], 70 + 50 * i,
                         2 * mp[i+1], "black")
    drawTickMarks(t)
    insertText(t)

def drawLine(t, x1, y1, x2, y2, colorP="black"):
    t.up()
    t.goto(x1,y1)
    t.down()
    t.color(colorP)
    t.goto(x2,y2)

def drawLineWithDots(t, x1, y1, x2, y2, colorP="black"):
    t.pencolor(colorP)
    t.up()
    t.goto(x1,y1)
    t.dot(5)
    t.down()
    t.goto(x2,y2)
    t.dot(5)

def drawTickMarks(t):
    for i in range(4):
        drawLine(t, 20 + (50 * i), 0, 20 + 50 * i , 10)
    drawLine(t, 0, 2 * max(wf), 10, 2 * max(wf))
    drawLine(t, 0, 2 * min(mp), 10, 2 * min(mp))
    
def insertText(t):
    t.up()
    t.pencolor("black")
    t.goto(30, 152)
    t.write("Well off financially")
    t.pencolor("black")
    t.goto(30, 65)
    t.write("Meaningful philosophy of life")
    # Display greatest enrollment value.
    t.color("blue")
    t.goto(-15, 2 * max(wf) - 7)
    t.write(max(mp))
    # Display least enrollment value.
    t.goto(-15, 2 * min(mp) - 7)
    t.write(min(mp))
    # Display labels for tick marks on x-axis.
    t.goto(0, -20)
    x = 20
    for i in range(1978, 2009, 10):
        t.goto(x, -20)
        t.write(str(i), align="center")
        x += 50
    t.goto(0, -40)
    t.write("Freshman Life Goals")
    t.goto(0, -55)
    t.write("(% of students committed to goal)")
    
main()    
        



