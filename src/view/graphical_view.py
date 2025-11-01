import pygame
from data.initial_city import *  # Correct relative import
from ..models.city_object import Object
from ..controllers.features import Button_general, Menu
import numpy as np

# dal centro si ottiene i suoi punti più estremi
def get_bounds(center_x, center_y, width, height):
    half_w = width / 2
    half_h = height / 2
    
    return (
        center_x - half_w,
        center_x + half_w,
        center_y - half_h,
        center_y + half_h
    )


# si controllano le posizioni 'false' degli oggetti 
def position_object(object, position_release):
    global CORDINATE
    global CORDINATE_UPDATE
    print(f"ho cliccato il bottone --> {object}, posiztion_release --> {position_release}")
    draw = True
    match object['name']:
        case 'home':  
            size = SIZE_HOME
            color = GRIGIO
            width_new, height_new = size
        case 'lake':
            size = SIZE_LAKE
            color = AZZURRO
            width_new = size[0]
            height_new = size[0]
        
            
    # si calcola il centro cosi si fa in un modo per tutti gli oggetti perchè il cerchio da cordinate centro invece
    # con il quadrato si ha i punti più a sinistra e più in alto
     
    for  idx_coord, coord in enumerate(CORDINATE_UPDATE):
        if OBJECT_BASE[idx_coord]['name'] == 'home':
            print(coord)
            center_x = coord[0] + (SIZE_HOME[0] // 2)
            center_y = coord[1] + (SIZE_HOME[1] // 2)
        elif OBJECT_BASE[idx_coord]['name'] == 'lake':
            print(coord)
            center_x = coord[0] 
            center_y = coord[1]

        print(f"draw --> {draw}")
        print(f"cordinate oggetto creato -->{CORDINATE[idx_coord]}")
        print(f"cordinate oggetto creato CORDINATE_UPDATE -->{CORDINATE_UPDATE[idx_coord]}")
        position_left, position_right, position_top, position_bottom = get_bounds(center_x, center_y, width_new, height_new)
        print(f"position_bottom --> {position_bottom}, position_top --> {position_top}, position_left --> {position_left}, position_right --> {position_right}")
        if (((position_left <= position_release[0]) and (position_release[0] <= position_right)) and ((position_top <= position_release[1]) and (position_release[1] <= position_bottom ))):
            draw = False
            break
    

    
    if draw:
        OBJECT_BASE.append({'name':object['name'], 'size':size, 'color':color})
        # inserire le cordinate qua
        CORDINATE = np.concatenate((CORDINATE, np.array([[position_release[0], position_release[1]]])), axis=0)
        CORDINATE_UPDATE = np.concatenate((CORDINATE_UPDATE, np.array([[position_release[0], position_release[1]]])), axis=0)
        draw = False
        

def check_button(position_clicked, pulsante): 
    print(pulsante)
    # si controlla se si ha cliccato il bottone dentro al menu degli oggetti
    if (((position_clicked[0] > pulsante['position_x_min']) and (position_clicked[0] < pulsante['position_X_max'])) and ((position_clicked[1] > pulsante['position_y_min']) and (position_clicked[1] < pulsante['position_y_max']))):
        return True
    return False


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
        pulsante_premuto = False
        name_button = ''

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.dragging = True
                    self.last_position = pygame.mouse.get_pos()

                    '''

                        quando si clicca un pulsante dentro il menu permette di depositare l'oggetto
                        all'interno della mappa, una volta rilasciato il menu rimane aperto.
                        cosi che se si volesse depositare un altro oggetto basta ricliccarlo.
                        se non si clicca un altro pulsante e si clicca all'infuori del menu allora il menu scomparirà
                        questo processo è gestito tutto da pulsante_premuto e condizioni per vedere dove si è premuto,
                        invece per la creazione dell'oggetto viene gestito da position_object che lo crea nel punto cliccato
                        all'infuori del menu e da position_object che controlla se si ha cliccato un pulsante o no

                    '''
    
                    if (((MENU['positon_x'] < self.last_position[0]) and (self.last_position[0] < MENU['positon_x'] + MENU['width'])) and ((MENU['positon_y'] < self.last_position[1]) and (self.last_position[1] < MENU['positon_y'] + MENU['height']))):
                        for button_menu_id in range(len(menu.position_button)):
                            pulsante_premuto = check_button(self.last_position, menu.position_button[button_menu_id])
                            name_button = menu.position_button[button_menu_id]                          
                            if pulsante_premuto:
                                break
                    else:
                        if pulsante_premuto:
                            pulsante_premuto = False
                            position_object(name_button, self.last_position)
                        else:
                            button.button_click = False

                    # controllo se clicco bottone tendina
                    if button.mouse_over(self.last_position):
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

                        # si continua ad aggiornare le cordinate, se si va oltre lo schermo si resettano essendo che il
                        # click del mouse va da 0' a WIDTH e da 0 a HEIGHT
                        for cordUpd_id in range(len(CORDINATE_UPDATE)):
                            if CORDINATE_UPDATE[cordUpd_id][0] > WIDTH: CORDINATE_UPDATE[cordUpd_id][0] = CORDINATE[cordUpd_id][0]
                            if CORDINATE_UPDATE[cordUpd_id][1] > HEIGHT: CORDINATE_UPDATE[cordUpd_id][1] = CORDINATE[cordUpd_id][1]
                                    
                            CORDINATE_UPDATE[cordUpd_id][0] += dx
                            CORDINATE_UPDATE[cordUpd_id][1] += dy

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
                object = Object(OBJECT_BASE[num_object_x]['name'], self.screen, CORDINATE[num_object_x][0], 
                                CORDINATE[num_object_x][1], self.camera_x, self.camera_y, OBJECT_BASE[num_object_x]['size'], OBJECT_BASE[num_object_x]['color'])
                object.draw()
            
            button(self.screen, 'Menu', 'center')

            # mostrare il menu una volta cliccato il bottone
            if button.button_click:
                menu(self.screen)
            
            pygame.display.flip()      
            self.clock.tick(60)        
        
        pygame.quit()   