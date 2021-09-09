import turtle


count = 6
count2 = 6
X = -100
Y= 300


turtle.penup()
turtle.right(90)

while(count > 0):
    turtle.goto(X,Y)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    X +=100
    count -= 1


X = -100
Y = 300
turtle.left(90)

while(count2 > 0):
    turtle.goto(X,Y)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    Y -=100
    count2 -= 1


turtle.exitonclick()
