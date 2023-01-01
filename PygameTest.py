import pygame as p

p.init()

WIDTH, HEIGHT = 600, 300
R_BORDER = 570
SCREEN = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("Basic Game")

VEL = 2
BLACK = (0, 0, 0)
GREY = (60, 60, 60)
WHITE = (255, 255, 255)
FPS = 60
FIGURE = p.image.load('poppetje.png')
OBJECT= p.image.load('object1.png')
main_character = p.transform.scale(FIGURE, (50,80))
main_object = p.transform.scale(OBJECT, (40, 25))
jump = False

def draw_window(m_c, m_o):
    SCREEN.fill(WHITE)
    SCREEN.blit(main_character, (m_c.x, m_c.y))
    SCREEN.blit(main_object, (m_o.x, m_o.y))
    p.draw.line(SCREEN, GREY, (0, 245), (600, 245), 1)
    p.display.update()

def move_main_character(m_c):
    key_input = p.key.get_pressed()
    if key_input[p.K_RIGHT] and m_c.x <= R_BORDER:
        m_c.x += 2
    if key_input[p.K_LEFT] and m_c.x >= 0:
        m_c.x -= 2

def detect_collision(m_o, m_c):
    #if m_o.x < m_c.x and m_c.y >= 168:
    #    m_c.x = 0
    if m_c.x == m_o.x and m_c.y > 158:
        print("Hello")
        m_c.x = 0
        # dit werkt niet goed.

def move_main_object(m_o):
    p.time.delay(10)
    m_o.x = m_o.x - VEL
    #print(m_o.x)
    if m_o.x < -40:
        m_o.x = 620


def main():
    m_c = p.Rect((0, 168), (10, 10))
    m_o = p.Rect((620, 222), (10, 10))
    jump = False
    jumpCount = 0
    jumpMax = 15

    clock = p.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        move_main_object(m_o)
        move_main_character(m_c)
        detect_collision(m_o, m_c)
        draw_window(m_c, m_o)

        for e in p.event.get():
            if e.type == p.QUIT:
                run = False
            if e.type == p.KEYDOWN:
                if not jump and e.key == p.K_SPACE:
                    jump = True
                    jumpCount = jumpMax

        if jump:
            m_c.y -= jumpCount
            if jumpCount > -jumpMax:
                jumpCount -= 1
            else:
                jump = False

    p.quit()


if __name__ == "__main__":
    main()
