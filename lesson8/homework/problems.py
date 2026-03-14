# Problem 1
# Use turtle to draw a filled square inside a larger square.



# Problem 2
# Use turtle to draw a flower with 6 petals.
# Each petal can be made using a small circle arc.



# Problem 3
# Use turtle to draw a rainbow:
# Draw 5 semicircles with different colors, each one bigger than the last.

import turtle
t = turtle.Turtle()
t.penup(0, -200)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
radius = 50

for c in colors:
    t.pendown()
    t.circle(radius, 180)
    t.penup()
    t.goto(0, -200 + (radius - 50))
    radius += 20

turtle.done()

# Problem 4
# Use turtle to draw a grid of 3x3 small squares.



# Problem 5
# Use turtle to make a simple "logo" using at least 3 different colors and 2 shapes.
