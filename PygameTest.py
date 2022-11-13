import pygame as p

WIDTH, HEIGHT = 600, 300
SCREEN = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("Basic Game")

LIGHTBLUE = (150, 200, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
FIGURE = p.image.load('stick_figure.png')
main_character = p.transform.scale(FIGURE, (600, 600))


def draw_window(c):
    SCREEN.fill(WHITE)
    SCREEN.blit(main_character, (c.x, c.y))
    p.display.update()


def main():
    c = p.Rect(-250, 25, 600, 600)

    clock = p.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for e in p.event.get():
            if e.type == p.QUIT:
                run = False
            if e.type == p.KEYDOWN:
                if e.key == p.K_RIGHT:
                    c.x += 10
        draw_window(c)

    p.quit()


if __name__ == "__main__":
    main()
