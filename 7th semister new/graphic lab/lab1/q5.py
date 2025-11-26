import turtle

# Create turtle screen
screen = turtle.Screen()
screen.bgcolor("lightyellow")
screen.title("Drawing Shapes with Turtle")

# Create turtle object
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(5)

# ----------- Draw a Square -----------
pen.color("blue")
for _ in range(4):
    pen.forward(100)
    pen.right(90)

# Move to a new position
pen.penup()
pen.goto(-150, 0)
pen.pendown()

# ----------- Draw a Triangle -----------
pen.color("green")
for _ in range(3):
    pen.forward(100)
    pen.left(120)

# Move again
pen.penup()
pen.goto(150, 0)
pen.pendown()

# ----------- Draw a Circle -----------
pen.color("red")
pen.circle(50)

# Move again
pen.penup()
pen.goto(0, -150)
pen.pendown()

# ----------- Draw a Star -----------
pen.color("purple")
for _ in range(5):
    pen.forward(100)
    pen.right(144)

# Hide turtle
pen.hideturtle()

# Keep window open
turtle.done()
