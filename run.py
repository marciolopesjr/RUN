import random 
import pygame as pg 
from pygame.math import Vector2

def main():
    pg.init()
    screen = pg.display.set_mode((640, 480))
    eye = pg.image.load('eye.png')
    pg.display.set_icon(eye)
    pg.display.set_caption("run!")
    clock = pg.time.Clock()
    image = pg.Surface((30, 30))
    mirror = pg.image.load('mirror.png')
    mX = random.randint(0, 640)
    mY = random.randint(0, 480)
    minMirror = pg.transform.scale(mirror, (48, 57))
    image.fill(pg.Color('dodgerblue1'))
    x, y = 300, 200 
    rect = eye.get_rect(center=(x, y))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        mouse_pos = pg.mouse.get_pos()
        run = (mouse_pos[0] - x) * 0.1  
        rise = (mouse_pos[1] - y) * 0.1
        x += run
        y += rise
        rect.center = x, y

        screen.fill((30, 30, 30))
        screen.blit(eye, rect)
        screen.blit(minMirror, (mX, mY))

        pg.display.flip()
        clock.tick(60)
        print(clock)


if __name__ == '__main__':
    main()
    pg.quit()
