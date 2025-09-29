import pygame
import random
from data.initial_city import *

class Object:
    def __init__(self, name, screen, cordinata_x, cordinata_y):
        self.name = name
        self.screen = screen
        self.cordinata_x = cordinata_x
        self.cordinata_y = cordinata_y

    def draw_casa(self):
        pass

    def draw_circle(self):
        pygame.draw.circle(self.screen, NERO, (self.cordinata_x, self.cordinata_y), 10)
    
    def draw(self):
        if self.name == "casa":
            self.draw_casa()
        if self.name == "circle":
            self.draw_circle()