from pico2d import *

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SHIFT_DOWN, SHIFT_UP = range(7)
#0~6까지의 정수값이 할당

#딕셔너리 이용해서 ~
#key 는 (정수, 정수) tuple, value 는 정수
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,

    (SDL_KEYDOWN, SDLK_LSHIFT): SHIFT_DOWN,
    (SDL_KEYDOWN, SDLK_RSHIFT): SHIFT_DOWN,
    (SDL_KEYUP, SDLK_LSHIFT): SHIFT_UP,
    (SDL_KEYUP, SDLK_RSHIFT): SHIFT_UP,
}


# Boy States  이 클래스 자체를 하나의 싱글톤 객체로 인식해서 처리하도록 함
class IdleState:
    #Entry Action
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.timer = 500

    #exit action
    def exit(boy, event):
        pass
    #do action
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        if boy.timer == 0:
            boy.add_event(SLEEP_TIMER)

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)

class SleepState:
    def enter(boy, event):
        boy.frame = 0

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 8

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100,
                            3.141592 / 2, '', boy.x -25, boy.y -25, 100, 100)
        else:
            boy.image.clip_composite_draw(boy.frame * 100, 200, 100, 100,
                        -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)


class RunState:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.dir = boy.velocity

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1 ) % 8
        boy.timer -= 1

        boy.x += boy.velocity * 5
        boy.x = clamp(25, boy.x, 800-25)


    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


class DashState:
    def enter(boy, event):
        if event == SHIFT_DOWN:
            boy.speed = 15
        elif event == SHIFT_UP:
            boy.speed = 0
        boy.dash_timer = 100

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        #####################
        boy.dash_timer -= 1
        if boy.dash_timer == 0:
            boy.add_event(SHIFT_UP)
        ######################
        boy.x += boy.velocity * boy.speed
        boy.x = clamp(25, boy.x, 800 - 25)

    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)





next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState,
                RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                SLEEP_TIMER: SleepState,
                SHIFT_UP: IdleState, SHIFT_DOWN: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
               LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               SHIFT_UP: DashState, SHIFT_DOWN: DashState},
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState,
                 LEFT_UP: RunState, RIGHT_UP: RunState},

    DashState: {RIGHT_UP: RunState, LEFT_UP: RunState,
                RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                SHIFT_UP: RunState, SHIFT_DOWN: RunState}
}


class Boy:
    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.speed = 0
        self.frame = 0
        self.timer = 0
        self.dash_timer = 0

        self.event_que = [] #이벤트 큐 초기화
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        #현재 상태를 IdleState로 설정하고 entry action을 실행

    def change_state(self,  state):
        # fill here
        pass


    def add_event(self, event):
        self.event_que.insert(0, event)


    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)


    def draw(self):
        self.cur_state.draw(self)
        debug_print('Velocity :' + str(self.velocity) + ' Dir:' + str(self.dir))


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


