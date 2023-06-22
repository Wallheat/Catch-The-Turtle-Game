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

# kaplumbağa.onclick(turtle.goto)

skor.hideturtle()
skor.penup()
skor.color("red")
skor.goto(0 ,250) # skor tablosunun konumunu belirtir.

# score = score + kaplumbağa.onclick(turtle.goto)

skor.write(f"Score: {score}", font = ("Verdana", 50, "normal"), align="center")
print("Başlangıç skor.", score)

süre = turtle.Turtle()
zaman = turtle.Turtle()

# while times > 0:

#     for i in range(55):

#         time.sleep(1/3)
#         kaplumbağa.hideturtle()
#         kaplumbağa.goto(randint(-500,500),randint(-400,400))
#         kaplumbağa.speed(3)

#         kaplumbağa.showturtle()
#         time.sleep(1/50)
        
#         times -= 1

class Countdown():
    
    def __init__(self):
        # self.süre = turtle.Turtle()
        self.süre = süre  
        self.skor = skor
        times = 30

        while times + 1 > 0:
            süre.hideturtle()
            süre.penup()
            süre.color("blue")
            süre.goto(0, 180) # süre tablosunun konumunu belirtir.
            # süre.write(f"Time: {times}", font = ("Verdana", 40, "bold"), align = "center")
            süre.write(f"Time: ", font = ("Verdana", 40, "bold"), align = "center")

            zaman.hideturtle()
            zaman.penup()
            zaman.color("blue")
            zaman.goto(130, 180)
            zaman.write(f"{times}", font = ("Verdana", 40, "bold"), align = "center")
            times -= 1
            time.sleep(1)
            zaman.clear()

            if times == 0:
                break
            else:
                time.sleep(1/4)
                kaplumbağa.hideturtle()
                kaplumbağa.goto(randint(-500,500),randint(-400,400))
                kaplumbağa.speed(1)
                kaplumbağa.showturtle()
                time.sleep(1/2)
                times -= 1

    # def turtle_escape(self):
    # def __init__(self):

    #     for i in range(times):

    #         time.sleep(1/3)
    #         kaplumbağa.hideturtle()
    #         kaplumbağa.goto(randint(-500,500),randint(-400,400))
    #         kaplumbağa.speed(3)

    #         kaplumbağa.showturtle()
    #         time.sleep(1/50)

Countdown()
# escape_turtle = Countdown()
# escape_turtle.turtle_escape()



süre.clear()
süre.goto(0, 180)
süre.write(f"Time is Over!", font = ("Verdana", 40, "bold"), align = "center")

# turtle.bgpic("car.gif")

print("Skor", score)
turtle.mainloop()

# turtle.done()