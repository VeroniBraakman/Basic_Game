import pygame as p

WIDTH, HEIGHT = 600, 300
R_BORDER = 300
SCREEN = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("Basic Game")

VEL = 1
BLACK = (0, 0, 0)
GREY = (60, 60, 60)
WHITE = (255, 255, 255)
FPS = 60
FIGURE = p.image.load('stick_figure.png')
OBJECT= p.image.load('object1.png')
main_character = p.transform.scale(FIGURE, (600, 600))
main_object = p.transform.scale(OBJECT, (40, 25))


def draw_window(m_c, m_o):
    SCREEN.fill(WHITE)
    SCREEN.blit(main_character, (m_c.x, m_c.y))
    SCREEN.blit(main_object, (m_o.x, m_o.y))
    p.draw.line(SCREEN, GREY, (0, 245), (600, 245), 1)
    #p.draw.rect(SCREEN, GREY, p.Rect(450, 220, 25, 25), 1)
    p.display.update()

def move_main_character(e, m_c):
    if e.type == p.KEYDOWN:
        if e.key == p.K_RIGHT and m_c.x <= R_BORDER:
            m_c.x += 10
        if e.key == p.K_LEFT and m_c.x >= -275:
            m_c.x -= 10

def move_main_object(m_o):
    p.time.delay(10)
    m_o.x = m_o.x - VEL
    if m_o.x < 0:
        m_o.x = 450

def main():
    m_c = p.Rect((-250, 25), (10, 10))
    m_o = p.Rect((450, 222), (10, 10))

    clock = p.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        move_main_object(m_o)
        for e in p.event.get():
            if e.type == p.QUIT:
                run = False
            move_main_character(e, m_c)
        draw_window(m_c, m_o)

    p.quit()


if __name__ == "__main__":
    main()
