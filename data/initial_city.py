import numpy as np

WIDTH = 1200
HEIGHT = 720
NERO = (0, 0, 0)
AZZURRO = (59, 204, 247)
GRIGIO = (131, 140, 142)
VERDE = (0, 143, 57)

BUTTON = {
    'positon_x' : 20,
    'positon_y' : 20,
    'color': VERDE,
    'width': 100,
    'height': 50,
    'radius': 10,
    'font': 20,
    'text' : "ok",
}

CORDINATE = np.random.randint((WIDTH // 2), size=(5,2))
OBJECT_BASE = ["casa", "casa", "casa", "lago", "casa" ]