import random
from math import floor

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
bg_color = (0, 0, 0)

# Jet setup
t_rad = 25
width = t_rad
height = t_rad * 3
turrent_image = pygame.image.load("turrent.png").convert_alpha()
turrent_image = pygame.transform.scale(turrent_image, (width, height))

x, y = screenwidth/2, screenheight/2
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
e_spawn = 0
e_spawn_ps = 3 # how many spawn per second
e_rad = 20
distance = 0

lives = 3
scene = "main"

#shop
money = 0
multi_cost = 100
multi_bullet = 1

not_enough = False


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

        edx = (diff_x / distance) * espeed
        edy = (diff_y / distance) * espeed
        enemys.append({"x": ex, "y": ey,"edx": edx, "edy": edy ,"t":0 })

    def make_text(tx,ty,color,yap,size):
        font = pygame.font.SysFont("Comic Sans MS", size)
        text_surface = font.render(str(yap), True, color)
        screen.blit(text_surface, (tx, ty))

    #EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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

                bullets.append({"x": turrent_center_x,"y": turrent_center_y,"dx": math.cos(angle) * 8,"dy": -math.sin(angle) * 8})

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
    if scene == "game":
        e_spawn +=1
        if e_spawn >= fps / e_spawn_ps:
            make_enemy()
            e_spawn = 0

    if lives <= 0:
        scene = "main"
        lives = 3

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
            continue

    #DRAW #################################
    screen.fill(bg_color)
    if scene == "main":
        rect_play = pygame.Rect(350, 200, 100, 50)
        rect_how = pygame.Rect(500, 200, 100, 50)
        rect_shop = pygame.Rect(200, 200, 100, 50)
        pygame.draw.rect(screen, (255, 255, 255), rect_play)
        pygame.draw.rect(screen, (255, 255, 255), rect_how)
        pygame.draw.rect(screen, (255, 255, 255), rect_shop)
        make_text(375, 200, (0, 0, 0), "Play",30)
        make_text(510, 205, (0, 0, 0), "How 2?",25)
        make_text(215, 200, (0, 0, 0), "Shop", 30)

    if scene == "shop":
        rect_upg_multi_s = pygame.Rect(200, 200, 100, 50)
        rect_upg_atk_spd = pygame.Rect(500, 200, 100, 50)
        pygame.draw.rect(screen, (255, 255, 255), rect_upg_multi_s)
        pygame.draw.rect(screen, (255, 255, 255), rect_upg_atk_spd)
        make_text(205, 200, (0, 0, 0), "Multishot", 20)
        make_text(205, 220, (0, 0, 0), f"{multi_cost}$ -> {floor(multi_cost ** 1.1)}$", 10)
        make_text(205, 230, (0, 0, 0), f"{multi_bullet}$ -> {multi_bullet + 2}$", 10)
        make_text(510, 205, (0, 0, 0), "How 2?", 25)

        make_text(x+t_rad/12.5-2.5,y+t_rad/3,(0,0,0),ammo,30)
        make_text(50,50,(255,255,255),lives,30)

    for enemy in enemys[:]:
        # move
        enemy["x"] += enemy["edx"]
        enemy["y"] += enemy["edy"]
        enemy["t"] += 1

        # off-screen cleanup
        if enemy["t"] >= 20:
            if (enemy["x"] < 0 or enemy["x"] > screenwidth or enemy["y"] < 0 or enemy["y"] > screenheight):
                enemys.remove(enemy)
                continue

            # draw
        pygame.draw.circle(screen, (255, 0, 0),(int(enemy["x"]), int(enemy["y"])),e_rad)

            # player collision
        dx = enemy["x"] - turrent_center_x
        dy = enemy["y"] - turrent_center_y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance <= e_rad + t_rad:
            enemys.remove(enemy)
            lives -= 1

    if scene == "game":
        turrent_center = (x + width // 2, y + height // 2)

    # *---------draw sphere and turrent---------*
    pygame.draw.circle(screen, (255, 255, 255), turrent_center, t_rad)
    turrent_rect = rotated_turrent.get_rect(center=turrent_center)
    screen.blit(rotated_turrent, turrent_rect.topleft)

    for bullet in bullets[:]:
        bullet["rect"] = pygame.Rect(int(bullet["x"]) - ammo_rad,int(bullet["y"]) - ammo_rad,ammo_rad * 2, ammo_rad * 2)
        pygame.draw.circle(screen,(255, 255, 0), bullet["rect"].center,ammo_rad)
        if scene == "main":
            ammo = 100
            if bullet["rect"].colliderect(rect_shop):
                scene = "shop"
                bullets.remove(bullet)
                continue

            elif bullet["rect"].colliderect(rect_play):
                scene = "game"
                bullets.remove(bullet)
                continue

            elif bullet["rect"].colliderect(rect_how):
                scene = "how"
                bullets.remove(bullet)
                continue

            for enemy in enemys[:]:
                enemys.remove(enemy)

        if scene == "shop":
            ammo = 100
            if bullet["rect"].colliderect(rect_upg_multi_s):
                if money >= multi_cost:
                    multi_cost **= 1.1
                    multi_bullet += 2
                else:
                    not_enough = True

                bullets.remove(bullet)
                continue
                pygame.draw.circle(screen, (255, 255, 0), bullet_rect.center, ammo_rad)

                # off screen
                if not screen.get_rect().collidepoint(bullet["x"], bullet["y"]):
                    bullets.remove(bullet)
                    continue

                # enemy collision
                if scene == "game":
                    for enemy in enemys[:]:
                        dx = bullet["x"] - enemy["x"]
                        dy = bullet["y"] - enemy["y"]
                        distance = (dx ** 2 + dy ** 2) ** 0.5

                        if distance <= ammo_rad + e_rad:
                            bullets.remove(bullet)
                            enemys.remove(enemy)
                            money += 1
                            break

        if scene == "game":
            for enemy in enemys[:]:
                dx = bullet["x"] - enemy["x"]
                dy = bullet["y"] - enemy["y"]
                distance = (dx ** 2 + dy ** 2) ** 0.5

                if distance <= ammo_rad + e_rad:
                    bullets.remove(bullet)
                    enemys.remove(enemy)
                    money += 1
                    break



    pygame.display.update()

pygame.quit()
