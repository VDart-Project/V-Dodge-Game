# initalizations
import random
import pygame
import os
pygame.init()

# clock cycle
clock = pygame.time.Clock()

# image basics, constant throughout
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("V-Dodge")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# home screen background information
hs_bg = pygame.image.load(os.path.join('pygame_background.png')).convert()
hs_bg1 = pygame.image.load(os.path.join('pygame_background.png')).convert()
hs_bgX = 0
hs_bgX2 = hs_bg.get_width()

# background information
bg = pygame.image.load(os.path.join('bg1.png')).convert()
bg1 = pygame.image.load(os.path.join('bg1.png')).convert()
bgX = 0
bgX2 = bg.get_width()

# vdart logo player ship
playerImg = pygame.image.load('vdart_logo.png')
playerX = 80
playerY = 300

# values
speed = 25
vel = 10

# asteroid intialization
asteroidImg = []
asteroidX = []
asteroidY = []
asteroidX_change = []
asteroidY_change = []
num_asteroid = 10

# adds new asteroids to list
for i in range(num_asteroid):
    asteroidImg.append(pygame.image.load('asteroid.png'))
    asteroidX.append(random.randint(650, 750))
    asteroidY.append(random.randint(50, 450))
    asteroidX_change.append(i)
    asteroidY_change.append(i)

# home screen
hs_font = pygame.font.SysFont('comicsansms.ttf', 64)

# score
score_value = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)

# game over
go_font = pygame.font.Font('freesansbold.ttf', 69)

# replay
r_font = pygame.font.Font('freesansbold.ttf', 22)

def game_over_text():
    over_text = go_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def asteroid(x: object, y: object) -> object:
    screen.blit(asteroidImg[i], (x, y))

def redrawWindow():
    screen.blit(bg, (bgX, 0))
    screen.blit(bg, (bgX2, 0))
    player(playerX, playerY)
    asteroid(asteroidX[i], asteroidY[i])
    pygame.display.update()

running_game = True
winning = True
start = True
score = 0
delay = 0
level = 0
level_up = 0

# MAIN WHILE LOOP
while running_game:
    # redrawWindow()
    clock.tick(speed)
    clock.tick(speed)
    
    # home screen
    if start:
        screen.fill((0, 0, 0))
        screen.blit(hs_bg1, (0, 0))
        screen.blit(hs_font.render("Welcome to V-Dodge", True, (255, 24, 130)), (180, 250))
        print_next = hs_font.render("Game will begin shortly", True, (255, 24, 130))
        screen.blit(print_next, (150, 300))
        pygame.display.update()
        while delay < 50000:
            delay += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_game = False
                    pygame.quit()
                    quit()
        winning = True
        start = False

    # checks if the game has be exited
    while winning:
        for event in pygame.event.get():
            # exit button check
            if event.type == pygame.QUIT:
                running_game = False
                pygame.quit()
                quit()

        clock.tick(speed)
        clock.tick(speed)
        # scrolls images back
        bgX -= 1.4
        bgX2 -= 1.4
        if bgX < bg.get_width() * -1:
            bgX = bg.get_width()

        if bgX2 < bg.get_width() * -1:
            bgX2 = bg.get_width()

        # sets background
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        # moves vdart logo
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            playerY -= vel
        if keys[pygame.K_DOWN]:
            playerY += vel

        # ensures that logo is still on screen
        if playerY <= 0:
            playerY = 0
        elif playerY >= 566:
            playerY = 566

        level_up += 1
        if level_up < 100:
            num_asteroid = 3
        if level_up > 200:
            num_asteroid = 4
        if level_up > 400:
            num_asteroid = 5
        if level_up > 600:
            num_asteroid = 6
        if level_up > 800:
            num_asteroid = 7

        # asteroids
        for i in range(num_asteroid):
            asteroidX[i] += asteroidX_change[i]
            asteroidY[i] = asteroidY_change[i]
            if asteroidX[i] > 0:
                asteroidX_change[i] = -20
            if asteroidX[i] <= 0:
                rnd_x = random.randrange(600, 800)
                rnd_y = random.randrange(40, 560)
                asteroidX_change[i] = rnd_x
                asteroidY_change[i] = rnd_y
                score += 1
        for i in range(num_asteroid):
            if ((asteroidY[i] >= playerY and (asteroidY[i]) <= (playerY + 35)) and (asteroidX[i] >= playerX and (asteroidX[i]) <= (playerX + 60))):
                winning = False
                for i in range(num_asteroid):
                    asteroidX[i] = 800
                    asteroidY[i] = 600

        redrawWindow()
        player(playerX, playerY)
        asteroid(asteroidX[0], asteroidY[0])
        asteroid(asteroidX[1], asteroidY[1])
        asteroid(asteroidX[2], asteroidY[2])
        if num_asteroid >= 4:
            asteroid(asteroidX[3], asteroidY[3])
        if num_asteroid >= 5:
            asteroid(asteroidX[4], asteroidY[4])
        if num_asteroid >= 6:
            asteroid(asteroidX[5], asteroidY[5])
        if num_asteroid >= 7:
            asteroid(asteroidX[6], asteroidY[6])
        if num_asteroid >= 8:
            asteroid(asteroidX[7], asteroidY[7])
        if num_asteroid >= 9:
            asteroid(asteroidX[8], asteroidY[8])
        if num_asteroid >= 10:
            asteroid(asteroidX[9], asteroidY[9])
        pygame.display.update()

    # exit button check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
            pygame.quit()
            quit()

    # game over page
    screen.fill((0, 0, 0))
    bg1 = pygame.image.load(os.path.join('pygame_background.png')).convert()
    screen.blit(bg1, (0, 0))
    screen.blit(go_font.render("GAME OVER", True, (255, 0, 0)), (200, 155))
    print_score = score_font.render("Score: " + str(score*10), True, (255, 100, 100))
    screen.blit(print_score, (325, 275))
    Next = pygame.key.get_pressed()
    print_next = r_font.render("PRESS SPACEBAR TO RETRY", True, (255, 255, 255))
    screen.blit(print_next, (240, 375))

    # Restarting V-Dodge
    if Next[pygame.K_SPACE]:
        winning = True
        score = 0
        playerX = 80
        playerY = 300
        num_asteroid = 3
        level_up = 0

    pygame.display.update()