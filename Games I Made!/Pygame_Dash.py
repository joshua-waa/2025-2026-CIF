import pygame

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
# screen size
screenwidth = 800
screenheight = 600
screen = pygame.display.set_mode((screenwidth, screenheight))
bg_color = (0, 100, 255)

font = pygame.font.SysFont("Comic Sans MS", 30)
word_color = (255, 255, 255)
text = "Play"  ###################################################

clock = pygame.time.Clock()
playing = True

lv = 1
start = False
ingame = False


list1 = []

x = 200
y = screenheight / 2 + 25
v = 0


def make_text(tx, ty, color, yap, size):
    font1 = pygame.font.SysFont("Comic Sans MS", size)
    text_surface = font1.render(str(yap), True, color)
    screen.blit(text_surface, (tx, ty))


def make_block(length, height, b_or_s, what_lv):
    if b_or_s == "block":
        what_lv.append({"l": length * 45 + x, "h": -height * 45 + screenheight / 2 + 25, "block/spike": b_or_s})
    else:
        what_lv.append({"l": length * 45 + x, "h": (-height+2) * 45 + screenheight / 2 + 23, "block/spike": b_or_s})


def level_one():
    make_block(15, 0, "spike", list1)
    make_block(25, 0, "spike", list1)
    make_block(26, 0, "spike", list1)
    make_block(43, 0, "spike", list1)
    make_block(44, 0, "spike", list1)
    make_block(45, 0, "block", list1)
    make_block(46, 0, "spike", list1)
    make_block(47, 0, "spike", list1)
    make_block(48, 0, "spike", list1)
    make_block(49, 0, "block", list1)
    make_block(49, 1, "block", list1)
    make_block(50, 0, "spike", list1)
    make_block(51, 0, "spike", list1)
    make_block(52, 0, "spike", list1)
    make_block(53, 0, "block", list1)
    make_block(53, 1, "block", list1)
    make_block(53, 2, "block", list1)
    make_block(62, 0, "spike", list1)
    make_block(63, 0, "spike", list1)
    make_block(69, 0, "block", list1)
    make_block(70, 0, "block", list1)
    make_block(71, 0, "block", list1)
    make_block(72, 0, "block", list1)
    make_block(73, 0, "block", list1)
    make_block(74, 0, "spike", list1)
    make_block(75, 0, "spike", list1)
    make_block(76, 0, "block", list1)
    make_block(77, 0, "block", list1)
    make_block(78, 0, "block", list1)
    make_block(79, 0, "block", list1)
play = pygame.Rect((screenwidth - 100) / 2 + 23, (screenheight - 100) / 2 - 20, 100, 100)
image = pygame.image.load("arrow (2).png").convert_alpha()
image = pygame.transform.scale(image, (100, 100))

lv1 = pygame.Rect((800 - 525) / 2, (600 - 300) / 2, 525, 300)

fps = 30
touch = 0
press =False
touching = False

ground = screenheight / 2 + 45

speed = 400  ###400 normal
jump = 20
g = 2.5
landed = False
mode = "square"

delay = 0
while playing:
    if v < -20:
        v = -20

    prev_y = y
    touching = False
    clock.tick(fps)  # FPS
    screen.fill(bg_color)  # background color

    touch -= 1
    if touch <= 0:
        touching = False
    else:
        touching = True

    if y >= screenheight / 2 + 25 and not landed:
        y = screenheight / 2 + 25
        v = 0
        touching = True


    delay -= 1
    if delay > 0:
        touching = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            press = True
            if mode == "square":
                if touching:
                    v = jump
                    touching = False
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_UP, pygame.K_SPACE):
                press = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if play.collidepoint(event.pos) and not start:
                lv = 1
                start = True

            elif lv1.collidepoint(event.pos) and start and lv == 1 and not ingame:
                list1.clear()
                v = 0
                y = screenheight / 2
                ingame = True

                level_one()

    if not start:
        pygame.draw.rect(screen, (0, 100, 255), play)
        screen.blit(image, (screenwidth / 2 - 25, screenheight / 2 - 70))

    elif start:
        if ingame:
            y -= v
            rect = pygame.Rect(x, y, 45, 45)
            if mode == "square":
                pygame.draw.rect(screen, (0, 255, 0), rect)  # draw box
                pygame.draw.rect(screen, bg_color, pygame.Rect(x + 7 , y + 7, 31, 31))
                pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(x + 15, y + 15, 15, 15))

                v -= g


                if y >= ground or y >= screenheight / 2 + 45:
                    y = ground
                    v = 0

        if lv == 1:
            if ingame:
                for block in list1:
                    block["l"] -= speed / fps
                    if block["block/spike"] == "block":

                        pygame.draw.rect(screen, black, pygame.Rect(block["l"], block["h"], 45, 45))
                        pygame.draw.rect(screen, white, pygame.Rect(block["l"] + 3, block["h"] + 3, 39, 39))
                        block_rect = pygame.Rect(block["l"], block["h"], 45, 45)

                        if rect.colliderect(block_rect):
                            if prev_y + 45 <= block_rect.top:
                                y = block_rect.top - 45
                                v = 0
                                touching = True
                                touch = fps / 5
                                delay = 3
                            else:
                                v = 0
                                ingame = False



                    elif block["block/spike"] == "spike":
                        spike_rect = pygame.Rect(block["l"] + 16, block["h"] + 15 - 90, 15, 20)
                        pygame.draw.polygon(screen, white, ((block["l"] + 22.5, block["h"] - 90), (block["l"], block["h"] - 45),(block["l"] + 45, block["h"] - 45)), 0)
                        pygame.draw.polygon(screen, black, ((block["l"] + 22.5, block["h"] - 90), (block["l"], block["h"] - 45),(block["l"] + 45, block["h"] - 45)), 3)
                        if spike_rect.colliderect(rect):
                            lv = 1
                            ingame = False

                    elif block["block/spike"] == "uspike":
                        spike_rect = pygame.Rect(block["l"] + 16, block["h"] + 15 - 90, 15, 20)
                        pygame.draw.polygon(screen, white, ((block["l"] + 22.5, block["h"]-90), (block["l"], block["h"] -45),(block["l"] - 22.5 , block["h"]-90)), 0)
                        pygame.draw.polygon(screen, black, ((block["l"] + 22.5, block["h"]-90), (block["l"], block["h"] -45) ,(block["l"] - 22.5, block["h"]-90)), 3)
                        if spike_rect.colliderect(rect):
                            lv = 1
                            ingame = False
            else:
                pygame.draw.rect(screen, (0, 255, 0), lv1)
                make_text((800 - 50) / 2, (600 - 300) / 2, black, "Lv1", 40)
                list1.clear()

    pygame.display.update()

pygame.quit()
