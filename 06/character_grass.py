from pico2d import *
import math

def move_shape_circle(a):
    while a<360:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400 + 220 * math.cos(a / 360*2*math.pi) , 300+ 220 * math.sin(a / 360*2*math.pi))
        a += 10
        delay(0.01)

def move_shape_rectangle(x,y):
    while x<=750 and y==90:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x+=10   
        delay(0.01)    

    while y<550:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y+=10    
        delay(0.01)

    while x>10 and y==550:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x-=10    
        delay(0.01)

    while x==10 and y>90:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y-=10    
        delay(0.01)    

    
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')
count = 0 #홀짝 판별

while True:
    if count % 2 == 0 : #짝수번째에 사각형운동
        move_shape_rectangle(10,90)
       
    if count % 2 == 1 : #홀수번째에 원운동
        move_shape_circle(0)
        
    count += 1
    
    
close_canvas()


