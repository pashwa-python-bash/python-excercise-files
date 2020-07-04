import turtle
star = turtle.Turtle()
star.speed(10)
star.color("#05ffd1", "#fffafb")
star.begin_fill()
for i in range(30):
    star.forward(200)
    star.left(170)
    star.forward(200)
star.end_fill()
turtle.done()
