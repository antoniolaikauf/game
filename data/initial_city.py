import numpy as np
import copy

WIDTH = 1200
HEIGHT = 720
NERO = (0, 0, 0)
AZZURRO = (50, 150, 200)
GRIGIO = (131, 140, 142)
BLU = (0, 128, 255)  # Blu
BLU_OVER = (0, 200, 255)   # Blu più chiaro per il passaggio del mouse
VERDE_OVER = (80, 200, 120)
VERDE = (0, 128, 0)
SIZE_HOME = [20, 20]
SIZE_LAKE = [30]

BUTTON = {
    'positon_x' : 20,
    'positon_y' : 20,
    'color_not_over': BLU,
    'color_over':BLU_OVER,
    'width': 100,
    'height': 50,
    'radius': 10,
    'font': 20,
}

MENU = {
    'positon_x' : 20,
    'positon_y' : 20,
    'color_not_over': BLU,
    'color_over':BLU_OVER,
    'width': 150,
    'height': 400,
    'radius': 10,
    'font': 20,
    'tag' : ['casa', 'lago', 'ciaosa'],
}

BUTTON_OBJECT = {
    'positon_x' : 25,
    'positon_y' : 20,
    'color_not_over': VERDE,
    'color_over':VERDE_OVER,
    'width': 100,
    'height': 50,
    'radius': 10,
    'font': 20,
}

CORDINATE = np.random.randint((WIDTH // 2), size=(5,2))
CORDINATE_UPDATE = copy.deepcopy(CORDINATE)
OBJECT_BASE = [
    {
        'name':'casa',
        'size':SIZE_HOME,
        'color':GRIGIO
    },
    {
        'name':'casa',
        'size':SIZE_HOME,
        'color':GRIGIO,
    },
    {
        'name':'casa',
        'size':SIZE_HOME,
        'color':GRIGIO,
    },
    {
        'name':'lago',
        'size':SIZE_LAKE,
        'color':AZZURRO
    },
    {
        'name':'casa',
        'size':SIZE_HOME,
        'color':GRIGIO
    }
]
