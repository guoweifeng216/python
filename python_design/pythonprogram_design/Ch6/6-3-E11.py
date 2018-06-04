import turtle

def main():
    t = turtle.Turtle()
    t.speed(10)
    t.hideturtle()
    colors = ["black", "white", "dark blue", "red", "yellow"]
    diameter = 300
    for color in colors:
        t.pencolor(color)
        t.dot(diameter)
        diameter -= 60

main()        
