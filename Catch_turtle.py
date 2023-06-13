# Catch The Turtle

import turtle
import time

board = turtle.Screen()
board.title("Catch The Turtle")
board.setup()
skor = turtle.Turtle()
kaplumbağa = turtle.Turtle()

kaplumbağa.penup()
kaplumbağa.shape("turtle")
kaplumbağa.shapesize(3)

score = 0
times = 3

kaplumbağa.onclick(turtle.goto)

skor.hideturtle()
skor.penup()
skor.color("red")
skor.goto(0 ,250)

# score = score + kaplumbağa.onclick(turtle.goto)

skor.write(f"Score: {score}", font = ("Verdana", 50, "normal"), align="center")
print(score)

süre = turtle.Turtle()

while times + 1 > 0:
    time.sleep(1)
    print(times)
    süre.hideturtle()
    süre.penup()
    süre.color("blue")
    süre.goto(0, 180)
    süre.clear()
    süre.write(f"Time: {times}", font = ("Verdana", 40, "bold"), align = "center")
    times -= 1

süre.clear()

süre.goto(0, 180)
süre.write(f"Time is Over!", font = ("Verdana", 40, "bold"), align = "center")

# turtle.bgpic("car.gif")

print(score)
turtle.mainloop()

# turtle.done()