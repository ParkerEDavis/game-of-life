from game_of_life import *
import time

clock = pygame.time.Clock()
FPS = 1

game = GameOfLife(9, 9)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    game.update()
    #running = False

    # Update Display
    pygame.display.flip()
    clock.tick(FPS)
# End of Loop

# Program Quit
pygame.quit()