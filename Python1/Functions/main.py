import turtle
import random

# Set up screen
screen = turtle.Screen()
screen.title("Color Spinner")
screen.setup(width=600, height=600)
screen.bgcolor("white")

# Spinner pieces
spinner = turtle.Turtle()
spinner.speed(0)
spinner.penup()
spinner.goto(0, 0)
spinner.hideturtle()

# Draw four colored triangles to make spinner
def draw_spinner():
    colors = ["red", "blue", "yellow", "black"]
    angles = [0, 90, 180, 270]
    
    for i in range(4):
        spinner.fillcolor(colors[i])
        spinner.begin_fill()
        spinner.setheading(angles[i])
        spinner.forward(100)
        spinner.left(135)
        spinner.forward(141.4)
        spinner.left(90)
        spinner.forward(141.4)
        spinner.left(135)
        spinner.forward(100)
        spinner.end_fill()

draw_spinner()

# Arrow pointer
arrow = turtle.Turtle()
arrow.color("red")
arrow.pensize(4)
arrow.speed(1)
arrow.hideturtle()

def spin_arrow():
    arrow.clear()
    arrow.penup()
    arrow.goto(0, 0)
    arrow.setheading(0)
    arrow.showturtle()

    color_index = random.randint(0, 3)
    angles = [315, 45, 135, 225]  # red, blue, yellow, black
    arrow.setheading(angles[color_index])
    arrow.pendown()
    arrow.forward(150)

    # Print result
    result = ["red", "blue", "yellow", "black"][color_index]
    print(f"Spinner landed on: {result.upper()}")

# Button to spin
button = turtle.Turtle()
button.hideturtle()
button.penup()
button.goto(-250, -250)
button.shape("square")
button.shapesize(stretch_wid=2, stretch_len=6)
button.fillcolor("lightgreen")
button.showturtle()

# Button label
text_writer = turtle.Turtle()
text_writer.hideturtle()
text_writer.penup()
text_writer.goto(-250, -258)
text_writer.write("Spin Again", align="center", font=("Arial", 12, "bold"))

# Click detection for button
def on_click(x, y):
    if -280 < x < -220 and -270 < y < -230:
        spin_arrow()

screen.onclick(on_click)

turtle.done()
