import pygame
import sys
from chess import Board
from ai import AI


def main():

    # Initialize Pygame
    pygame.init()

    # Screen settings
    WIDTH, HEIGHT = 1450, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # font = pygame.font.SysFont(None, 16)

    # Clock for controlling FPS
    clock = pygame.time.Clock()
    FPS = 60

    board = Board(800, 800, screen)
    ai = AI(650, 680, screen, board)

    # Game Loop
    running = True
    while running:

        pygame.display.set_caption(f"Chess fps :{clock.tick(FPS)}")
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    print("Space key pressed")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    board.select_square(mouse_x, mouse_y, screen)

        board.dashboard(screen)
                
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

main()