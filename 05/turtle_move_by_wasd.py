import turtle

#윗쪽이동
def drunken_move_w():
    turtle.penup();
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(50)
    turtle.stamp()

#왼쪽이동
def drunken_move_a():
    turtle.penup();
    turtle.setheading(180)
    turtle.pendown()
    turtle.forward(50)
    turtle.stamp()

#아래쪽이동
def drunken_move_s():
    turtle.penup();
    turtle.setheading(-90)
    turtle.pendown()
    turtle.forward(50)
    turtle.stamp()

#오른쪽이동
def drunken_move_d():
    turtle.penup();
    turtle.setheading(360)
    turtle.pendown()
    turtle.forward(50)
    turtle.stamp()

#리셋
def restart():
    turtle.reset()

turtle.shape('turtle')
turtle.onkey(drunken_move_w, 'w')
turtle.onkey(drunken_move_a, 'a')
turtle.onkey(drunken_move_s, 's')
turtle.onkey(drunken_move_d, 'd')

turtle.onkey(restart, 'Escape')
turtle.listen()
