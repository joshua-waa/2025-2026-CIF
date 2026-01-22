import random
import pygame
import math

#
#swd
#
pygame.init()

# Screen
screenwidth = 800
screenheight = 600
screen = pygame.display.set_mode((screenwidth, screenheight))
bgcolor = (0, 0, 0)

# Jet setup
t_rad = 25
width = t_rad
height = t_rad * 3
turrent_image = pygame.image.load("turrent.png").convert_alpha()
turrent_image = pygame.transform.scale(turrent_image, (width, height))

x, y = screenwidth/2 - t_rad , screenheight/2 - t_rad
speed = 2

clock = pygame.time.Clock()
fps = 60
playing = True

move_up = move_down = move_left = move_right = False

# Bullets
bullets = []  # {"x","y","dx","dy"}
enemys = []

max_ammo = 10
ammo = max_ammo
reload_timer = 0
time_to_reload = 0.4
ammo_rad = 5

espeed = 1  # how fast enemy moves
espawn = 0
espawnps = 3 # how many spawn per second
e_rad = 20

lives = 3
while playing:
    clock.tick(fps)

    def make_enemy():
        side=random.randint(1,4)
        if side == 1:  ## LEFT
            ex = 0
            ey = random.randint(0,screenheight)
        elif side == 2:   ## TOP
            ex = random.randint(0,screenwidth)
            ey = 0
        elif side == 3: ##RIGHT
            ex = screenwidth
            ey = random.randint(0, screenheight)
        elif side == 4: ###BOTTOM
            ex = random.randint(0,screenwidth)
            ey = screenheight


        diff_x = x - ex
        diff_y = y - ey

        distance = (diff_x ** 2 + diff_y ** 2) ** 0.5  # Pythagoras

        edx = (diff_x / distance) * speed
        edy = (diff_y / distance) * speed

        enemys.append({"x": ex, "y": ey,"edx": edx, "edy": edy ,"t":0 })

    #EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT or lives <=0:
            playing = False

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_w, pygame.K_UP):
                move_up = True
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                move_down = True
            elif event.key in (pygame.K_a, pygame.K_LEFT):
                move_left = True
            elif event.key in (pygame.K_d, pygame.K_RIGHT):
                move_right = True

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_UP):
                move_up = False
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                move_down = False
            elif event.key in (pygame.K_a, pygame.K_LEFT):
                move_left = False
            elif event.key in (pygame.K_d, pygame.K_RIGHT):
                move_right = False

        #Mouse click shooting
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and ammo > 0:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                turrent_center_x = x + width // 2
                turrent_center_y = y + height // 2

                dx = mouse_x - turrent_center_x
                dy = mouse_y - turrent_center_y
                angle = math.atan2(-dy, dx)

                bullets.append({
                    "x": turrent_center_x,
                    "y": turrent_center_y,
                    "dx": math.cos(angle) * 8,
                    "dy": -math.sin(angle) * 8
                })

                ammo -= 1
                reload_timer = 0

    #MOVEMENT
    if move_left: x -= speed
    if move_right: x += speed
    if move_up: y -= speed
    if move_down: y += speed

    x = max(0, min(x, screenwidth - width))
    y = max(0, min(y, screenheight - height))

    #enemy spawn
    espawn +=1
    if espawn >= fps / espawnps:
        make_enemy()
        espawn = 0

    #RELOAD
    reload_timer += 1
    if reload_timer > time_to_reload*fps and ammo < max_ammo:
        ammo += 1
        reload_timer = 0

    # I got this online      the angle thing
    mouse_x, mouse_y = pygame.mouse.get_pos()
    turrent_center_x = x + width // 2
    turrent_center_y = y + height // 2

    dx = mouse_x - turrent_center_x
    dy = mouse_y - turrent_center_y
    angle = math.degrees(math.atan2(-dy, dx))

    turrent_center = (x, y)
    rotated_turrent = pygame.transform.rotate(turrent_image, angle-90)
    turrent_cir = pygame.draw.circle(screen, (255, 255, 255), turrent_center, t_rad)

    #BULLETs
    for bullet in bullets[:]:
        bullet["x"] += bullet["dx"]
        bullet["y"] += bullet["dy"]
        if (bullet["x"] < 0 or bullet["x"] > screenwidth or bullet["y"] < 0 or bullet["y"] > screenheight):
            bullets.remove(bullet)

    for enemy in enemys[:]:
        enemy["x"] += enemy["edx"]
        enemy["y"] += enemy["edy"]
        enemy["t"] += 1
        if enemy["t"] >= 20:
            if (enemy["x"] < 0 or enemy["x"] > screenwidth or enemy["y"] < 0 or enemy["y"] > screenheight):
                enemys.remove(enemy)
    #DRAW
    screen.fill(bgcolor)

    turrent_center = (x + width // 2, y + height // 2)
    pygame.draw.circle(screen, (255, 255, 255), turrent_center, t_rad)

    turrent_rect = rotated_turrent.get_rect(center=turrent_center)
    screen.blit(rotated_turrent, turrent_rect.topleft)



    for bullet in bullets:
        pygame.draw.circle(screen, (255, 255, 0),(int(bullet["x"]), int(bullet["y"])), ammo_rad)


    for enemy in enemys:
        pygame.draw.circle(screen, (255, 0, 0),(int(enemy["x"]), int(enemy["y"])), e_rad)
        dx = enemy["x"] - turrent_center_x
        dy = enemy["y"] - turrent_center_y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance <= e_rad + t_rad:
            if enemy in enemys:
                enemys.remove(enemy)
                lives -= 1
    for bullet in bullets[:]:
        for enemy in enemys[:]:
            dx = bullet["x"] - enemy["x"]
            dy = bullet["y"] - enemy["y"]
            distance = (dx ** 2 + dy ** 2) ** 0.5

            if distance <= ammo_rad + e_rad:
                # Collision detected: remove both
                if bullet in bullets:
                    bullets.remove(bullet)
                if enemy in enemys:
                    enemys.remove(enemy)

    ammo_text = pygame.font.SysFont("Comic Sans MS", 30).render(str(ammo), True, (0, 0, 0))
    screen.blit(ammo_text, (x+t_rad/12.5 , y+t_rad/3))
    screen.blit(pygame.font.SysFont("Comic Sans MS", 30).render(str(lives), True, (255, 255, 255)), (50, 50))

    pygame.display.update()

pygame.quit()
