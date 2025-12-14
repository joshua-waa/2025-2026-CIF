import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600)) #size
clock = pygame.time.Clock()
playing = True
x=?
y=?
while playing:
    clock.tick(30) #fps
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    #if key[pygame.K_UP]:    is for controllable things
    screen.fill((0, 0, 0))  # Fills with black
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, (color rgb), rect)
    pygame.display.update()
pygame.quit()
