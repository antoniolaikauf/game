import pygame
from data.initial_city import *

#------------------------
#    GESTIONE BOTTONE
#------------------------

class Button:
    def __init__(self):
        self.position_x = 0
        self.position_y = 0
        self.color =  0
        self.color_over = 0
        self.width = 0
        self.height = 0
        self.radius = 0
        self.font = 0
        self.button_click = False
        self.size = [] #  widthg, height

    def __call__(self, screen, text_name, position, cordinata_x = 0, cordinata_y = 0):
        # cordinate bottone formato da due rettangoli e 4 cerchi ai lati che formano i raccordi
        pygame.draw.rect(screen, self.color, ((self.position_x, self.position_y), (self.width, self.height)))
        pygame.draw.rect(screen, self.color, (((self.position_x - self.radius), (self.position_y + self.radius)), ((self.width +  2 * self.radius), (self.height - 2 * self.radius))))
        pygame.draw.circle(screen, self.color, (self.position_x , self.position_y + self.radius), self.radius)
        pygame.draw.circle(screen, self.color, (self.position_x , self.position_y + self.height - self.radius), self.radius)
        pygame.draw.circle(screen, self.color, (self.position_x + self.width , self.position_y + self.height - self.radius), self.radius)
        pygame.draw.circle(screen, self.color, (self.position_x + self.width , self.position_y + self.radius), self.radius)

        #print(f"la cordinata di cordinata_x --> {cordinata_x}, cordinata di cordinata_y --> {cordinata_y}")
        text = pygame.font.Font('freesansbold.ttf', self.font)
        text_surface = 0
        # creazione testo bottone
        if position == 'center':
            text_surface = text.render(text_name , False, (0, 0, 0))
            screen.blit(text_surface, (((self.width // 2) + self.position_x) - text_surface.get_width() // 2, ((self.height // 2) + self.position_y) - (text_surface.get_height() // 2)))
        elif position == 'choice':
            text_surface = text.render(text_name, False, (0, 0, 0))
            screen.blit(text_surface, (cordinata_x, cordinata_y))

        self.size.append(text_surface.get_width())
        self.size.append(text_surface.get_height())
        
    def mouse_over(self, position):
        position_x = position[0]
        position_y = position[1]

        min_left = self.position_x - self.radius # cordinata minima left del pulsante 
        max_left = self.position_x + self.width + self.radius # cordinata massima left del pulsante
        min_top = self.position_y # cordinata minima top del pulsante
        max_top = self.position_y + self.height # cordinata massima top del pulsante

        color_save = self.color
        if (min_left < position_x and position_x < max_left) and (min_top < position_y and position_y < max_top): # premuto il pulsante o sono sul bottone
            self.color = self.color_over
            return True
        
        self.color = color_save
        return False

class Button_object(Button):
    def __init__(self):
        self.position_x = BUTTON_OBJECT['positon_x']
        self.position_y = BUTTON_OBJECT['positon_y']
        self.color =  BUTTON_OBJECT['color_not_over']
        self.color_over = BUTTON_OBJECT['color_over']
        self.width = BUTTON_OBJECT['width']
        self.height = BUTTON_OBJECT['height']
        self.radius = BUTTON_OBJECT['radius']
        self.font = BUTTON_OBJECT['font']
        self.button_click = False
        self.size = []

class Button_general(Button):
    def __init__(self):
        self.position_x = BUTTON['positon_x']
        self.position_y = BUTTON['positon_y']
        self.color =  BUTTON['color_not_over']
        self.color_over = BUTTON['color_over']
        self.width = BUTTON['width']
        self.height = BUTTON['height']
        self.radius = BUTTON['radius']
        self.font = BUTTON['font']
        self.button_click = False
        self.size = []




#------------------------
#     GESTIONE MENU
#------------------------


class Menu:
    def __init__(self):
        self.position_x = MENU['positon_x']
        self.position_y = MENU['positon_y']
        self.color =  MENU['color_not_over']
        self.width = MENU['width']
        self.height = MENU['height']
        self.radius = MENU['radius']
        self.font = MENU['font']
        self.tag = MENU['tag']
        self.button_tag = [Button_object() for Button_tag in range(len(MENU['tag']))]
    
    def __call__(self, screen):
        pygame.draw.rect(screen, self.color, ((self.position_x, self.position_y), (self.width, self.height)))
        pygame.draw.rect(screen, self.color, (((self.position_x - self.radius), (self.position_y + self.radius)), ((self.width + 2* self.radius), (self.height - 2*self.radius))))
        pygame.draw.circle(screen, self.color, (self.position_x , self.position_y + self.radius), self.radius)
        pygame.draw.circle(screen, self.color, (self.position_x , self.position_y + self.height - self.radius), self.radius)
        pygame.draw.circle(screen, self.color, (self.position_x + self.width , self.position_y + self.height - self.radius), self.radius)
        pygame.draw.circle(screen, self.color, (self.position_x + self.width , self.position_y + self.radius), self.radius)
    
        # salvataggio prime positioni

        position_mouse = pygame.mouse.get_pos()
        for id_tag in range(len(self.tag)):
             print(f"la cordinata di cordinata_x --> {self.button_tag[id_tag].position_y}, cordinata di BUTTON_OBJECT['height'] --> {BUTTON_OBJECT['height']} ")
             if id_tag == 0: position_Y = self.position_y + (BUTTON_OBJECT['height'] * id_tag ) + 5
             else: position_Y += (BUTTON_OBJECT['height']) + 5
             self.button_tag[id_tag].position_y = position_Y 
             self.button_tag[id_tag](screen, self.tag[id_tag], 'choice', self.position_x + 10, position_Y + ( BUTTON_OBJECT['height'] // 2 - BUTTON_OBJECT['font'] // 2))
             self.button_tag[id_tag].mouse_over(position_mouse)
             

    def mouse_over(self):
        pass
    
        
        