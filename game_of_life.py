import pygame
import random

class GameOfLife:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.window_width = width * 16
        self.window_height = height * 16

        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Game of Life")

        self.game_map = [[0 for column in range(self.width)] for row in range(self.height)]
    
    def frameUpdate(self):
        for row in range(self.height):
            for column in range(self.width):
                pygame.draw.rect(self.window, (0, 0, 100), (row * 16, column * 16, 16, 16))