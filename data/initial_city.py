import numpy as np
import copy

WIDTH = 1200
HEIGHT = 720

NERO = (0, 0, 0)
RED = (217, 33, 33)
AZZURRO = (50, 150, 200)
GRIGIO = (131, 140, 142)
BLU = (0, 128, 255)  # Blu
BLU_OVER = (0, 200, 255)   # Blu più chiaro per il passaggio del mouse
VERDE_OVER = (80, 200, 120)
VERDE = (0, 128, 0)
BIANCO = (255, 255, 255)
VERDE_SCURO = (1, 50 , 32)
MARRONE = (101, 67, 33)
ROSA = (255, 192, 203)
GIALLO_SPENTO = (230, 255, 108)

SIZE_HOME = [20, 20]
SIZE_LAKE = [30]
SIZE_MANUFACTURIES = [30, 20]
SIZE_ROAD = [100, 35]
SIZE_FOREST = [100, 100]

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
    'tag' : ['home', 'road', 'industria', 'lake'], 
}

BUTTON_OBJECT = {
    'positon_x' : 25,
    'positon_y' : 20,
    'color_not_over': VERDE,
    'color_over':VERDE_OVER,
    'width': 140,
    'height': 50,
    'radius': 10,
    'font': 20,
}

CORDINATE = np.random.randint((WIDTH // 2), size=(1,2))
CORDINATE_UPDATE = copy.deepcopy(CORDINATE)
OBJECT_BASE = [
    {
        'name':'home',
        'size':SIZE_HOME,
        'color':RED
    },
    # {
    #     'name':'manufacturing',
    #     'size':SIZE_MANUFACTURIES,
    #     'color':GRIGIO,
    # },
    # {
    #     'name':'forest',
    #     'size':SIZE_FOREST,
    #     'color':VERDE,
    # },
    {
        'name':'lake',
        'size':SIZE_LAKE,
        'color':AZZURRO
    },
    # {
    #     'name':'road', 
    #     'size':SIZE_ROAD,
    #     'color':NERO
    # }
]

CORDINATE_PERSON = np.random.randint(WIDTH // 2, size=(5,2))
PERSON_BASE = [
    {
        'name':'farmer'
    },
    {
        'name':'miner',
    },
    {
        'name':'citizen',
    },
    {
        'name':'miner',
    },
    {
        'name':'citizen',
    }
]