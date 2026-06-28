import pygame
import os

pygame.init()


# screen size
screenwidth = 1920  #1920 / 960 / 480
screenheight = 1040 #1040 / 520 / 260
screen = pygame.display.set_mode((screenwidth, screenheight))

BASE_W = 1920
BASE_H = 1040



#Monkey/Hitboxes

projectile_box = []
monkey_box = []
map_completion_data = [{"name": "Monkey Meadow", "completion": 10000000000000}]

image = []
buttons = []
map_buttons = []



def sx(x):
    return x / BASE_W * screenwidth
def sy(y):
    return y / BASE_H * screenheight
def make_image(x, y, image_name, parent, width = None, height = None):

    path = os.path.join("Random Games","BTD6","Assets", parent, f"{image_name}.webp")
    imgs = pygame.image.load(path)

    if width is None or height is None:
        x -= imgs.get_size()[0] / 2
        y -= imgs.get_size()[1] / 2
    else:
        imgs = pygame.transform.scale(imgs, (sx(int(width)), sy(int(height))))
        x -= width / 2
        y -= height / 2
    x = sx(x)
    y = sy(y)
    screen.blit(imgs, (x, y))
def make_text(x, y, color, yap, size):
    size = int(round(sy(size)))
    font = pygame.font.SysFont("Comic Sans MS", size)
    text_surface = font.render(str(yap), False, color)

    text_rect = text_surface.get_rect(center=(sx(x), sy(y)))
    screen.blit(text_surface, text_rect)
def make_rect(tx, ty, color, width, height):
    rect = pygame.Rect(sx(tx - width / 2), sy(ty - height / 2), sx(width), sy(height))
    if color != -1:
        pygame.draw.rect(screen, color, rect)
    return rect
def make_button(x, y, box_color, width, height, inside_border, border_color, tx, ty, tcolor, yap, size, destination, scene_in, is_it_border_percentage = None):
    button_made = make_rect(x, y, box_color, width, height)

    if inside_border > 0:
        if is_it_border_percentage is None:
            shrink_x = button_made.width * inside_border / 100
            shrink_y = button_made.height * inside_border / 100
            inner = button_made.inflate(-shrink_x, -shrink_y)
        else:
            inner = button_made.inflate(-inside_border, -inside_border)

        pygame.draw.rect(screen, border_color if border_color != 0 else (0, 0, 0), inner)

    make_text(x + tx, y + ty, tcolor, yap, size)
    buttons.append({"button":button_made, "destination": destination, "scene": scene_in})
def make_map(row, column, name, width = None, height = None):
    x = 480 * column
    if row == 1:
        y = 223
    else:
        y = 594

    if width is None or height is None:
        button_made = make_rect(x, y, -1, 400, 300)
    else:
        button_made = make_rect(x - width, y - height, -1, 400, 300)

    pygame.draw.rect(screen, (0, 0, 0), button_made)
    pygame.draw.rect(screen, (50, 255, 50), button_made.inflate(-20, -20))
    make_image(x, y - 6, name, "Maps", 370, 250)
    make_text(x, y - 170, (0, 0, 0), name, 40)
    map_buttons.append({"name": name, "button": button_made})
    for i in map_completion_data:
        if i["name"] == name:
            if i["completion"] >= 10000000000000:
                make_image(x - 100, y + 100, "Easy Badge", "Badges")
            else:
                make_image(x - 50, y + 100, "Empty", "Badges", 30, 30)


scene = "title"
prev_scene = "title"
level_type = ""
level_screen = 1
prev_level_screen = 1
monkey_money = 0
money = 0

clock = pygame.time.Clock()
playing = True

##

fps = 60
loading_screen = True
freeze_timer = fps
freeze_timer_original = freeze_timer
freeze_timer = 0
while playing:
    screen.fill((200, 255, 200))
    clock.tick(fps)
    if loading_screen:
        if prev_scene != scene:
            freeze_timer = freeze_timer_original
            prev_scene = scene
        if prev_level_screen != level_screen:
            freeze_timer = freeze_timer_original / 2
            prev_level_screen = level_screen
        if freeze_timer > 0:
            freeze_timer -= 1
            screen.fill((0, 0, 0))
            make_text(960, 520, (255, 255, 255), "Loading", 30)
            pygame.display.update()
            continue

    if scene == "title":
        make_button(960, 520, (0, 0, 0), 200, 150, 10, (50, 255, 50), 0, 0, (0, 0, 0), "Play",  50, "level_select","title")
        make_button(1280,520, (0, 0, 0), 200, 150, 10, (50, 255, 50), 0, 0, (0, 0, 0), "Monkeys",40, "index", "title")
        make_button(640, 520, (0, 0, 0), 200, 150, 10, (50, 255, 50), 0, 0, (0, 0, 0), "Heros", 50, "heros", "title")
        make_button(1820, 100, (0, 0, 0), 100, 100, 15, (0, 255, 0), 0, 0, (0, 0, 0), "Load", 30, "load", "title")
        make_button(1820, 250, (0, 0, 0), 100, 100, 15, (255, 0, 0), 0, 0, (0, 0, 0), "Save", 30, "save", "title")
        make_button(200, 250, (0, 0, 0), 150, 150, 15, (255, 0, 0), 0, 0, (0, 0, 0), "", 30, "settings", "title")
        make_image(200, 250, "Settings", "Other", 150, 150)
    elif scene == "level_select":
        make_text(125, 50, (0, 0, 0), "You can only have", 30)
        make_text(125, 75, (0, 0, 0), "one save file at!", 30)
        make_text(125, 100, (0, 0, 0), "a time!", 30)

        make_button(1845, 520, (0, 0, 0), 100, 100, 33, (255, 255, 255), 0, 0, (50, 255, 50), "Next", 25, "level_select", "level_select")

        if level_type == "beginner":

            if level_screen >= 6:
                level_screen = 1
                prev_level_screen = level_screen

            if level_screen == 1:
                make_map(1, 1, "Monkey Meadow")
                make_map(1, 2, "In the Loop")
                make_map(1, 3, "Tree Stump")
                make_map(2, 1, "Middle of the Road")
                make_map(2, 2, "Town Center")
                make_map(2, 3, "One Two Tree")

    elif scene == "index":
        pass

    elif scene == "load":
        pass

    elif scene == "save":
        pass

    elif scene == "heros":
        pass
    elif scene == "settings":
        pass

    else:
        make_image(520,960, scene, "Maps", 1040, 1920)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if scene == "title":
                for button in buttons:
                    if button["scene"] == "title":
                        if button["button"].collidepoint(event.pos):
                            scene = button["destination"]
                        if button["destination"] == "level_select":
                            level_screen = 1
                            level_type = "beginner"



            elif scene == "level_select":
                for map_data in map_buttons:
                    if map_data["button"].collidepoint(event.pos):
                        scene = map_data["name"]

                for button in buttons:
                    if button["scene"] == "level_select":
                        if button["button"].collidepoint(event.pos):
                            if button["destination"] == "level_select" and prev_level_screen == level_screen:
                                level_screen += 1
                            else:
                                scene = button["destination"]


    pygame.display.update()

pygame.quit()