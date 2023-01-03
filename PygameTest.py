import pygame as p

p.init()

WIDTH, HEIGHT = 600, 300
SCREEN = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("Game")

VEL = 2
BLACK = (0, 0, 0)
GREY = (60, 60, 60)
WHITE = (255, 255, 255)
FPS = 60
jump = False

def draw_window():
    SCREEN.fill(WHITE)
    #ground
    p.draw.line(SCREEN, GREY, (0, 245), (600, 245), 1)
    #flag
    p.draw.line(SCREEN, GREY, (550, 245), (550, 180), 3)
    p.draw.line(SCREEN, GREY, (550, 180), (570, 200), 3)
    p.draw.line(SCREEN, GREY, (550, 200), (570, 200), 3)


def create_obstacle(obstacle):
    p.draw.rect(SCREEN, BLACK, p.Rect(obstacle.x, obstacle.y, 20, 20))

def move_obstacle(obstacle, hero):
    if hero.x <= 550:
        p.time.delay(10)
        obstacle.x -= VEL
        if obstacle.x <= 0:
            obstacle.x = WIDTH

def create_a_hero(hero):
    p.draw.rect(SCREEN, BLACK, p.Rect(hero.x, hero.y, 10, 50), 2)
    key_input = p.key.get_pressed()
    if key_input[p.K_RIGHT] and hero.x <= WIDTH:
        hero.x += 2
    if key_input[p.K_LEFT] and hero.x >= 0:
        hero.x -= 2

def check_collision(hero, obstacle):
    collide = p.Rect.colliderect(hero, obstacle)
    if collide:
        hero.x = 20

def winning(hero):
    if  hero.x >= 550:
        font = p.font.Font('freesansbold.ttf', 26)
        text = font.render('You Won!', True, WHITE, BLACK)
        textRect = text.get_rect()
        textRect.center = (500, 50)
        SCREEN.blit(text, textRect)

def main():
    hero = p.Rect((20, 195), (10, 50))
    obstacle = p.Rect((WIDTH, 225, 20, 20))
    jump = False
    jumpCount = 0
    jumpMax = 15

    clock = p.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        draw_window()
        create_a_hero(hero)
        create_obstacle(obstacle)
        move_obstacle(obstacle, hero)
        check_collision(hero, obstacle)
        winning(hero)
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
