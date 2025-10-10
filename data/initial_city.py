import numpy as np

WIDTH = 1200
HEIGHT = 720
NERO = (0, 0, 0)
AZZURRO = (50, 150, 200)
GRIGIO = (131, 140, 142)
BLU = (0, 128, 255)  # Blu
BLU_OVER = (0, 200, 255)   # Blu più chiaro per il passaggio del mouse

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
    'tag' : ['casa', 'lago'],
    'render': False
}

BUTTON_OBJECT = {
    'positon_x' : 20,
    'positon_y' : 20,
    'color_not_over': BLU,
    'color_over':BLU_OVER,
    'width': 100,
    'height': 50,
    'radius': 10,
    'font': 20,
}

CORDINATE = np.random.randint((WIDTH // 2), size=(5,2))
OBJECT_BASE = ["casa", "casa", "casa", "lago", "casa" ]