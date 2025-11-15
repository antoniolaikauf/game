import pygame
from data.initial_city import *
from ..controllers.helpers import get_center
import random
from threading import Timer

class Object:
    def __init__(self, name, screen, cordinata_x, cordinata_y, camera_x, camera_y, size, color):
        self.name = name
        self.screen = screen
        self.cordinata_x = cordinata_x
        self.cordinata_y = cordinata_y
        # posizione assoluta ancorata al mondo se si muove a sinistra la posizione aumenta cosi l'oggetto si sposterebbe a destra
        self.position_x = 0
        self.position_y = 0
        self.size = size
        self.color = color

    def draw_casa(self):
        pygame.draw.rect(self.screen, self.color, ((self.position_x, self.position_y), (self.size[0], self.size[1])))
        pygame.draw.polygon(self.screen, GRIGIO, 
                    ((self.position_x, self.position_y), (self.position_x + self.size[0], self.position_y),
                     (self.position_x + self.size[0] // 2, self.position_y - self.size[0] // 2)))

    def draw_circle(self):
        pygame.draw.circle(self.screen, self.color, (self.position_x, self.position_y), self.size[0])
    
    def draw_manufacturing(self):
        pygame.draw.rect(self.screen, self.color, ((self.position_x, self.position_y), (self.size[0], self.size[1])))
    
    # creazione della foresta
    def draw_forest(self):
        pygame.draw.rect(self.screen, self.color, ((self.position_x, self.position_y), (self.size[0], self.size[1])))
        
        random.seed(12)
        for _ in range(5):
            # si fa meno 10 e 20 perchè sarebbero le grandezze del tronco e il punto di creazione del tronco è lo spigolo in alto a sinistra
            ofset_x = random.randint(0, self.size[0] - 10)
            ofset_y = random.randint(0, self.size[1] - 20)
            position_x = self.position_x + ofset_x
            position_y = self.position_y + ofset_y

            pygame.draw.rect(self.screen, MARRONE, ((position_x, position_y), (10, 20)))
            pygame.draw.circle(self.screen, VERDE_SCURO, (position_x - 2, position_y), 10)
            pygame.draw.circle(self.screen, VERDE_SCURO, (position_x + 12, position_y), 10)
            pygame.draw.circle(self.screen, VERDE_SCURO, (position_x + 5, position_y - 10), 10)
    
    def draw_road(self):
        pygame.draw.rect(self.screen, self.color, ((self.position_x, self.position_y), (self.size[0], self.size[1])))
        pygame.draw.line(self.screen, BIANCO, (self.position_x , self.position_y + 4), (self.position_x + self.size[0], self.position_y + 4), width=2)
        # si mette 6 nella posizione perchè si conta anche lo spessore della riga quindi 4 che è l'ofset + lo spessore
        pygame.draw.line(self.screen, BIANCO, 
                         (self.position_x, self.position_y + self.size[1] - 6), (self.position_x + self.size[0], self.position_y + self.size[1] - 6), width=2)


    def draw(self, camera_x, camera_y):
        self.position_x = self.cordinata_x - camera_x
        self.position_y = self.cordinata_y - camera_y
        if self.name == "home":
            self.draw_casa()
        if self.name == "lake":
            self.draw_circle()
        if self.name == "manufacturing":
            self.draw_manufacturing()
        if self.name == "forest":
            self.draw_forest()
        if self.name == "road":
            self.draw_road()

# personaggi che si muoveranno
class Robot():
    def __init__(self, screen, cordinate_x, cordinate_y, camera_x, camera_y, job):
        self.name = ''
        self.screen = screen
        self.position_x = 0
        self.position_y = 0
        self.cordinate_x = cordinate_x
        self.cordinate_y = cordinate_y
        self.job = job
        self.text = pygame.font.Font('freesansbold.ttf', 15)
        self.text_surface = self.text.render(self.job, False, (0, 0, 0))
        self.height = self.text_surface.get_height()
        self.width = self.text_surface.get_width()

    # def walk_robots(self):
    #     self.position_x += 1

    def draw(self, camera_x, camera_y):
        self.position_x = self.cordinate_x - camera_x
        self.position_y = self.cordinate_y - camera_y
        # timer = Timer(5.0, self.walk_robots)
        # timer.start()

        center_x, center_y = get_center('text', [self.width, self.height]) # si ottiene il centro del testo
        if self.job == 'citizen':
            self.citizen(center_x)
        elif self.job == 'farmer':
            self.farmer(center_x)
        elif self.job == 'miner':
            self.miner(center_x)

    def citizen(self, center_x):
        raggio = 10
        self.screen.blit(self.text_surface, (self.position_x - center_x, self.position_y - self.height - raggio))
        pygame.draw.circle(self.screen, ROSA, (self.position_x, self.position_y), raggio)
    
    def farmer(self, center_x):
        self.screen.blit(self.text_surface, (self.position_x + (10 - center_x), self.position_y - 20 - self.height))
        pygame.draw.polygon(self.screen, GIALLO_SPENTO, ((self.position_x, self.position_y), (self.position_x + 20, self.position_y), (self.position_x + 10, self.position_y - 20)))

    def miner(self, center_x):
        size = (10, 10) 
        self.screen.blit(self.text_surface, (self.position_x + (size[0] // 2 - center_x), self.position_y - self.height)) # si sottrae la metà del lato delle x cosi che si ottiene il punto preciso di partenza delle x cosi che la scritta compaia centrale
        pygame.draw.rect(self.screen, NERO, ((self.position_x, self.position_y), size), border_radius=2)
    