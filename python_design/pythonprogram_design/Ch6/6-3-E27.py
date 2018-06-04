
import turtle

values = [7.6, 5.0, 4.7, 2.8, 2.8]

def main():
    ## Draw bar chart for popular majors.
    t = turtle.Turtle()
    t.speed(10)
    t.hideturtle()
    for i in range(5):
        height = 30 * values[i]
        drawSolidRectangle(t, (-250 + 100 * i), 0, 100, height, "black", "light blue")
    insertText(t)

def drawSolidRectangle(t, x, y, w, h, colorP="black", colorF="black"):
    ## Draw a solid vertical rectangle with bottom-left corner (x, y),
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

def insertText(t):
    t.up()
    labels1 = ["Biology", "Nursing", "Psychology", "Mechanical", "Bus. Admin."]
    labels2 = ["(general)", "", "", "Engineering", "(general)"]
    for i in range(5):
        t.pencolor("blue")
        t.goto(-200 + 100 * i, 30 * values[i])
        t.write(str(values[i]) + '%', align="center",font=("Ariel", 10, "normal"))
        t.goto(-200 + 100 * i, 25)
        t.write(labels1[i], align="center",font=("Ariel", 10, "normal"))
        t.goto(-200 + 100 * i, 10)
        t.write(labels2[i], align="center",font=("Ariel", 10, "normal"))
    t.goto(-250, -25)
    t.write("Most Popular Majors for College Freshmen in Fall 2013",
            font=("Ariel", 10, "normal"))
            
main()    
        



