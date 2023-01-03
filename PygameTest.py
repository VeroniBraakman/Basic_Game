import pygame as p

p.init()

WIDTH, HEIGHT = 600, 300
SCREEN = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("Basic Game")

VEL = 2
BLACK = (0, 0, 0)
GREY = (60, 60, 60)
WHITE = (255, 255, 255)
FPS = 60
jump = False

def draw_window():
    x = 320
    y = 225
    SCREEN.fill(WHITE)
    p.draw.line(SCREEN, GREY, (0, 245), (600, 245), 1)
    obstacle = p.draw.rect(SCREEN, BLACK, p.Rect(x, y, 20, 20))

def create_a_hero(hero):
    p.draw.rect(SCREEN, BLACK, p.Rect(hero.x, hero.y, 10, 80), 2)
    key_input = p.key.get_pressed()
    if key_input[p.K_RIGHT] and hero.x <= WIDTH:
        hero.x += 2
    if key_input[p.K_LEFT] and hero.x >= 0:
        hero.x -= 2

def main():
    hero = p.Rect((20, 165), (10, 80))
    jump = False
    jumpCount = 0
    jumpMax = 15

    clock = p.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        draw_window()
        create_a_hero(hero)
        p.display.update()

        for e in p.event.get():
            if e.type == p.QUIT:
                run = False
            if e.type == p.KEYDOWN:
                if not jump and e.key == p.K_SPACE:
                    jump = True
                    jumpCount = jumpMax

        if jump:
            hero.y -= jumpCount
            if jumpCount > -jumpMax:
                jumpCount -= 1
            else:
                jump = False

    p.quit()


if __name__ == "__main__":
    main()
