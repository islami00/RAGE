import os

def pathify(path : str):
    paths = path.split('/')
    init = ''
    for path in paths:
        init = os.path.join(init,path)
    return init
