import pygame
from data.initial_city import *

class Button:
    def __init__(self):
        self.position_x = BUTTON['positon_x']
        self.position_y = BUTTON['positon_y']
        self.color =  BUTTON['color_not_over']
        self.width = BUTTON['width']
        self.height = BUTTON['height']
        self.radius = BUTTON['radius']
        self.font = BUTTON['font']
        self.text = BUTTON['text']
        self.button_click = False

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
        
    def mouse_over(self, position):
        position_x = position[0]
        position_y = position[1]

        min_left = self.position_x - self.radius # cordinata minima left del pulsante 
        max_left = self.position_x + self.width + self.radius # cordinata massima left del pulsante
        min_top = self.position_y # cordinata minima top del pulsante
        max_top = self.position_y + self.height # cordinata massima top del pulsante

        if (min_left < position_x and position_x < max_left) and (min_top < position_y and position_y < max_top): # premuto il pulsante o sono sul bottone
            self.color = BUTTON['color_over']
            return True
        
        self.color = BUTTON['color_not_over']
        return False

class Menu:
    def __init__(self):
        self.list = MENU['list']
        self.position_x = MENU['positon_x']
        self.position_y = MENU['positon_y']
        self.color =  MENU['color_not_over']
        self.width = MENU['width']
        self.height = MENU['height']
        self.radius = MENU['radius']
        self.font = MENU['font']
        self.text = MENU['text']
    
    def __call__(self, screen):
        pygame.draw.rect(screen, self.color, ((self.position_x, self.position_y), (self.width, self.height)))
        pygame.draw.rect(screen, self.color, (((self.position_x - self.radius), (self.position_y + self.radius)), ((self.width + 2* self.radius), (self.height - 2*self.radius))))
    
    def mouse_over(self):
        pass