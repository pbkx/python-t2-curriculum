import turtle

t = turtle.Turtle()
t.speed(5)

# Draw a square:
for i in range(4):  # repeat once per side
    t.forward(100)
    t.left(90)

t.penup()
t.goto(-150, 0)  # goto (x, y) on our screen
t.pendown()

# Draw a triangle:
for i in range(3):  # repeat once per side
    t.forward(100)
    t.left(120)  # to get the degrees you want to turn divide 360 degrees by the number of sides.

t.penup()
t.goto(-250, 0)
t.pendown()
t.circle(50)  # draw a circle with radius x

t.penup()
t.goto(0, 200)
t.pendown()

# Drawing a simple house:
for i in range(4):
    t.forward(80)
    t.left(90)

t.left(90)
t.forward(80)
t.right(90)

for i in range(3):
    t.forward(80)
    t.left(120)

turtle.done()