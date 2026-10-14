from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball1:
    def __init__(self):
        self.x,self.y = random.randint(100,700),50
        self.frame = 0
        self.image = load_image('ball41x41.png')
    def update(self):
        a=random.randint(1,10)
        if self.y < 580 :
            self.y += a
        else:
            self.y -= a
    def draw(self):
        frame_width = 41 
        frame_height = 41
        self.image.clip_draw(self.frame * 100, 0, frame_width, frame_height,
                             self.x, self.y ,frame_width,frame_height)
class Ball2:
    def __init__(self):
        self.x,self.y = random.randint(100,700),50
        self.frame = 0
        self.image = load_image('ball21x21.png')
    def update(self):
        a=random.randint(1,10)
        if self.y < 590 :
            self.y += a
        else:
            self.y -= a
    def draw(self):
        frame_width = 21 
        frame_height = 21
        self.image.clip_draw(self.frame * 100, 0, frame_width, frame_height,
                             self.x, self.y ,frame_width,frame_height)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global team1
    global team2
    global team3
    global world
    global ball1
    global ball2
    world = []
    # 세계에 존재하는 객체들을 담는 리스트를 만든다
    
    running = True
    grass = Grass()
    ball1 = Ball1()
    ball2 = Ball2()
    world.append(grass)
    world.append(ball1)
    team1 = [Boy() for i in range(10)]
    world += team1
    team2 = [Ball1() for i in range(10)]
    world += team2
    team3 =[Ball2() for i in range(10)]
    world += team3

def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()



open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
