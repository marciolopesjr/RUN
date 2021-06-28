import pygame as pg 
from pygame.math import Vector2

def main():
    pg.init()
    screen = pg.display.set_mode((640, 480))
    clock = pg.time.Clock()
    image = pg.Surface((30, 30))
    image.fill(pg.Color('dodgerblue1'))
    x, y = 300, 200 
    rect = image.get_rect(center=(x, y))

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
        screen.blit(image, rect)

        pg.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
    pg.quit()
