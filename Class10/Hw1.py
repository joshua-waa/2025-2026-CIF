import pygame
import random
pygame.init()

screenwidth = 800
screenheight = 600
screen = pygame.display.set_mode((screenwidth, screenheight))

clock = pygame.time.Clock()
playing = True

x=0#box
y=0
width=80#box
height=80#box
speed=4#speed of the box

move_up = False
move_down = False
move_left = False
move_right = False

fps = 30 #random color
change_color = 0
color_num = 0
color_list = [(255, 255, 255),(255, 0, 0),(0, 255, 0),(0, 0, 255),(255, 255, 0),(0, 255, 255),(128, 0, 128)]
while playing:
    clock.tick(fps)
    change_color+=1
    if change_color == 2*fps:
        change_color = 0
        color_num = random.randint(0, len(color_list)-1)
        print(color_num)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_up = True
            elif event.key == pygame.K_DOWN:
                move_down = True
            elif event.key == pygame.K_LEFT:
                move_left = True
            elif event.key == pygame.K_RIGHT:
                move_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_up = False
            elif event.key == pygame.K_DOWN:
                move_down = False
            elif event.key == pygame.K_LEFT:
                move_left = False
            elif event.key == pygame.K_RIGHT:
                move_right = False

    if move_up:
        y -= speed
    if move_down:
        y += speed
    if move_left:
        x -= speed
    if move_right:
        x += speed

    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if x > screenwidth - width:
        x = screenwidth - width
    if y > screenheight - height:
        y = screenheight - height

    screen.fill((0, 0, 0))
    rect=pygame.Rect(x,y,width,height)
    pygame.draw.rect(screen,color_list[color_num],rect)
    pygame.display.update()
pygame.quit()
