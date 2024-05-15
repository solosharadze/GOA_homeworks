from turtle import *


#we want to paint a house

#draw a square
speed(10)
color ("purple")
width(5)
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
color("green")
left (90)
forward (70)    #height of the door
right(90)
forward(60)
right(90)
forward(70)

penup()
goto (200, 200)

pendown()

begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()



penup()
goto(25, 115)
     
pendown()

left(120)
forward(55) 
left(90)     
forward(55)
left(90)    
forward(55)
left (90)   
forward(55)
penup()
goto(120, 115)
pendown()
left(90)
forward(55)
left(90)
forward(55)
left(90)
forward(55)
left(90)
forward(55)



exitonclick()