import pygame
from data.initial_city import *

class Button:
    def __init__(self):
        self.position_x = BUTTON['positon_x']
        self.position_y = BUTTON['positon_y']
        self.color =  BUTTON['color']
        self.width = BUTTON['width']
        self.height = BUTTON['height']

    def __call__(self, screen):
        pygame.draw.rect(screen, self.color, ((self.position_x, self.position_y), (self.width, self.height)))