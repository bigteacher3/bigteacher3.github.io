import turtle
import random
import time

s = turtle.Screen()
s.tracer(0, 200)
s.title("Приклад анімації")

p = turtle.Turtle()

p.up()
p.ht()
# p.speed(10)

def poligon(n) :
    bg = (random.random(), random.random(), random.random())
    fg = (random.random(), random.random(), random.random())
    p.color(fg, bg)
    p.begin_fill()
    for x in range(n) :
        p.down()
        p.fd(30)
        p.lt(360 / n)
        p.up()
    p.end_fill()
    pass

name = turtle.textinput("Привітання", "Як тебе звати?")

x = -100
n = 6
m = -1
while x < 100 :
    p.goto(x, 0)
    poligon(n)
    s.update()
    p.clear()
    n += 1 * m
    x += 20
    if n < 4 or n > 6:
        m *= -1
time.sleep(0.5)
s.update()

p.goto(0, 100)
p.color("blue")
p.write(f"{name}, it's all over", 
        font = ("Roboto", 24, "bold"),
       align = "center")
s.tracer(1)
