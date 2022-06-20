from turtle import Turtle
from random import randint

#create object
leo = Turtle('turtle')
leo.color('blue')
leo.penup()
leo.goto(-160,100)
leo.pendown()

Dona = Turtle('turtle')
Dona.color('purple')
Dona.penup()
Dona.goto(-160,70)
Dona.pendown()

raph = Turtle('turtle')
raph.color('red')
raph.penup()
raph.goto(-160,40)
raph.pendown()

mike = Turtle('turtle')
mike.color('orange')
mike.penup()
mike.goto(-160,10)
mike.pendown()

for move in range(100):
    leo.forward(randint(1,5))
    Dona.forward(randint(1,5))
    raph.forward(randint(1,5))
    mike.forward(randint(1,5))