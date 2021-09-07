import os
import os.path as path
from utils import pathify

class MapLoader:
    def load_map(self,path_=pathify('./Data/Maps/level1.txt')):
        with open(path_,'r') as lvl1:
            _data=lvl1.read()
            data=_data.split('\n')
            game_map=[]
            for row in data:
                game_map.append(list(row))

        return game_map

map_=MapLoader()
game_map=map_.load_map()


