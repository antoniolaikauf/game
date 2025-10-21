import pygame
from data.initial_city import *

class Object:
    def __init__(self, name, screen, cordinata_x, cordinata_y, camera_x, camera_y, size, color):
        self.name = name
        self.screen = screen
        self.cordinata_x = cordinata_x
        self.cordinata_y = cordinata_y
        self.camera_y = camera_y
        self.camera_x = camera_x
        # posizione assoluta ancorata al mondo  se si muove a sinistra la posizione aumenta cosi l'oggetto si sposterebbe a destra
        self.position_x = cordinata_x - camera_x
        self.position_y = cordinata_y - camera_y
        self.size = size
        self.color = color

    def draw_casa(self):
        pygame.draw.rect(self.screen, self.color, ((self.position_x, self.position_y), (self.size[0], self.size[1])))

    def draw_circle(self):
        pygame.draw.circle(self.screen, self.color, (self.position_x, self.position_y), self.size[0])
    
    def draw(self):
        if self.name == "casa":
            self.draw_casa()
        if self.name == "lago":
            self.draw_circle()