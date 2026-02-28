import turtle

t = turtle.Turtle()  # initialize turtle
t.speed(3)  # set turtle speed

t.forward(100)  # moves turtle forward
t.left(90)  # turns turtle left x degrees
t.forward(100)

t.right(90)  # turns turtle right x degrees
t.forward(50)

# Pen control
t.penup()  # lifts your pen up: do not draw while moving
t.forward(50)
t.left(90)
t.forward(50)
t.pendown()  # sets your pen down: draw while moving 
t.forward(50)

turtle.done()