import pygame
from data.initial_city import *

class Button:
    def __init__(self):
        self.position_x = BUTTON['positon_x']
        self.position_y = BUTTON['positon_y']
        self.color =  BUTTON['color']
        self.width = BUTTON['width']
        self.height = BUTTON['height']
        self.radius = BUTTON['radius']
        self.font = BUTTON['font']
        self.text = BUTTON['text']

    def __call__(self, screen):
        # cordinate bottone formato da due rettangoli e 4 cerchi ai lati che formano i raccordi
        pygame.draw.rect(screen, self.color, ((self.position_x, self.position_y), (self.width, self.height)))
        pygame.draw.rect(screen, self.color, (((self.position_x - self.radius), (self.position_y + self.radius)), ((self.width +  2 * self.radius), (self.height - 2 * self.radius))))
        pygame.draw.circle(screen, self.color, (self.position_x , self.position_y + self.radius), self.radius)
        pygame.draw.circle(screen, self.color, (self.position_x , self.position_y + self.height - self.radius), self.radius)
        pygame.draw.circle(screen, self.color, (self.position_x + self.width , self.position_y + self.height - self.radius), self.radius)
        pygame.draw.circle(screen, self.color, (self.position_x + self.width , self.position_y + self.radius), self.radius)

        # centratura testo nel bottone
        largeText = pygame.font.Font('freesansbold.ttf',self.font)
        text_surface = largeText.render(self.text , False, (0, 0, 0))
        screen.blit(text_surface, (((self.width // 2) + self.position_x) - text_surface.get_width() // 2, ((self.height // 2) + self.position_y) - (text_surface.get_height() // 2)))
        