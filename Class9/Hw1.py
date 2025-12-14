import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()
playing = True
gbox=0
pbox=720
while playing:
    gbox+=5
    pbox-=5
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    screen.fill((0, 0, 0))
    grect=pygame.Rect(gbox,200,100,80)
    prect=pygame.Rect(pbox,100,100,80)
    pygame.draw.rect(screen,(0,255,0),grect)
    pygame.draw.rect(screen, (255, 100, 100), prect)
    pygame.display.update()
pygame.quit()
