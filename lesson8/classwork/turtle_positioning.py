import turtle

t = turtle.Turtle()
t.speed(2)

t.forward(100)

# Move without drawing
t.penup()
t.goto(-100, 0)
t.pendown()

t.circle(40)

t.penup()
t.goto(0, 100)
t.pendown()

# Stamping the turtle shape:

t.shape("turtle")  # Change turtle pen shape, takes string

# Draw a filled in blue hexagon:
t.begin_fill()
t.color("blue")
for i in range(6):
  t.forward(50)
  t.left(60)
t.end_fill()

# Stamp turtles in each corner of the hexagon:
t.color("green")
t.penup()
for i in range(6):
  t.pendown()
  t.stamp()
  t.penup()
  t.forward(50)
  t.left(60)

t.stamp()  # Stamp the turtle shape at current position
