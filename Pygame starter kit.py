####### IMPORTANT
###### COMMENTED OR # IS OPTIONAL
# For moving boxes with controls is red
# # is text
# ################################### is pls change
from ctypes.wintypes import PWORD
from turtledemo.nim import SCREENWIDTH

import pygame

pygame.init()



# screen size
screenwidth = 800
screenheight = 600
screen = pygame.display.set_mode((screenwidth, screenheight))
bgcolor=(0,0,0)

#text/images
img_w=768   #centre the img
img_h=432   #centre the img
img_x = screenwidth // 2 - img_w // 2   #centre the img
img_y = screenheight // 2 - img_h // 2   #centre the img

image = pygame.image.load("Kashuhua.png").convert_alpha()
image = pygame.transform.scale(image, (img_w, img_h))



font=pygame.font.SysFont("Comic Sans MS", 30)
word_color=(255,255,255)
text="PUT YOUR TEXT HERE" ###################################################

clock = pygame.time.Clock()
playing = True

# box position
x = 0
y = 0
width = 80   # box width ################################################
height = 80  # box height ############################################
speed = 4    # speed of the box ################################################

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
            if event.key in (pygame.K_w, pygame.K_UP):
                move_up = True
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                move_down = True
            elif event.key in (pygame.K_a, pygame.K_LEFT):
                move_left = True
            elif event.key in (pygame.K_d, pygame.K_RIGHT):
                move_right = True

        # key released
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_UP):
                move_up = False
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                move_down = False
            elif event.key in (pygame.K_a, pygame.K_LEFT):
                move_left = False
            elif event.key in (pygame.K_d, pygame.K_RIGHT):
                move_right = False

    dx = 0 #direction(1 is right 0 is left)
    dy = 0 #direction(1 is down 0 is up)
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

    # text
    screen.blit(font.render(text, True, word_color), (0, 0))################
    screen.blit(image, (img_x, img_y))


    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if x > screenwidth - width:
        x = screenwidth - width
    if y > screenheight - height:
        y = screenheight - height

    #before movement/ wasd detection
    #old_x=x
    #old_y=y

    #for collision, use
    #if rect.colliderect(rect2):
        #x=old_x
        #y=old_y

    rect = pygame.Rect(x, y, width, height)    # draw box
    pygame.draw.rect(screen, (255, 255, 255), rect)    # draw box

    pygame.display.update()

pygame.quit()
