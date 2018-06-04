import turtle

def main():
    t = turtle.Turtle()
    t.speed(10)
    t.hideturtle()
    t.pencolor("blue")
    for i in range(1, 25):
        t.forward(5 * i)
        t.left(90)

main()        

