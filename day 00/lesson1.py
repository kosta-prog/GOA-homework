from turtle import *

#we want to paint a house

#step 1: draw a square
speed(10)
width(7)
color("yellow")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("purple")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end of height of the door

#drawing windows

color("purple")
penup()
goto(150, 100)
pendown()

right(150)
begin_fill()
forward(50)
right(90)
forward(25)
right(90)
forward(50)
right(90)
forward(25)
end_fill()

penup()
goto(50, 100)
pendown()

begin_fill()
forward(25)
right(90)
forward(50)
right(90)
forward(25)
right(90)
forward(50)
end_fill()



exitonclick()