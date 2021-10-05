from pico2d import *
from random import randint


KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def move_to_hand():
    global x, y
    global a, b
    x = a
    y = b
    delay(0.2)
    if x == a and y == b:
        a = randint(1, 1024)
        b = randint(1, 1080)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

#
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
a = randint(1, KPU_WIDTH)
b = randint(1, KPU_HEIGHT)

# hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand.draw(a, b)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    handle_events()
    move_to_hand()


close_canvas()




