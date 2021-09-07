from pygame import image, Rect
from constants import*
from utils import pathify
#functions#########
animation_frames = {}

class Animation:
    def load(self, path, frame_duration):
        animation_name = path.split(f'{pathSep}')[-1]
        frame_data = []
        n = 1
        for frame in frame_duration:
            animation_frame_id = animation_name + '_' + str(n)
            img_loc = path + f'{pathSep}' + animation_frame_id + '.png'
            self.animation_img = image.load(img_loc)
            animation_frames[animation_frame_id] = self.animation_img.copy(
            )

            for i in range(frame):
                frame_data.append(animation_frame_id)
            n += i

        return frame_data

    def database(self):
        database = {}

        database['run'] = self.load(
            pathify('./Data/img/characters/Good/12x16/Animation/run'), [1, 2, 40])
        database['idle'] = self.load(
            pathify('./Data/img/characters/Good/12x16/Animation/idle'), [1, 2, 40])
        return database

    def change_action(self, action_old, frame, new_value):
        if action_old != new_value:
            action_old = new_value
            frame = 0
        return action_old, frame


class Scroll:
    true_scroll = [0, 0]

    def __init__(self, rect: Rect) -> None:
        self.true_scroll[0] += (rect.x-self.true_scroll[0]-100)/20
        self.true_scroll[1] += (rect.y-self.true_scroll[1]-70)/40
        self.scroll = self.true_scroll.copy()

        self.scroll[0] = int(self.scroll[0])
        self.scroll[1] = int(self.scroll[1])

    def scroll_x(self):
        return self.true_scroll[0]

    def scroll_y(self):
        return self.true_scroll[1]


class Fail:
    def __init__(self, player: Rect, message='', scroll=[0, 0], momentum=[0,0]) -> None:
        self.player = player
        self.message = message
        self.scroll = scroll
        self.momentum = momentum

        if self.player.y > SCREEN_HEIGHT-scroll[1]/4:
            print(self.message)
            self.momentum[1]=0
            self.player.y


##############
