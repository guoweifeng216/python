import turtle

values = [75.3, 17.2, 7]

def main():
    t = turtle.Turtle()
    t.speed(10)
    t.hideturtle()
    for i in range(3):
        height = 3 * values[i]
        drawFilledRectangle(t, (-250 + 150 * i), 0, 150, height, "black", "light blue")
    insertText(t )

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

def insertText(t):
    t.up()
    for i in range(3):
        labels1 = ["Public (not", "", ""]
        labels2 = ["charter or magnet)", "Private", "Other"]
        t.pencolor("blue")
        t.goto(-175 + (150 * i), 3 * values[i])
        t.write(str(values[i]) + '%', align="center",font=("Ariel", 10, "normal"))
        t.goto(-175 + 150 * i, 18)
        t.write(labels1[i], align="center",font=("Ariel", 10, "normal"))
        t.goto(-175 + (150 * i), 1)
        t.write(labels2[i], align="center", font=("Ariel", 10, "normal"))
    t.goto(-250, -25)
    t.write("Type of High School Attended by Fall 2013 College Freshmen",
            font=("Ariel", 10, "normal"))
            
main()    
        



