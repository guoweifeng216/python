import turtle

def main():
    t = turtle.Turtle()
    t.hideturtle()
    t.up()
    colors = ["red", "blue", "green", "purple",
              "orange", "brown", "black", "yellow"]
    word = "Python"
    for i in range(len(word)):
        t.color(colors[i])
        t.goto(20 * i, 0)
        t.write(word[i], font=("Courier New", 18, "bold"))
    
main()        
