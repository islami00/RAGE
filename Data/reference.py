import pygame
from pygame import Rect, Surface, display, event, sprite, image, key, transform
from pygame import draw
from pygame.constants import KEYDOWN, KEYUP, K_UP, QUIT, K_LEFT, K_RIGHT
from map_loader import game_map
from pygame.time import Clock
from utils import pathify

clock = Clock()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
NEW_SCREEN_WIDTH = SCREEN_WIDTH-600
NEW_SCREEN_HEIGHT = SCREEN_HEIGHT-300

WINDOW_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT
NEW_WINDOW_SIZE = NEW_SCREEN_WIDTH, NEW_SCREEN_HEIGHT

window = display
surface = window.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

_display = Surface((NEW_SCREEN_WIDTH, NEW_SCREEN_HEIGHT))

grass = image.load(pathify('./img/tiles/12x12/grass_0.png'))
dirt = image.load(pathify('./img/tiles/12x12/dirt_0.png'))


TILE_SIZE = grass.get_width()



class Character(Rect, sprite.Sprite):
    def __init__(self, img=pathify('./img/tiles/12x12/grass_0.png'), x=100, y=8) -> Rect:
        self.img = image.load(img)
        self.img.set_colorkey((255, 255, 255))
        self.height = self.img.get_height()
        self.width = self.img.get_width()
        self.posx = x
        self.posy = y
        self.y_momentum = 0

    def move(self, direction='', speed=1):
        self.direction = direction
        self.speed = speed

        if direction == 'left':
            self.posx -= self.speed
        elif direction == 'right':
            self.posx += self.speed
        elif direction == 'up':
            self.posy -= self.speed
        else:
            self.y_momentum -= 1
            self.posy += self.y_momentum
            if self.y_momentum > -5:
                self.y_momentum = 5

    fall = move

    def show(self, surf):
        surf.blit(self.img, (self.posx, self.posy))


def collision(rect: Rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


def movement_(rect: Rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False,
                       'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True

    rect.y += movement[1]
    hit_list = collision(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types


yols = Character()


# for collision function access (not visible)
yols_rect = Rect(yols.posx, yols.posy, yols.width, yols.height)
moving_right = False
moving_left = False
air_timer = 0
y_momentum = 0

#scroll values
true_scroll = [0, 0]


run = True
while run:
    _display.fill((120, 190, 255))

    true_scroll[0]+=(yols_rect.x-true_scroll[0]-252)/20
    true_scroll[1]+=(yols_rect.y-true_scroll[1]-100)/40
    scroll=true_scroll.copy()

    scroll[0]=int(scroll[0])
    scroll[1]=int(scroll[1])

    tile_rects = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile == '1':
                _display.blit(grass, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile == '2':
                _display.blit(dirt, (x*TILE_SIZE-scroll[0], y*TILE_SIZE-scroll[1]))
            if tile != '0':
                tile_rects.append(
                    Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1

    player_movement = [0, 0]
    if moving_right == True:
        player_movement[0] += 7
    if moving_left == True:
        player_movement[0] -= 7

    player_movement[1] += y_momentum
    y_momentum += 1

    if y_momentum > 10:
        y_momentum = 10

    yols_rect, collisions = movement_(yols_rect, player_movement, tile_rects)

    if collisions['bottom'] == True:
        air_timer = 0
    else:
        air_timer += 1
    
    
    _display.blit(yols.img, (yols_rect.x-scroll[0], yols_rect.y-scroll[1]))
    

    for e in event.get():
        if e.type == QUIT:
            run = False

        if e.type == KEYDOWN:
            if e.key == K_RIGHT:
                moving_right = True
            if e.key == K_LEFT:
                moving_left = True
            if e.key == K_UP:
                if air_timer < 6:
                    y_momentum = -18

        if e.type == KEYUP:
            if e.key == K_RIGHT:
                moving_right = False
            if e.key == K_LEFT:
                moving_left = False
            if e.key == K_UP:
                pass

    surf = transform.scale(_display, WINDOW_SIZE)
    surface.blit(surf, (0, 0))


    window.update()
