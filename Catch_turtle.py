# Catch The Turtle

import turtle
import time
from random import randint

board = turtle.Screen()
board.title("Catch The Turtle")
board.setup(1200,800)
skor = turtle.Turtle()

kaplumbağa = turtle.Turtle()
kaplumbağa.penup()
kaplumbağa.shape("turtle")
kaplumbağa.shapesize(3)

score = 0
times = 3

skor.hideturtle()
skor.penup()
skor.color("red")
skor.goto(0 ,250) # skor tablosunun konumunu belirtir.

skor.write(f"Score: {score}", font = ("Verdana", 50, "normal"), align="center")
print("Başlangıç skor.", score)

süre = turtle.Turtle()
zaman = turtle.Turtle()

class Countdown():
    
    def __init__(self):
        self.süre = süre  
        self.skor = skor
        times = 30

        while times + 1 > 0:
            süre.hideturtle()
            süre.penup()
            süre.color("blue")
            süre.goto(-30, 180) # süre tablosunun konumunu belirtir.
            süre.write(f"Time: ", font = ("Verdana", 40, "bold"), align = "center")

            zaman.hideturtle()
            zaman.penup()
            zaman.color("blue")
            zaman.goto(90, 180)
            zaman.write(f"{times}", font = ("Verdana", 40, "bold"), align = "center")
            print(f"Süre: {times}")
            times -= 1
            time.sleep(1)
            zaman.clear()

            if times == 0:
                break
            else:
                kaplumbağa.hideturtle()
                kaplumbağa.goto(randint(-500,500),randint(-400,400))
                kaplumbağa.speed(0)
                kaplumbağa.speed(0.5)
                kaplumbağa.showturtle()

Countdown()

süre.clear()
süre.goto(0, 180)
süre.write(f"Time is Over!", font = ("Verdana", 40, "bold"), align = "center")

# turtle.bgpic("car.gif")

print("Skor", score)
turtle.mainloop()