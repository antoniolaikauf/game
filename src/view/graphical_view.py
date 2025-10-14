import pygame
from data.initial_city import *  # Correct relative import
from ..models.city_object import Object
from ..controllers.features import Button_general, Menu


def check_button(position_chicked, menu_bottoni):
    for button_id in range(len(menu_bottoni)):
        print(f" indice bottone --> {button_id}, cordinate --> {menu_bottoni[button_id]}")
    





class LayoutGame:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("villaggio")
        self.dragging = False
        self.last_position = (0, 0)
        self.tile_width = WIDTH
        self.tile_height = HEIGHT
        self.image = pygame.image.load("src/utils/background1.jpg").convert()
        self.camera_x = 0
        self.camera_y = 0

    def draw_grid(self):
        blocksize = 20
        for idX in range(0, WIDTH, blocksize):
            for idY in range(0, HEIGHT, blocksize):
                rect = pygame.Rect(idX, idY, blocksize, blocksize)
                pygame.draw.rect(self.screen, (200, 200, 200), rect, 1)      

    def start_game(self):
        button = Button_general()
        menu = Menu()
        running = True
        position_x = 0
        position_y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.dragging = True
                    self.last_position = pygame.mouse.get_pos()

                    # per uscire dal menu si clicca all'esterno del menu
                    if (((MENU['positon_x'] < self.last_position[0]) and (self.last_position[0] < MENU['positon_x'] + MENU['width'])) and ((MENU['positon_y'] < self.last_position[1]) and (self.last_position[1] < MENU['positon_y'] + MENU['height']))):
                        pass
                    else:
                        button.button_click = False

                    check_button(self.last_position, menu.position_button)
                    # controllo se clicco bottone tendina
                    if button.mouse_over(self.last_position):
                        # implementare qua tendina di oggetti
                        button.button_click = True

                
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.dragging = False
                
                elif event.type == pygame.MOUSEMOTION :
                    # over sul bottone
                    if button.mouse_over(pygame.mouse.get_pos()):
                        pass
                    
                    if self.dragging == True:
                        position_x, position_y = pygame.mouse.get_pos() # posizione dopo aaver fatto il drag con il mouse 

                        # quantità mossa, può essere una decina o anche 0 essendo che ho visto che non si aggiorna
                        # self.camera_x --> 5, self.camera_y --> 41, dx --> 0, dy --> -2
                        # self.camera_x --> 5, self.camera_y --> 41, dx --> 0, dy --> 0
                        dx = position_x - self.last_position[0] 
                        dy = position_y - self.last_position[1] 
                        # grandezza della camera cioè di quanto in la ti sei spinto fino ad ora 
                        self.camera_x -= dx 
                        self.camera_y -= dy

                        self.last_position = (position_x, position_y)

                        print(f"self.camera_x --> {self.camera_x}, self.camera_y --> {self.camera_y}, dx --> {dx}, dy --> {dy}")


            '''
            si crea una griglia 3x3 cosi da coprire meglio gli spazi sopratutto quando si muove diagonalemnte
            dopo questa griglia viene sempre espansa man mano che camera cresce 
            '''
            num_tiles_x = 3  # Per x
            num_tiles_y = 3  # Per y, per scrolling verticale
            min_tile_x = int(self.camera_x // self.tile_width) - 1 # si mette - 1 perchè cosi si ha uno a sinistra uno in centro e uno a destra, senza quel -1 all'inizio avresti problemi ad andare a sinistra 
            min_tile_y = int(self.camera_y // self.tile_height) - 1
            for i in range(num_tiles_x):
                for j in range(num_tiles_y):
                    # Posizione mondiale
                    world_x = (min_tile_x + i) * self.tile_width
                    world_y = (min_tile_y + j) * self.tile_height
                    
                    # Posizione schermo (offset camera)
                    screen_x = world_x - self.camera_x
                    screen_y = world_y - self.camera_y
                    # se siamo dentro tra la grandezza dell'immagine a sinistra (e quindi -) e la grandezza del layout + la sua immagine.       stessa cosa per l'altezza
                    if -self.tile_width < screen_x < WIDTH + self.tile_width and -self.tile_height < screen_y < HEIGHT + self.tile_height:
                        self.screen.blit(self.image, (screen_x, screen_y))

            self.draw_grid()

            for num_object_x in range(CORDINATE.shape[0]):
                object = Object(OBJECT_BASE[num_object_x], self.screen, CORDINATE[num_object_x][0], CORDINATE[num_object_x][1], self.camera_x, self.camera_y)
                object.draw()
            
            button(self.screen, 'Menu', 'center')

            # mostrare il menu una volta cliccato il bottone
            if button.button_click:
                menu(self.screen)
            
            pygame.display.flip()      
            self.clock.tick(60)        
        
        pygame.quit()

if __name__ == "__main__":
    game = LayoutGame()
    game.start_game()    