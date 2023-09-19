import turtle as trtl
import random
wn = trtl.Screen()

trtl.screensize(bg = "#127321")
c = trtl.Turtle("turtle")

c.speed(100)
c.pensize(5)
c.fillcolor("#951010")
c.begin_fill()
#background
c.penup()
c.goto(-400, -200)
c.pendown()
for i in range (2):
 c.forward(800)
 c.left(90)
 c.forward(400)
 c.left(90)
 
c.end_fill()


#window
c.penup()
c.goto(-370, -60)
c.pendown()
c.pensize(3)
c.fillcolor("#ADF4F7")
c.begin_fill()
for i in range (2):
 c.forward(250)
 c.left(90)
 c.forward(150)
 c.left(90)
c.end_fill()
#window 2
c.penup()
c.goto(120, -60)
c.pendown()
c.pensize(3)
c.fillcolor("#ADF4F7")
c.begin_fill()
for i in range (2):
 c.forward(250)
 c.left(90)
 c.forward(150)
 c.left(90)
c.end_fill()


#door
c.pensize(5)
c.penup()
c.goto(-80, -200)
c.pendown()
c.left(90)
c.fillcolor("#705A3D")
c.begin_fill()
for i in range(2):
 c.forward(300)
 c.right(90)
 c.forward(160)
 c.right(90)
c.end_fill()
c.penup()
#handle
c.penup()
c.goto(-70, -50)
c.pendown()
for i in range(2):
 c.forward(15)
 c.right(90)
 c.forward(10)
 c.right(90)
#door window 1
c.penup()
c.goto(-60, -20)
c.pendown()
c.fillcolor("#ADF4F7")
c.begin_fill()
for i in range(2):
 c.forward(100)
 c.right(90)
 c.forward(120)
 c.right(90)
c.end_fill()
#door sign
c.penup()
c.goto(0, 30)
c.pendown()
c.color("red")
c.write("OPEN", align='center', font=('arial', 15, 'bold'))
c.penup()
c.goto(-30, 60)
c.pendown()
c.right(90)
c.pencolor("blue")
for i in range(2):
 c.forward(60)
 c.right(90)
 c.forward(30)
 c.right(90)
c.left(90)
c.pencolor("black")


#door window 2 
c.penup()
c.goto(-60, -180)
c.pendown()
c.fillcolor("#ADF4F7")
c.begin_fill()
for i in range(2):
 c.forward(100)
 c.right(90)
 c.forward(120)
 c.right(90)
c.end_fill()
#door overhang
c.penup()
c.goto(80, 100)
c.pendown()
c.fillcolor("#CC0303")
c.begin_fill()
c.circle(80, 180)
c.end_fill()
c.goto(80, 100)
c.penup()


d=45
x= -60
y= 100
c.right(180)
c.pensize(7)
c.pencolor("white")
for i in range(3):
 c.penup()
 c.goto(x,y)
 c.pendown()
 c.forward(d)
 d=d+15
 x= x+20


for i in range(4):
 c.penup()
 c.goto(x,y)
 c.pendown()
 c.forward(d)
 d=d-15
 x= x+20


#roof
c.penup()
c.goto(-400, 200)
c.pendown()
c.pencolor("black")
c.fillcolor("#453609")
c.begin_fill()
c.right(45)
c.forward(200)
c.right(45)
c.forward(520)
c.right(45)
c.forward(200)
c.end_fill()
c.penup()
c.goto(-400, 200)
c.pendown()


c.fillcolor("red")
x=-400
y=200
c.right(45)
for cover in range (8):
 c.begin_fill()
 c.penup()
 c.goto(x,y)
 c.pendown()
 c.circle(50, 180)
 c.end_fill()
 x= x+100
 c.right(180)
 rem = cover % 2
 if (rem == 0):
  c.fillcolor("white")
 if (rem == 1):
  c.fillcolor("red")


#sign 
c.penup()
c.goto(0, 250)
c.pendown()
c.write("Turtle's Pizzeria", align='center', font=('arial', 50, 'bold'))


#path 
c.fillcolor("#7B776C")
c.pensize(5)
c.penup()
c.goto(-80, -200)
c.pendown()
c.begin_fill()
c.right(20)
c.forward(250)
c.left(110)
c.forward(330)
c.left(110)
c.forward(250)
c.end_fill()


#Bike Rack 
c.right(20)
c.penup()
c.goto(-370, -200)
c.pendown()
c.pencolor("black")
c.pensize(5)
c.fillcolor("#6D5A26")
c.begin_fill()
for i in range(2):
  c.forward(30)
  c.right(90)
  c.forward(250)
  c.right(90)
c.end_fill()
c.penup()
c.goto(-330, -145)
c.pendown()
x=-330
y=-145
for i in range(7):
  c.penup()
  c.goto(x,y)
  c.pendown()
  c.circle(30)
  x= x+40


