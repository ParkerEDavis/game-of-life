from game_of_life import *

clock = pygame.time.Clock()
FPS = 2

game = GameOfLife(20, 20)

paused = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.clicked(pygame.mouse.get_pos())
    
    game.update(paused)

    # Update Display
    pygame.display.flip()
    clock.tick(FPS)
# End of Loop

# Program Quit
pygame.quit()