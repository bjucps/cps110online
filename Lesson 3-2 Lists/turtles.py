from turtle import Turtle, Screen

win = Screen()

turtles = []

for i in range(18):
    t = Turtle()
    t.speed(0)
    t.right(i * 20)
    turtles.append(t)

for i in range(4):

    for t in turtles:
        t.forward(100)
        t.right(45)    

win.exitonclick()