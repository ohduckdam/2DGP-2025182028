from pico2d import *


open_canvas(800, 600)

# 여기를 채우시오.
import math

open_canvas(800, 600)

# 여기를 채우시오.
grass = load_image('grass.png')
character = load_image('character.png')

# 원운동 설정
center_x, center_y = 400, 300   # 화면 중앙
radius = 150                    # 화면 안에 들어오는 반지름
angle = 0                       # 시작 각도

while 1:
    clear_canvas()  # 이전 프레임 지우기

    rad = math.radians(angle)
    x = center_x + radius * math.cos(rad)
    y = center_y + radius * math.sin(rad)

    character.draw( x, y) 

    angle += 2          # 각도를 조금씩 증가
    if angle >= 360:
        angle -= 360     # 각도가 360 넘으면 다시 0부터 (끊기지 않게 순환)

    update_canvas()
    delay(0.01)          # 프레임 속도 조절

close_canvas()

close_canvas()

