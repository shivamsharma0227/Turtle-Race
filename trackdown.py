from turtle import *

speed(0)
penup()
goto(-140,140)

for line in range(15):
 write(line, align="center")
 right(90)
 penup()
 forward(10)
 pendown()
 forward(150)
 penup()
 backward(160)
 left(90)
 forward(20)