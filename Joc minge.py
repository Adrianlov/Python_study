import turtle
wn = turtle.Screen()
wn.bgcolor('green')
wn.title("Bila miscatoare")

minge = turtle.Turtle()
minge.penup()
minge.shape("square")
minge.goto(0, 100)
minge.speed(0.5)
minge.dy = 10

gravity = 0.2

while True:
    minge.dy -= gravity
    minge.sety(minge.ycor() + minge.dy)
    if minge.ycor() < -200:
        minge.dy *= -1








wn.mainloop()














