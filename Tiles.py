import pygame
import random
pygame.init()

width = 30
height = 50

screenwidth = 600
screenheight = 1200
screen = pygame.display.set_mode((screenwidth, screenheight))
bg_color=(0,0,0)

font=pygame.font.SysFont("Comic Sans MS", 30)
word_color=(0,0,0)
text="Tiles"

clock = pygame.time.Clock()
playing = True

press1 = press2 = press3 = press4 = False
keys = []

FPS = 30
spawn_rate = FPS * 1
spawn = 0

color = [0,254,0]
x = 24

speed = 4

def make_tile():
    num = random.randint(1, 4)
    if num == 1:
        x = screenwidth/2 - width*2
    elif num == 2:
        x = screenwidth/2 - width
    elif num == 3:
        x = screenwidth/2
    elif num == 4:
        x = screenwidth/2 + width

    keys.append({"x": x, "y": -height, "num": num})

def make_text(tx, ty, color, yap, size):
    fonts = pygame.font.SysFont("Comic Sans MS", size)
    text_surface = fonts.render(str(yap), True, color)
    screen.blit(text_surface, (tx, ty))

scene = "title"
score = 0
deduct = False

start = pygame.Rect(screenwidth / 2 - 37.5, screenheight / 2 - 50, 75, 50)
settings = pygame.Rect(screenwidth / 2 + 55, 55, 40, 40)
back = pygame.Rect(screenwidth/2 - 50, screenheight/2 + 100, 100, 50)

show_keys = True
big_small = 50
switch = 0

image = pygame.image.load("vector-settings-icon-removebg-preview.png").convert_alpha()
image = pygame.transform.scale(image, (50, 50))

settings_hitbox = pygame.Rect(screenwidth / 2 - 25, screenheight / 2 - 75, 50, 50)

