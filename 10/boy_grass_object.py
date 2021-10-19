import random

from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):  # 생성자 : 객체의 속성에 대한 초기값을 만들어줌
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x = random.randint(100,700)
        self.y = 90
        self.frame = random.randint(0,7)

    def update(self): #소년의 행위 구현
        self.x += 5 #속성값을 바꿈으로써 행위(오른쪽이동) 구현
        self.frame = (self.frame +1) % 8

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x = random.randint(100,700)
        self.y = 599
    def update(self):
        if self.y > 90-20:
            self.y -= random.randint(8, 15)
        else:
            self.y = 90-23
    def draw(self):
        self.image.draw(self.x,self.y)

class BigBall:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x = random.randint(100,700)
        self.y = 599
    def update(self):
        if self.y > 90-19:
            self.y -= random.randint(8, 15)
        else:
            self.y = 90-21
    def draw(self):
        self.image.draw(self.x,self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()
grass = Grass() #Grass 라는 클래스로부터, grass 객체를 생성
#boy = Boy() #소년객체 생성


#team 만들기
team = [Boy() for i in range(11)]
balls = [Ball() for i in range(10)]
bigballs = [BigBall() for i in range(5)]

running = True
# game main loop code
while running:
    handle_events() #키 입력을 받아들이는 처리

    #Game logic
    #grass에 대한 상호작용
    for boy in team:
        boy.update()  # 소년의 상호작용
    for ball in balls:
        ball.update()
    for bigball in bigballs:
        bigball.update()

    #Game Drawing
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    for bigball in bigballs:
        bigball.draw()
    update_canvas()
    delay(0.05)

# finalization code