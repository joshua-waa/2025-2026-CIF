############################THINGS WITH THIS HASHTAGS ARE OPTIONAL


import pygame
from pygame import K_DOWN, K_LEFT, K_RIGHT

pygame.init()

#text
font = pygame.font.SysFont("Comic Sans MS", 30) ##################################
textsurface = font.render("PUT YOUR TEXT HERE", False, (255, 255, 255))#########################

# screen size
screenwidth = 800
screenheight = 600
screen = pygame.display.set_mode((screenwidth, screenheight))
bgcolor=(0,0,0)

clock = pygame.time.Clock()
playing = True

# box position
x = 0  ###########
y = 0  ######################
width = 80   # box width##############
height = 80  # box height#################
speed = 4    # speed of the box#####

# movement flags
move_up = False  ###############
move_down = False    ###########
move_left = False    ###########
move_right = False    ###########

while playing:

    clock.tick(30)  # FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        # key pressed
        if event.type == pygame.KEYDOWN:     ###########
            if event.key == pygame.K_w or K_up:
                move_up = True
            elif event.key == pygame.K_s or K_DOWN:
                move_down = True
            elif event.key == pygame.K_a or K_LEFT:
                move_left = True
            elif event.key == pygame.K_d or K_RIGHT:
                move_right = True

        # key released
        if event.type == pygame.KEYUP:    ###########
            if event.key == pygame.K_w or K_up:
                move_up = False
            elif event.key == pygame.K_s or K_DOWN:
                move_down = False
            elif event.key == pygame.K_a or K_LEFT:
                move_left = False
            elif event.key == pygame.K_d or K_RIGHT:
                move_right = False

    dx = 0      ###########
    dy = 0    ###########
    # horizontal movement
    if move_left:    ###########
        dx -= 1
    if move_right:    ###########
        dx += 1

    # vertical movement
    if move_up:    ###########
        dy -= 1
    if move_down:    ###########
        dy += 1

    if dx != 0 or dy != 0:  #to prevent dividing by 0    ###########    ###########    ###########    ###########    ###########
        length = (dx **2 + dy**2) ** 0.5  # ** is power of   # pythagorean theorem    ###########    ###########
        dx = dx / length   # make distance for movement *1.???? for speed    ###########    ###########
        dy = dy / length   # make distance for movement *1.???? for speed    ###########    ###########
        x += dx * speed    ###########    ###########
        y += dy * speed    ###########    ###########

    screen.fill(bgcolor)  # background color

    # text
    screen.blit(textsurface, (0, 0))     ###########

    #borders
    if x < 0:     ###########    ###########    ###########
        x = 0    ###########    ###########    ###########    ###########
    if y < 0:    ###########    ###########    ###########
        y = 0    ###########    ###########    ###########
    if x > screenwidth - width:    ###########    ###########    ###########
        x = screenwidth - width    ###########    ###########    ###########
    if y > screenheight - height:    ###########    ###########    ###########
        y = screenheight - height    ###########    ###########    ###########

    # draw box
    rect = pygame.Rect(x, y, width, height)    ###########    ###########    ###########
    pygame.draw.rect(screen, (255, 255, 255), rect)    ###########    ###########    ###########

    pygame.display.update()

pygame.quit()
