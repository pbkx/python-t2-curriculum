import turtle

t = turtle.Turtle()
t.speed(6)

t.color("blue")  # Change color of turtle object, takes string for color
t.forward(100)

t.color("red")
t.pensize(4)  # Change pensize of turtle object, takes integer
t.forward(100)

# Filling shapes:
t.penup()
t.goto(-150, 0)
t.pendown()

t.color("green")
# Call when you want whatever shape you are about to draw to be filled:
t.begin_fill()
for i in range(4):
  t.forward(100)
  t.left(90)
# Call when you finish drawing whatever shape you want to be filled: 
t.end_fill()

turtle.done()