hi_score = 0
while playing:
    if score < 0:
        score = 0
    clock.tick(FPS)
    if score > hi_score:
        hi_score = score

    speed = 4 + score * 0.05
    spawn_rate = FPS - 0.5 * score
    height = 50 - score /2
    spawn += 1
    if spawn_rate < 5:
        spawn_rate = 5
        if height < 20:
            height = 20
    if spawn >= spawn_rate:
        make_tile()
        spawn = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d: press1 = True
            if event.key == pygame.K_f: press2 = True
            if event.key == pygame.K_j: press3 = True
            if event.key == pygame.K_k: press4 = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d: press1 = False
            if event.key == pygame.K_f: press2 = False
            if event.key == pygame.K_j: press3 = False
            if event.key == pygame.K_k: press4 = False
        if  event.type == pygame.MOUSEBUTTONDOWN:
            if scene == "title":
                if start.collidepoint(event.pos):
                    scene = "play"
                if settings.collidepoint(event.pos):
                    scene = "settings"
            if scene == "end" or scene == "settings":
                if back.collidepoint(event.pos):
                    scene = "title"
            if scene == "settings":
                if settings_hitbox.collidepoint(event.pos):
                    show_keys = not show_keys

    screen.fill(bg_color)

    if scene == "title":
        pygame.draw.rect(screen, (255,255,255), start)
        make_text(screenwidth/2-35, screenheight/2-45,(0,0,0), "Start", 25)

        pygame.draw.rect(screen, (255, 255, 255), settings)

        make_text(screenwidth/2 - 10, screenheight/3,(255,255,255),str(hi_score),20)

        screen.blit(image, (screenwidth / 2 + 50, 50))
    elif scene == "play":
        if deduct:
            score -= 2
            deduct = False
        screen.blit(font.render(str(score), True, (255,255,255)), (50, 50))
        hit_zone_y = height * 10
        pygame.draw.line(screen,(255,255,255),(screenwidth / 2 - width - width - 25 ,height * 10 ),(screenwidth / 2 + width + width + 25 ,height * 10),5)

        pygame.draw.line(screen, (192, 192, 192), (screenwidth / 2 - width - width, 0), (screenwidth / 2 - width - width, screenheight),1)
        pygame.draw.line(screen, (192,192,192),(screenwidth / 2 - width, 0),(screenwidth / 2 - width, screenheight), 1)
        pygame.draw.line(screen, (192,192,192), (screenwidth / 2, 0), (screenwidth / 2, screenheight),1)
        pygame.draw.line(screen, (192,192,192), (screenwidth / 2 + width, 0), (screenwidth / 2 + width, screenheight),1)
        pygame.draw.line(screen, (192, 192, 192), (screenwidth / 2 + width + width, 0),(screenwidth / 2 + width + width, screenheight), 1)
        if show_keys:
            make_text(screenwidth / 2 - width - width / 1.5,height * 10 + 20,(255,255,255),"d", 20)
            make_text(screenwidth / 2 - width / 1.5, height * 10 + 20, (255, 255, 255), "f", 20)
            make_text(screenwidth / 2 + width + width / 2.8, height * 10 + 20, (255, 255, 255), "k", 20)
            make_text(screenwidth / 2 + width / 2.8, height * 10 + 20, (255, 255, 255), "j", 20)

        lane_tiles1 = [k for k in keys if k["num"] == 1]
        closest1 = min(lane_tiles1, key=lambda k: abs((k["y"] + height / 2) - hit_zone_y), default=None)

        lane_tiles2 = [k for k in keys if k["num"] == 2]
        closest2 = min(lane_tiles2, key=lambda k: abs((k["y"] + height / 2) - hit_zone_y), default=None)

        lane_tiles3 = [k for k in keys if k["num"] == 3]
        closest3 = min(lane_tiles3, key=lambda k: abs((k["y"] + height / 2) - hit_zone_y), default=None)

        lane_tiles4 = [k for k in keys if k["num"] == 4]
        closest4 = min(lane_tiles4, key=lambda k: abs((k["y"] + height / 2) - hit_zone_y), default=None)

        for key in keys[:]:
            key["y"] += speed
            pygame.draw.rect(screen, (255,255,255),
            pygame.Rect(key["x"], key["y"], width, height))
            inz = hit_zone_y - height <= key["y"] + height / 2 <= hit_zone_y + height

            if key["num"] == 1 and press1:
                if inz:
                    keys.remove(key)
                    score += 1
                else:
                    if closest1:
                        deduct = True
                press1 = False
            elif key["num"] == 2 and press2:
                if inz:
                    keys.remove(key)
                    score += 1
                else:
                    if closest2:
                        deduct = True
                press2 = False
            elif key["num"] == 3 and press3:
                if inz:
                    keys.remove(key)
                    score += 1
                else:
                    if closest3:
                        deduct = True
                press3 = False
            elif key["num"] == 4 and press4:
                if inz:
                    keys.remove(key)
                    score += 1
                else:
                    if closest4:
                        deduct = True
                press4 = False
            elif key["y"] > screenheight:
                scene = "end"
    elif scene == "end":
        pygame.draw.rect(screen, (255, 255, 255), back)
        make_text(screenwidth / 2 - 50, screenheight / 2 + 100, (0, 0, 0), "Back", 25)
        make_text(screenwidth /2 - big_small/2.6 ,screenheight / 2 - big_small /2,(255,255,255),str(score),big_small)
        for key in keys:
            keys.remove(key)
        if switch == 0:
            big_small -= 1
            if big_small < 30:
                switch = 1
        elif switch == 1:
            big_small += 1
            if big_small > 50:
                switch = 0

    elif scene == "settings":
        if show_keys:
            if color[1] < 255:
                color[1] += 10
                if color[1] > 255:
                    color[1] = 255
            if color[0] > 0:
                color[0] -= 10
                if color[0] < 0:
                    color[0] = 0

            if x < 24:
                x += 2
        else:
            if color[0] < 255:
                color[0] += 10
                if color[0] > 255:
                    color[0] = 255
            if color[1] > 0:
                color[1] -= 10
                if color[1] < 0:
                    color[1] = 0

            if x > -24:
                x -= 2

        pygame.draw.rect(screen, (255, 255, 255), back)
        make_text(screenwidth / 2 - 50, screenheight / 2 + 100, (0, 0, 0), "Back", 25)

        make_text(screenwidth/2-50,screenheight/2 - 115, (255,255, 255),"Show keys",20)
        pygame.draw.circle(screen, (255, 255, 255), (screenwidth / 2 - 25, screenheight / 2 - 50), 25, 0)
        pygame.draw.circle(screen, (255, 255, 255), (screenwidth / 2 + 25, screenheight / 2 - 50), 25, 0)
        pygame.draw.rect(screen, (255, 255, 255), settings_hitbox)
        pygame.draw.circle(screen, (color[0], color[1], color[2]), (screenwidth / 2 - 25, screenheight / 2 - 49.5), 20, 0)
        pygame.draw.circle(screen, (color[0], color[1], color[2]), (screenwidth / 2 + 25, screenheight / 2 - 49.5), 20, 0)
        pygame.draw.rect(screen, (color[0], color[1], color[2]), pygame.Rect(screenwidth / 2 - 27.5, screenheight / 2 - 69.5, 50, 40))
        pygame.draw.circle(screen, (0, 0, 0), (screenwidth / 2 + x, screenheight / 2 - 49), 23, 0)
        pygame.draw.circle(screen, (255,255,255), (screenwidth / 2 + x, screenheight / 2 - 49), 20, 0)

    pygame.display.update()

pygame.quit()
