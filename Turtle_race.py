#turle race





from turtle import *
from random import randint
speed(20)
penup()
goto(-140,140)



for step in range(16):
    write(step)
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)



a = Turtle()
a.color('red')
a.shape('turtle')
a.penup()
a.goto(-160,100)
a.penup()


b = Turtle()
b.color('blue')
b.shape('turtle')
b.penup()
b.goto(-160,75)
b.penup()




c = Turtle()
c.color('pink')
c.shape('turtle')
c.penup()
c.goto(-160,50)
c.penup()



d = Turtle()
d.color('green')
d.shape('turtle')
d.penup()
d.goto(-160,25)
d.penup()



e = Turtle()
e.color('black')
e.shape('turtle')
e.penup()
e.goto(-160,0)
e.penup()


for tur in range(100):
    a.forward(randint(1,5))
     
   
    b.forward(randint(1,5))
       
      
    c.forward(randint(1,5))
    
    
    d.forward(randint(1,5))
    
    
    e.forward(randint(1,5))
    



