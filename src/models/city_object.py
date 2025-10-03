import pygame
import random
from data.initial_city import *

class Object:
    def __init__(self, name, screen, cordinata_x, cordinata_y, camera_x, camera_y):
        self.name = name
        self.screen = screen
        self.cordinata_x = cordinata_x
        self.cordinata_y = cordinata_y

    def draw_casa(self, camera_x, camera_y):
        position_

    def draw_circle(self, camera_x, camera_y):
        # posizione assoluta ancorata al mondo  se si muove a sinistra la posizione aumenta cosi l'oggetto si sposterebbe a destra
        position_x = self.cordinata_x - camera_x
        position_y = self.cordinata_y - camera_y
        # print(f"self.cordinata_x --> {self.cordinata_x}, self.cordinata_y --> {self.cordinata_y}")
        pygame.draw.circle(self.screen, NERO, (position_x, position_y), 10)
    
    def draw(self, camera_x, camera_y):
        if self.name == "casa":
            self.draw_casa(camera_x, camera_y)
        if self.name == "circle":
            self.draw_circle(camera_x, camera_y)