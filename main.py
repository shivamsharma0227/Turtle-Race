from trackdown import *
from random import randint

#first turtle
mika = Turtle()
mika.color("red")
mika.shape("turtle")
mika.penup()
mika.goto(-175,110)
mika.pendown()
mika.write("mika(1)")


for turn in range(10):
 mika.right(36)

#second turtle
bob = Turtle()
bob.color("purple")
bob.shape("turtle")
bob.penup()
bob.goto(-175,80)
bob.pendown()
bob.write("bob(2)")

for turn in range(10):
 bob.left(36)


#third turtle
zira = Turtle()
zira.color("yellow")
zira.shape("turtle")
zira.penup()
zira.goto(-175,50)
zira.pendown()
zira.write("Zira(3)")

for turn in range(10):
 zira.right(36)

#fourth turtle
cuba = Turtle()
cuba.color("blue")
cuba.shape("turtle")
cuba.penup()
cuba.goto(-175,20)
cuba.pendown()
cuba.write("Cuba(4)")

for turn in range(10):
 cuba.left(36)


for race in range(110):
 mika.forward(randint(1,4))
 bob.forward(randint(1,4))
 zira.forward(randint(1,4))
 cuba.forward(randint(1,4))
