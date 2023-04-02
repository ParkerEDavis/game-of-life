from game_of_life import *

clock = pygame.time.Clock()
FPS = 2

game = GameOfLife(20, 20)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    game.update()

    # Update Display
    pygame.display.flip()
    clock.tick(FPS)
# End of Loop

# Program Quit
pygame.quit()