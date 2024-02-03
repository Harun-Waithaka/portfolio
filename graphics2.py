import turtle
import time

turtle.bgcolor('black')
seven = turtle.Turtle()
seven.pensize(3)
seven.speed(0)
seven.goto(200, 200)

def drawsquare():
    seven.rt(180)
    seven.fd(200)
    seven.rt(360)
    seven.fd(180)

colors = ['white', 'yellow', 'purple', 'orange']

for i in range(23):
    for color in colors:
        seven.color(color)
        drawsquare()
        seven.rt(91)

time.sleep(5)
turtle.exitonclick()