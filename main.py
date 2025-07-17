import pygame
import sys
from chess import Board


def main():

    # Initialize Pygame
    pygame.init()

    # Screen settings
    WIDTH, HEIGHT = 1400, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.SysFont(None, 16)

    # Clock for controlling FPS
    clock = pygame.time.Clock()
    FPS = 60

    board = Board(WIDTH, HEIGHT, screen)
    board.init_board(screen)

    # Game Loop
    running = True
    while running:
        # clock.tick(FPS)  # Limit FPS
        pygame.display.set_caption(f"Chess fps :{clock.tick(FPS)}")
        # screen.blit(BE, (100, 100))
        # screen.blit(WE, (200, 100))
        # screen.blit(BQ, (300, 100))
        # screen.blit(WQ, (400, 100))
        # screen.blit(BK, (200, 300))
        # screen.blit(WK, (200, 300))
        # screen.blit(BE, (100, 100))

        # screen.fill(BLACK)  # Clear screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    print("Space key pressed")
        board.draw(screen)
                
        pygame.display.flip()




    # Quit Pygame
    pygame.quit()
    sys.exit()

main()