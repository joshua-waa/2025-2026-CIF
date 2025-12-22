####### IMPORTANT
###### COMMENTED OR # IS OPTIONAL
# For moving boxes with controls is red
# # is text

import pygame
from pygame import K_DOWN, K_LEFT, K_RIGHT, K_UP

pygame.init()

font = pygame.font.SysFont("Comic Sans MS", 30)

# screen size
screenwidth = 800
screenheight = 600
screen = pygame.display.set_mode((screenwidth, screenheight))
bgcolor=(0,0,0)

clock = pygame.time.Clock()
playing = True

# box position
x = 0
y = 0
width = 80   # box width
height = 80  # box height
speed = 4    # speed of the box

# movement flags
move_up = False
move_down = False
move_left = False
move_right = False

while playing:

    clock.tick(30)  # FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        # key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == K_UP:
                move_up = True
            elif event.key == pygame.K_s or event.key == K_DOWN:
                move_down = True
            elif event.key == pygame.K_a or event.key == K_LEFT:
                move_left = True
            elif event.key == pygame.K_d or event.key == K_RIGHT:
                move_right = True

        # key released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == K_UP:
                move_up = False
            elif event.key == pygame.K_s or event.key == K_DOWN:
                move_down = False
            elif event.key == pygame.K_a or event.key == K_LEFT:
                move_left = False
            elif event.key == pygame.K_d or event.key == K_RIGHT:
                move_right = False

    dx = 0
    dy = 0
    # horizontal movement
    if move_left:
        dx -= 1
    if move_right:
        dx += 1

    # vertical movement
    if move_up:
        dy -= 1
    if move_down:
        dy += 1

    if dx != 0 or dy != 0:  #to prevent dividing by 0
        length = (dx **2 + dy**2) ** 0.5  # ** is power of   # pythagorean theorem
        dx = dx / length   # make distance for movement *1.???? for speed
        dy = dy / length   # make distance for movement *1.???? for speed
        x += dx * speed
        y += dy * speed

    screen.fill(bgcolor)  # background color

    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if x > screenwidth - width:
        x = screenwidth - width
    if y > screenheight - height:
        y = screenheight - height

    # draw box
    rect = pygame.Rect(x, y, width, height)
    grect = pygame.Rect(screenwidth / 2 , screenheight / 2, width, height)
    pygame.draw.rect(screen, (0, 255, 0), grect)
    pygame.draw.rect(screen, (255, 100, 100), rect)

    if rect.colliderect(grect):
        textsurface = font.render("COLLIDED", False, (255, 255, 255))
    else:
        textsurface = font.render("", False, (255, 255, 255))
    screen.blit(textsurface, (0, 0))

    pygame.display.update()

pygame.quit()
