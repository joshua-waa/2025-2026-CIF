import pygame
from pygame import MOUSEBUTTONDOWN
import random
pygame.init()
pygame.mixer.init()
# screen size
screenwidth = 500
screenheight = 800
screen = pygame.display.set_mode((screenwidth, screenheight))
bg_color=(0,0,0)

def make_text(tx, ty, color, yap, size):
    fonts = pygame.font.SysFont("Comic Sans MS", size)
    text_surface = fonts.render(str(yap), True, color)
    screen.blit(text_surface, (tx, ty))

audio_file = "SpotiDown.App - Sugar - Maroon 5.mp3"
pygame.mixer.music.load(audio_file)
scene = "title"
FPS = 30

non_moving = []
moving = []

clock = pygame.time.Clock()
start = pygame.Rect(screenwidth/2 - 50,screenheight/2,100,50)

score = 0
hi_score = 0

def make_cir():
    x = random.randint(75, screenwidth-75)
    y = random.randint(75, screenheight-75)
    new_moving = {"x": x, "y": y, "size": 80, "color":[255,0,0], "color_change": 0, "d?":0}
    moving.append(new_moving)
    non_moving.append({"x": x, "y": y, "moving_ref": new_moving, "size": 40})
nt = 10
ns = 35 #Try to get 1:2  ns:ms
ms = 70

spawn_time = 0.499 ######
cir_ps = FPS * spawn_time # spawn per . . s
timer = 0

s_to_go_green = 0.75 #############
speed = s_to_go_green * FPS  ### . .s to go to green
clicked = False

mx = my = 0

t_from_start = 0
while True:
    if score > hi_score:
        hi_score = score
    clock.tick(30)
    screen.fill(bg_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            if scene == "title":
                if start.collidepoint(event.pos):
                    scene = "game"
                    clicked = True
                    moving.clear()
                    non_moving.clear()
                    pygame.time.delay(500)
                    pygame.mixer.music.play(-1)

                    continue
            elif scene == "game":
                mx, my = event.pos
                for cir in non_moving[:]:
                    distance_sq = (mx - cir["x"]) ** 2 + (my - cir["y"]) ** 2
                    hit_radius = cir["size"]
                    if distance_sq <= hit_radius ** 2:
                        moving_cir = cir["moving_ref"]
                        if ns - nt/2-2 <= moving_cir["size"] <= ns + nt/2+2:
                            score += 1
                            moving_cir["d?"] = 1
                            non_moving.remove(cir)
                            break

    if scene == "title":
        pygame.draw.rect(screen,(255,255,255),start)
        make_text(screenwidth / 2 - 45, screenheight / 2 -5 , (0, 0, 0), "Osu!", 45)
        make_text(screenwidth / 2 - 20 , screenheight / 2 - 100, (255,255,255), hi_score, 45)
    if scene == "game":
        print(score)
        timer += 1
        if timer > cir_ps:
            make_cir()
            timer = 0
        #spawning

        for cir in non_moving[:]:
            if cir["moving_ref"]["size"] < 5:
                non_moving.remove(cir)
            else:
                pygame.draw.circle(screen, (255, 255, 255), (cir["x"], cir["y"]), int(cir["size"]), nt)
        for cir in moving[:]:
            if cir["d?"] == 1:
                moving.remove(cir)
            else:
                    cir["size"] -= (ms - ns) / speed
                    if cir["size"] <= 0:
                        score-=2
                        moving.remove(cir)
                    if cir["color_change"] == 0:
                        cir["color"][0] = max(0, cir["color"][0] - 255 / speed)
                        cir["color"][1] = min(255, cir["color"][1] + 255 / speed)
                    elif cir["color_change"] == 1:
                        cir["color"][1] = max(0, cir["color"][1] - 255 / speed)
                        cir["color"][0] = min(255, cir["color"][0] + 255 / speed)
                    if cir["color"][0] <= 0:
                        cir["color_change"] = 1
                    pygame.draw.circle(screen, cir["color"], (cir["x"], cir["y"]), int(cir["size"]), 3)

        if not clicked:
            score -= 1

        t_from_start += 0.001 / FPS
        if t_from_start > 234:
            pygame.time.delay(1000)
            scene = "title"
            timer = 0
            score = 0
            pygame.mixer.music.stop()
    pygame.display.update()
