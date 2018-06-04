import turtle

MALE_ENROLLMENTS = [1375, 2047, 2233, 2559, 3265]
FEMALE_ENROLLMENTS = [945, 2479, 3007, 3390, 4415]

def main():
    ## Draw line chart to two-year college enrollments.
    t = turtle.Turtle()
    t.hideturtle()
    drawLine(t, 0, 0, 200, 0)    # Draw x-axis.
    drawLine(t, 0, 0, 0, 200)    # Draw y-axis.
    ## Draw graphs.
    for i in range(4):
        drawLineWithDots(t, 20 + (40 * i), MALE_ENROLLMENTS[i]/ 25,
                         60 + (40 * i), MALE_ENROLLMENTS[i+1]/25, "black")
    for i in range(4):
        drawLineWithDots(t, 20 + (40 * i), FEMALE_ENROLLMENTS[i]/ 25,
                         60 + (40 * i), FEMALE_ENROLLMENTS[i+1]/25, "black")
    drawTickMarks(t)
    insertText(t)

def drawLine(t, x1, y1, x2, y2, colorP="black"):
    ## Draw line segment from (x1, y1) to (x2, y2) having color colorP.
    t.up()
    t.goto(x1, y1)
    t.down()
    t.color(colorP)
    t.goto(x2, y2)

def drawLineWithDots(t, x1, y1, x2, y2, colorP="black"):
    ## Draw line segment from (x1, y1) to (x2, y2) having color 
    ## colorP and insert dots at both ends of the line segment. 
    t.pencolor(colorP)
    t.up()
    t.goto(x1, y1)
    t.dot(5)
    t.down()
    t.goto(x2, y2)
    t.dot(5)

def drawTickMarks(t):
    for i in range(5):
        drawLine(t, 20 + (40 * i), 0, 20 + 40 * i , 10)
    drawLine(t, 0, max(FEMALE_ENROLLMENTS)/25, 10,
             max(FEMALE_ENROLLMENTS)/25)
    drawLine(t, 0, min(FEMALE_ENROLLMENTS)/25, 10,
             min(FEMALE_ENROLLMENTS)/25)
    
def insertText(t):
    t.up()
    t.pencolor("black")
    t.goto(110, 150)
    t.write("Females")
    t.goto(120, 80)
    t.write("Males")
    # Display greatest enrollment value.
    t.color("blue")
    t.goto(-30, (max(FEMALE_ENROLLMENTS)/25)-10)
    t.write(max(FEMALE_ENROLLMENTS))
    # Display least enrollment value.
    t.goto(-22, (min(FEMALE_ENROLLMENTS)/25) - 10)
    t.write(min(FEMALE_ENROLLMENTS))
    # Display labels for tick marks on x-axis.
    t.goto(0, -20)
    x = 20
    for i in range(1970, 2011, 10):
        t.goto(x, -20)
        t.write(str(i), align="center")
        x += 40
    # Display title of line chart.
    t.goto(0, -40)
    t.write("Two-Year College Enrollments")
    t.goto(0, -55)
    t.write("(in thousands)")
    
main()    
        