#bush 
c.penup()
c.goto(120, -200)
c.pendown()
c.pencolor("black")
c.pensize(5)
c.fillcolor("#6D5A26")
c.begin_fill()
for i in range(2):
  c.forward(30)
  c.right(90)
  c.forward(250)
  c.right(90)
c.end_fill()
c.penup()
c.goto(150, -145)
c.pendown()
c.pencolor("#31BE2F")
c.fillcolor("#31BE2F")
x=150
y=-145
for i in range(9):
  c.begin_fill()
  c.penup()
  c.goto(x,y)
  c.pendown()
  c.circle(30)
  c.end_fill()
  x= x+30
c.pencolor("black")
c.right(90)


play = input(print("Would you like to come in? y/n"))
if (play == "y"):
  x = 90
  y = 205
  c.clear()
  c.goto(x, y)
  c.pendown()
  #make sign body
  c.fillcolor("#C4A484")
  c.begin_fill()
  for i in range (2):
    c.forward(400)
    c.left(90)
    c.forward(200)
    c.left(90)
  c.end_fill()
  c.penup()
  #write text on sign
  c.goto(x + 200, y + 165)
  c.write("Create your own pizza!", align='center', font=('Comic Sans', 25, 'bold'))
  c.goto(x + 20, y + 140)
  c.write("Today's choice of toppings:", font=('Comic Sans', 15, 'normal'))
  c.goto(x + 20, y + 120)
  c.write("Mushrooms, Pepperoni, Pineapple,", font=('Comic Sans', 10, 'normal'))
  c.goto(x + 20, y + 105)
  c.write("Green Peppers, Olives, Bacon", font=('Comic Sans', 10, 'normal'))
  c.goto(x + 15, y + 75)
  c.write("Comes with house tomato sauce and fresh mozarella", font=('Comic Sans', 12, 'normal'))
  c.goto(x + 200, y + 32)
  c.write("All pizzas are made fresh to order!", align='center', font=('Comic Sans', 17, 'bold'))
  #table
  c.pensize(5)
  c.penup()
  c.goto(-400,-200)
  c.pendown()
  c.fillcolor("#AD7868")
  c.begin_fill()
  for i in range (2):
    c.forward(800)
    c.left(90)
    c.forward(400)
    c.left(90)
  c.end_fill()
  #sauce container
  c.penup()
  c.goto(-350,-150)
  c.pendown()
  c.fillcolor("#B0320C")
  c.begin_fill()
  for i in range(2):
    c.forward(225)
    c.left(90)
    c.forward(150)
    c.left(90)
  c.end_fill()


  #cheeses
  c.penup()
  c.goto(-315,50)
  c.pendown()
  c.fillcolor("#FFEDB2")
  c.begin_fill()
  for i in range(2):
    c.circle(65)
    c.penup()
    c.forward(150)
    c.pendown()
    c.end_fill()
    c.fillcolor("#FFB733")
    c.begin_fill()
  c.end_fill()


  #pizza pan
  c.penup()
  c.goto(-75,-150)
  c.pendown()
  c.fillcolor("#A49E92")
  c.begin_fill()
  for i in range(4):
    c.forward(300)
    c.left(90)
  c.end_fill()


  #toppings
  y = 100
  x=280
  c.penup()
  c.goto(x,y)
  c.pendown()
  colors = ["#EA0000", "#A49E92","#000000", "#FFD232", "#1F8915", "#7E1E0F"]
  for i in range(3):
    new_color = colors.pop()
    c.fillcolor(new_color)
    c.begin_fill()
    c.circle(25)
    c.end_fill()
    y = y-125
    c.penup()
    c.goto(x,y)
    c.pendown()
  x=355
  y= 100


  c.penup()
  c.goto(x,y)
  c.pendown()
  for i in range(3):
    new_color = colors.pop()
    c.fillcolor(new_color)
    c.begin_fill()
    c.circle(25)
    c.end_fill()
    y = y-125
    c.penup()
    c.goto(x,y)
    c.pendown()


  #dough
  c.penup()
  c.goto(75,-135)
  c.pendown()
  c.fillcolor("#F0DAAA")
  c.begin_fill()
  c.circle(135)
  c.end_fill()

  c.penup()
  c.goto(75, 0)
  c.pendown()

  def draw_olive():
    c.pendown()
    c.pensize(6)
    c.pencolor("black")
    c.circle(7)
    c.penup()

  def draw_pepper():
    c.pendown()
    c.pensize(6)
    c.pencolor("green")
    c.circle(10, 130)
    c.right(130)
    c.penup()

  def draw_pineapple():
    c.pendown()
    c.pensize(9)
    c.pencolor("#FFD232")
    c.circle(9, 360, 3)
    c.penup()

  def draw_mushroom():
    c.pendown()
    c.fillcolor("#964B00")
    c.begin_fill()
    c.pensize(2.5)
    c.pencolor("#A49E92")
    c.circle(10, 180)
    c.left(90)
    c.forward(20)
    c.left(90)
    c.end_fill()
    c.penup()

  def draw_pepperoni():
    c.pendown()
    c.begin_fill()
    c.fillcolor("#EA0000")
    c.pencolor("#B0320C")
    c.circle(10)
    c.end_fill()
    c.penup()

  def draw_bacon():
    c.pendown()
    c.pencolor("#7E1E0F")
    c.pensize(10)
    c.forward(10)
    c.penup()

  x = 75
  y = 0
  x = random.randint(0,22)
  angle = 0
  c.penup()

  want_sauce = input("Do you want sauce on your pizza? y/n")
  if(want_sauce == "y"):
     c.penup()
     c.turtlesize(3)
     c.goto(-250,-75)
     c.pendown()
     c.speed(1)
     c.right(360)
     c.penup()
     c.pensize(5)
     c.speed(100)
     c.turtlesize(1)
     c.goto(75,-125)
     c.pendown()
     c.fillcolor("#B0320C")
     c.begin_fill()
     c.circle(125)
     c.end_fill()
      
  what_cheese = input("Do you want mozzarella cheese, cheddar cheese, or none on your pizza?")
  if(what_cheese=="mozzarella cheese"):
     c.penup()
     c.turtlesize(3)
     c.goto(-310,100)
     c.pendown()
     c.speed(1)
     c.right(360)
     c.penup()
     c.pensize(5)
     c.speed(100)
     c.turtlesize(1)
     c.goto(75,-110)
     c.pendown()
     c.fillcolor("#FFEDB2")
     c.begin_fill()
     c.circle(110)
     c.end_fill()


  elif(what_cheese=="cheddar cheese"):
     c.penup()
     c.turtlesize(3)
     c.goto(-175,100)
     c.pendown()
     c.speed(1)
     c.right(360)
     c.penup()
     c.pensize(5)
     c.speed(100)
     c.turtlesize(1)
     c.goto(75,-110)
     c.pendown()
     c.fillcolor("#FFB733")
     c.begin_fill()
     c.circle(110)
     c.end_fill()


  c.turtlesize(2)
  c.penup()
  want_bacon = input("Do you want bacon on your pizza? y/n")
  if(want_bacon=="y"):
    c.goto(280, 100)
    c.right(360)
    for i in range(15):
      c.goto(x, y)
      x = random.randint(-15,165)
      y = random.randint(-90, 90)
      angle = random.randint(0, 360)
      c.speed(30)
      c.right(angle)
      draw_bacon()
      c.speed(3)

  want_peppers = input("Do you want peppers on your pizza? y/n")
  if(want_peppers=="y"):
    c.goto(280, -25)
    c.right(360)
    for i in range(15):
      c.goto(x, y)
      x = random.randint(-15,165)
      y = random.randint(-90, 90)
      angle = random.randint(0, 360)
      c.speed(30)
      c.right(angle)
      draw_pepper()
      c.speed(3)

  want_pineapple = input("Do you want pineapple on your pizza? y/n")
  if(want_pineapple=="y"):
    c.goto(280, -150)
    c.right(360)
    for i in range(15):
      c.goto(x, y)
      x = random.randint(-15,165)
      y = random.randint(-90, 90)
      angle = random.randint(0, 360)
      c.speed(30)
      c.right(angle)
      draw_pineapple()
      c.speed(3)

  want_olives = input("Do you want olives on your pizza? y/n")
  if(want_olives=="y"):
    c.goto(355, 100)
    c.right(360)
    for i in range(15):
      c.goto(x, y)
      x = random.randint(-15,165)
      y = random.randint(-90, 90)
      angle = random.randint(0, 360)
      c.speed(30)
      c.right(angle)
      draw_olive()
      c.speed(3)

  want_mushrooms = input("Do you want mushrooms on your pizza? y/n")
  if(want_mushrooms=="y"):
    c.goto(355, -25)
    c.right(360)
    for i in range(15):
      c.goto(x, y)
      x = random.randint(-15,165)
      y = random.randint(-90, 90)
      angle = random.randint(0, 360)
      c.speed(30)
      c.right(angle)
      draw_mushroom()
      c.speed(3)

  want_pepperoni = input("Do you want pepperoni on your pizza? y/n")
  if(want_pepperoni=="y"):
    c.goto(355, -150)
    c.right(360)
    for i in range(15):
      c.goto(x, y)
      x = random.randint(-15,165)
      y = random.randint(-90, 90)
      angle = random.randint(0, 360)
      c.speed(30)
      c.right(angle)
      draw_pepperoni()
      c.speed(3)



  end = input("All done? y/n")
  if(end=="y"):
    c.clear()
    wn = trtl.Screen()
    pizza_box = trtl.Turtle()
    pizza_box.penup()
    pizza_box.goto(0, 0)
    pizza_box.pendown()
    wn.addshape("pizza_box.gif")
    pizza_box.shape("pizza_box.gif")
    c.penup()
    c.goto(0, 250)
    c.write("Enjoy your pizza!", align='center', font=('arial', 50, 'bold'))

    

wn.mainloop()