from turtle import *

speed(20)
penup()
goto(-140,140)

for line in range(15):
 write(line, align="center")
 forward(10)
 pendown()
 forward(200)
 penup()
 backward(210)
 right(90)
 forward(20)
 left(90)
 



input()