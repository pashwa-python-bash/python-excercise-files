import turtle
import math
pashwa = turtle.Turtle()
pashwa.color("#5257A5", "#29A642")
pashwa.speed(10)
pashwa.begin_fill()
for i in range(2000):
    pashwa.forward(math.sqrt(i))
    pashwa.left(i%180)
pashwa.end_fill()


turtle.done()

