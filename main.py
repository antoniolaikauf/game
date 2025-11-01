
import pygame
from src.view.graphical_view import LayoutGame
from data.initial_city import *

if __name__ == "__main__":
     screen = pygame.display.set_mode((WIDTH, HEIGHT))
     layout_game = LayoutGame(screen)  
     layout_game.start_game()    
