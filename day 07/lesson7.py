from turtle import *

#drawing a square

speed(100)
width(6.4)
penup()

right(90)
forward(300)

pendown()

right(90)
forward(300)
right(180)
forward(565)
left(90)
forward(400)
left(90)
forward(565)
left(90)
forward(400)

#end of square

#drawing a roof


left(180)
forward(400)
color("red")
right(45)
begin_fill()
forward(200)
right(90)
forward(200)
left(90)
forward(200)
right(90)
forward(200)
end_fill()

#end of roof

#going on door coordinates

penup()
goto(0, -300)
pendown()


color("black")

left(-135)
forward(150)

#drawing a door

color("yellow")

begin_fill()
right(90)
forward(220)
right(90)
forward(240)
right(90)
forward(220)
right(90)
forward(240)
end_fill()

#end of door

#door design

back(60)
color("brown")
begin_fill()
right(90)
forward(150)
right(90)
forward(120)
right(90)
forward(150)
end_fill()

#end of door design

#start of second floor

penup()

back(250)
left(90)
forward(237)
pendown()

color("green")
back(563)
left(90)
forward(145)
right(90)
forward(563)
right(90)
forward(145)

#end of second floor

#strat of queen and king (minecraft type)

#king
penup()
right(90)
forward(200)

right(90)
forward(110)
back(10)

pendown()

#head
width(3)
color("gold")
begin_fill()
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)


back(30)
left(90)

#left hand
forward(7)
left(90)
forward(40)
right(90)
forward(15)
right(90)
forward(40)
left(90)
forward(13)
left(90)
forward(45)
left(90)
forward(10)
left(90)
forward(45)

#right hand
   #going to right hand
right(90)
forward(27)
   #drawing right hand
right(90)
forward(45)
right(90)
forward(9)
right(90)
forward(45)
back(70)
left(90)
forward(5)
right(90)
forward(30)
left(90)
forward(5)
left(90)
forward(30)
right(90)
forward(5)
right(90)
forward(30)
end_fill()

#drwaing eyes

penup()
color("black")
forward(50)
pendown()
forward(10)
penup()
right(90)
forward(15)
right(90)
pendown()
forward(10)

#end of king

#queen

penup()

back(10)

right(180)
forward(10)
left(90)
forward(70)


pendown()

#head
color("cyan")
begin_fill()
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
right(90)
forward(7)
left(90)
forward(40)
right(90)
forward(15)
right(90)
forward(40)
left(90)
forward(13)
left(90)
forward(45)
left(90)
forward(10)
left(90)
forward(45)
end_fill()

#right hand
   #going to right hand
right(90)
forward(27)
   #drawing right hand
begin_fill()
right(90)
forward(45)
right(90)
forward(9)
right(90)
forward(45)
back(70)
left(90)
forward(5)
right(90)
forward(30)
left(90)
forward(5)
left(90)
forward(30)
right(90)
forward(5)
right(90)
forward(30)
end_fill()

#drwaing eyes

penup()
color("black")
forward(50)
pendown()
forward(10)
penup()
right(90)
forward(15)
right(90)
pendown()
forward(10)

#end of project

#removing cursor

penup()
goto(-1000, 10000)
pendown()














     



exitonclick()


