import turtle
import random
t = turtle.Turtle()
w = turtle.Turtle()
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
w.speed(0)
w.penup()
t.penup()
def randcolor():
    col1 = random.randint(0,255)
    col2 = random.randint(0,255)
    col3 = random.randint(0,255)
    randcol = (col1, col2, col3)
    return randcol
def drawfw1(angle):
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    t.goto(x, y)
    t.pendown()
    for _ in range(random.randint(30,100)):
        t.fd(200)
        t.left(angle)
    t.penup()
    
def drawfw2(angle):
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    
    w.goto(x, y)
    w.pendown()
    for _ in range(random.randint(30,100)):
        w.fd(200)
        w.left(angle)
    w.penup()
    
while True:
  for _ in range(2):
    t.pencolor(randcolor())
    w.pencolor(randcolor())
    angle = random.randint(99,179)
    angle2 = random.randint(99,179)
    drawfw1(angle)
    drawfw2(angle2)
  t.clear()
  w.clear()
  
  