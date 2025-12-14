import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
playing = True
x=0
y=0
while playing:
    clock.tick(30)
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    if key[pygame.K_UP]:
        y-=4
    if key[pygame.K_DOWN]:
        y+=4
    if key[pygame.K_LEFT]:
        x-=4
    if key[pygame.K_RIGHT]:
        x+=4
    screen.fill((0, 0, 0))
    grect=pygame.Rect(x,y,100,80)
    pygame.draw.rect(screen,(0,255,0),grect)
    pygame.display.update()
pygame.quit()
