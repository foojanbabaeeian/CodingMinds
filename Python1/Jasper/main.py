import turtle

turtle.title("Jasper")
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

# Draw a square
print("1. Square")
print("2. Circle")
print("3. Triangle")
print("4. Star")
print("5. Squid")

shape = input("what do you want to draw? ") 
if shape == "1":
    turtle.color("white")
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
if shape == "2":
    turtle.color("blue")
    turtle.circle(50)
if shape == "3":
    turtle.color("red")
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
if shape == "4":
    turtle.color("yellow")
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)

if shape == "5":
    turtle.color("purple")
    turtle.setheading(90)
    turtle.circle(38, 180)
    turtle.right(40)
    turtle.forward(50)
    turtle.circle(10, 180)
    turtle.forward(50)
    turtle.right(150)
    turtle.forward(50)
    turtle.circle(10, 180)
    turtle.forward(50)
    turtle.right(150)
    turtle.forward(50)
    turtle.circle(10, 180)
    turtle.forward(50)
    turtle.right(150)
    turtle.forward(50)
    turtle.circle(10, 180)
    turtle.forward(50)










turtle.mainloop()


