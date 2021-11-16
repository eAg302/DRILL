import game_framework
from pico2d import *

from random import randint
import game_world

# Bird FLY Speed
PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm
FLY_SPEED_KMPH = 30.0  # Km / Hour
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14



# Bird Event
# RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE = range(6)
#
# key_event_table = {
#     (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
#     (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
#     (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
#     (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
#     (SDL_KEYDOWN, SDLK_SPACE): SPACE
# }

FLY_RIGHT, FLY_LEFT = range(2)




# Bird States

class IdleState:

    def enter(bird, event):
        bird.velocity += FLY_SPEED_PPS
        bird.timer = 1000

    def exit(bird, event):
        pass

    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

    def draw(bird):
        if bird.dir == 1:
            bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y)
        else:
            bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y)


class FlyState:

    def enter(bird, event):
        if bird.x < 1550:
            bird.velocity += FLY_SPEED_PPS
        elif bird.x > 50:
            bird.velocity -= FLY_SPEED_PPS
        bird.dir = clamp(-1, bird.velocity, 1)

    def exit(bird, event):
        pass

    def do(bird):
        #bird.frame = (bird.frame + 1) % 8
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        bird.x += bird.velocity * game_framework.frame_time
        bird.x = clamp(25, bird.x, 1600 - 25)

    def draw(bird):
        if bird.dir == 1:
            bird.image.clip_draw(int(bird.frame) * 100, 100, 100, 100, bird.x, bird.y)
        else:
            bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y)



# next_state_table = {
#     IdleState: {RIGHT_UP: FLYState, LEFT_UP: FLYState, RIGHT_DOWN: FLYState, LEFT_DOWN: FLYState, SLEEP_TIMER: SleepState, SPACE: IdleState},
#     FLYState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: FLYState},
#     SleepState: {LEFT_DOWN: FLYState, RIGHT_DOWN: FLYState, LEFT_UP: FLYState, RIGHT_UP: FLYState, SPACE: IdleState}
# }

next_state_table = {
    IdleState: FlyState,
    FlyState: IdleState
}



class Bird:

    def __init__(self):
        self.x, self.y = randint(100,1500), randint(100,500)

        self.image = load_image('bird100x100x14.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def get_bb(self):
        # fill here
        return 0, 0, 0, 0


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        # if len(self.event_que) > 0:
        #     event = self.event_que.pop()
        #     self.cur_state.exit(self, event)
        #     self.cur_state = next_state_table[self.cur_state][event]
        #     self.cur_state.enter(self, event)
        pass

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        #fill here


    def handle_event(self, event):
        pass

