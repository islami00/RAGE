from pygame import Rect, Surface, display, draw, event, image, transform
from pygame.constants import K_F11, K_w, QUIT, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_UP
from pygame.time import Clock
from map_loader import *
from objects import *
from funcs import *
from constants import *
from utils import pathify

clock = Clock()

window = display

surface = window.set_mode(WINDOW_SIZE)
window.set_caption('Scorf')
# Init empty surface to scale from
disp = Surface(NEW_WINDOW_SIZE)

# CLASSES

# objects and constants
yola = Character()
yols_rect = yola.rect()

yols_action = 'idle'
animation_database = Animation().database()

yols_frame = 0
yols_flip = False

moving_left = False
moving_right = False

y_momentum = 0
air_timer = 0

scroll = Scroll.true_scroll

run = True
while run:

    # loops
    scroll[0] = Scroll(yols_rect).scroll_x()
    scroll[1] = Scroll(yols_rect).scroll_y()

    check_point = Rect(1994 - scroll[0], 152 - scroll[1], 16, 38)

    disp.blit(Background().load(pathify('./Data/img/bg/day_mounts.png')),
              (0 - scroll[0] / 30.00, 0 - scroll[1] / 30.0))

    draw.rect(disp, (9, 91, 85), check_point)

    if scroll[1] <= NEW_SCREEN_HEIGHT / 15:
        scroll[1] += 2

    # world creation
    tile_rects = []

    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile == '1':
                disp.blit(
                    Tiles.grass, (x * Tiles.TILE_SIZE - scroll[0], y * Tiles.TILE_SIZE - scroll[1]))
            if tile == '2':
                disp.blit(
                    Tiles.dirt1, (x * Tiles.TILE_SIZE - scroll[0], y * Tiles.TILE_SIZE - scroll[1]))
            if tile == 'L':
                disp.blit(
                    Tiles.left_grass, (x * Tiles.TILE_SIZE - scroll[0], y * Tiles.TILE_SIZE - scroll[1]))

            if tile == 'R':
                disp.blit(
                    Tiles.right_grass, (x * Tiles.TILE_SIZE - scroll[0], y * Tiles.TILE_SIZE - scroll[1]))

            if tile != '0':
                tile_rects.append(Rect(x * Tiles.TILE_SIZE, y * Tiles.TILE_SIZE,
                                       Tiles.TILE_SIZE, Tiles.TILE_SIZE))
            x += 1
        y += 1
    #############

    player_movement = [0, 0]
    if moving_right == True:
        player_movement[0] += 2
    if moving_left == True:
        player_movement[0] -= 2

    player_movement[1] += y_momentum
    y_momentum += 0.3

    if y_momentum > 4:
        y_momentum = 4

    if player_movement[0] > 0:
        yols_action, yols_frame = Animation().change_action(yols_action, yols_frame, 'run')
        yols_flip = False

    if player_movement[0] == 0:
        yols_action, yols_frame = Animation().change_action(
            yols_action, yols_frame, 'idle')

    if player_movement[0] < 0:
        yols_action, yols_frame = Animation().change_action(yols_action, yols_frame, 'run')
        yols_flip = True

    yols_rect, collisions = yola.move(yols_rect, player_movement, tile_rects)

    if collisions['bottom'] == True:
        air_timer = 0
    yols_frame += 1

    if yols_frame >= len(animation_database[yols_action]):
        yols_frame = 0

    yols_img_id = animation_database[yols_action][yols_frame]
    yola.img = animation_frames[yols_img_id]

    disp.blit(transform.flip(yola.img, yols_flip, False),
              (yols_rect.x - scroll[0], yols_rect.y - scroll[1]))

    Fail(yols_rect, 'You have failed', scroll, player_movement)

    # the game map should be generated

    for e in event.get():
        if e.type == QUIT:
            run = False
        # controller logic

        # Motion triggers
        if e.type == KEYDOWN:
            if e.key == K_RIGHT:
                moving_right = True
            if e.key == K_LEFT:
                moving_left = True
            if e.key == K_UP or e.key == K_w:
                air_timer += 1
                if air_timer <= 2:
                    y_momentum = -6
            # settings
            if e.key == K_F11:
                window.toggle_fullscreen()
        # Stop motion
        if e.type == KEYUP:
            if e.key == K_RIGHT:
                moving_right = False
            if e.key == K_LEFT:
                moving_left = False
            if e.key == K_UP:
                # let gravity do its job if up key no longer pressed
                pass

    surf = transform.scale(disp, WINDOW_SIZE)
    # Place surf on the surface at 0,0.
    surface.blit(surf, (0, 0))

    clock.tick(60)
    window.update()
