from pico2d import*
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_square():
    x = 0
    while (x < 800):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.01)

    x = 800
    y = 90
    while (y < 600):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(800,y)
        y = y + 2
        delay (0.01)

    x = 800
    y = 90
    while (x > 0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x,600)
        x = x - 2
        delay(0.01)

    x = 0
    y = 600
    while (y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(0,y)
        y = y - 2
        delay(0.01)

    x = 0
    while (x < 400):
         clear_canvas_now()
         grass.draw_now(400, 30)
         character.draw_now(x, 90)
         x = x + 2
         delay(0.01)

def move_circle():
    cx = 400
    cy = 300
    r = 210
    for degree in range(270, 270 + 360):
        clear_canvas_now()
        grass.draw_now(400, 30)
        rad = math.radians(degree)
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        character.draw_now(x, y)

        delay(0.01)

while True:
    move_square()
    move_circle()
close_canvas()
