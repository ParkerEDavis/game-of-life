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
    
    def update(self):
        self.game_map[random.randint(0, 9)][random.randint(0, 9)] = 1
        self.gameDraw()
    
    def gameDraw(self):
        for row in range(self.height):
            for column in range(self.width):
                if self.game_map[row][column] == 1:
                    color = (250, 250, 0)
                else:
                    color = (200, 200, 200)
                
                pygame.draw.rect(self.window, color, (row * 16, column * 16, 16, 16))