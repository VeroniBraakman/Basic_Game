import pygame as p

WIDTH, HEIGHT = 600, 300
R_BORDER = 300
SCREEN = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("Basic Game")

LIGHTBLUE = (150, 200, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
FIGURE = p.image.load('stick_figure.png')
main_character = p.transform.scale(FIGURE, (600, 600))


def draw_window(m_c):
    SCREEN.fill(WHITE)
    SCREEN.blit(main_character, (m_c.x, m_c.y))
    p.display.update()

def move_main_character(e, m_c):
    if e.type == p.KEYDOWN:
        if e.key == p.K_RIGHT and m_c.x <= R_BORDER:
            m_c.x += 10
        if e.key == p.K_LEFT and m_c.x >= -275:
            m_c.x -= 10


def main():
    m_c = p.Rect((-250, 25), (10, 10))

    clock = p.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for e in p.event.get():
            if e.type == p.QUIT:
                run = False
            move_main_character(e, m_c)
        draw_window(m_c)

    p.quit()


if __name__ == "__main__":
    main()
