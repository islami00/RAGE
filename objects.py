#objects###########

from pygame import image,Rect
class Character:
    def __init__(self, x=50, y=8, img=r'./Data/img/characters/Good/12x16/yola.png'):
        self.img = image.load(img)
        self.img.set_colorkey((255, 255, 255))
        self.posx = x
        self.posy = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def rect(self) -> Rect:
        return Rect(self.posx, self.posy, self.width, self.height)

    def collision(self, rect: Rect, tiles):
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def move(self, rect, movement, tiles):
        collision_types = {'top': False, 'bottom': False,
                           'right': False, 'left': False}
        rect.x += movement[0]
        hit_list = self.collision(rect, tiles)
        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
            elif movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True

        rect.y += movement[1]
        hit_list = self.collision(rect, tiles)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            elif movement[1] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True
        return rect, collision_types

    def fail(self):
        pass


class Tiles:
    # images
    dirt1 = image.load(
        r'./Data/img/tiles/16x16/dirt_0.png')
    dirt2 = image.load(
        r'./Data/img/tiles/16x16/dirt_1.png')
    grass = image.load(
        r'./Data/img/tiles/16x16/grass_0.png')
    right_grass = image.load(
        r'./Data/img/tiles/16x16/grass_r.png')
    left_grass = image.load(
        r'./Data/img/tiles/16x16/grass_l.png')
    tp_right_grass = image.load(
        r'./Data/img/tiles/12x12/grass_tp_r.png')
    tp_left_grass = image.load(
        r'./Data/img/tiles/12x12/grass_tp_l.png')
    # size
    TILE_SIZE = grass.get_width()

    # convert alpha = 0


class Background:
    def load(self,img):
        self.img=img
        return image.load(self.img)
#############