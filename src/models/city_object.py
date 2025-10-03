import pygame
import random
from data.initial_city import *

class Object:
    def __init__(self, name, screen, cordinata_x, cordinata_y, camera_x, camera_y):
        self.name = name
        self.screen = screen
        self.cordinata_x = cordinata_x
        self.cordinata_y = cordinata_y
        self.camera_y = camera_y
        self.camera_x = camera_x
        # posizione assoluta ancorata al mondo  se si muove a sinistra la posizione aumenta cosi l'oggetto si sposterebbe a destra
        self.position_x = cordinata_x - camera_x
        self.position_y = cordinata_y - camera_y

    def draw_casa(self):
        pygame.draw.rect(self.screen, GRIGIO, ((self.position_x, self.position_y), (20, 20)))

    def draw_circle(self):
        pygame.draw.circle(self.screen, AZZURRO, (self.position_x, self.position_y), 30)
    
    def draw(self):
        if self.name == "casa":
            self.draw_casa()
        if self.name == "lago":
            self.draw_circle()