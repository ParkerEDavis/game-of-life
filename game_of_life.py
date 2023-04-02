import pygame
import copy

class GameOfLife:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.window_width = width * 16
        self.window_height = height * 16

        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Game of Life")

        self.game_map = [[0 for column in range(self.width)] for row in range(self.height)]
    
    def update(self, paused):
        self.gameDraw(paused)
        if not paused:
            self.cellCycle()
    

    def cellCycle(self):
        temp_map = copy.deepcopy(self.game_map)
        for row in range(self.height):
            for column in range(self.width):
                surrounding_cells = self.checkCell(row, column)
                cell_state = self.game_map[row][column]

                if (cell_state == 0) and (surrounding_cells == 3):
                    temp_map[row][column] = 1
                elif (cell_state == 1) and (surrounding_cells <= 1):
                    temp_map[row][column] = 0
                elif (cell_state == 1) and (surrounding_cells >= 4):
                    temp_map[row][column] = 0

        self.game_map = temp_map

    def checkCell(self, cell_row, cell_column):
        # To tally up total surrounding cells
        surrounding_cells = 0

        # Will be added/subtracted from current location to find surrounding cells
        side_left = 1
        side_right = 1
        side_top = 1
        side_bottom = 1

        # Check to see if current cell is on any edges
        if cell_row == 0: # If on top row
            side_top = 0 # Don't check above
        if cell_row == self.height - 1: #etc
            side_bottom = 0 # etc
        if cell_column == 0:
            side_left = 0
        if cell_column == self.width - 1:
            side_right = 0
        
        #Then iterate through surrounding cells
        for row in range(cell_row - side_top, cell_row + side_bottom + 1):
            for column in range(cell_column - side_left, cell_column + side_right + 1):
                if (row != cell_row) or (column != cell_column):
                    surrounding_cells += self.game_map[row][column]
        return surrounding_cells
    
    def clicked(self, mouse_pos):
        x = int(mouse_pos[0] / 16)
        y = int(mouse_pos[1] / 16)
        self.game_map[x][y] = not self.game_map[x][y]

    def gameDraw(self, paused):
        for row in range(self.height):
            for column in range(self.width):
                if self.game_map[row][column] == 1:
                    color = (250, 250, 0)
                elif paused:
                    color = (200, 100, 100)
                else:
                    color = (200, 200, 200)
                
                pygame.draw.rect(self.window, color, (row * 16, column * 16, 16, 16))

    def reset(self):
        self.game_map = [[0 for column in range(self.width)] for row in range(self.height)]