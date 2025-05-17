from turtle import *
from random import *

p = Turtle() # перо
# p.shape("circle")


w = Screen() # вікно
w.tracer(0, 200) # трасування вимкнено, оновлення через 200 мілісекунд
p.speed(10) # найвища швидкість для цього пера
p.down()
p.color(random(), random(), random()) # колір в режимі RGB
p.width(5) # товщина пера

step = 50 # довжина сторони
for k in range(5): # встановлюємо параметри анімації
    p.clear() # очищаємо намальоване цим пером
    for n in range(8) : # малюємо багатокутник (кадр анімації
        p.fd(step)
        p.left(360 / 8)
    p.up()
    w.update() # після малювання кадру (його ще не видно) оновлюємо вікно
    p.color(random(), random(), random())
    p.left(360/5)
    p.down()
p.up()
