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

    board = Board(WIDTH, HEIGHT)

    BE = pygame.image.load("./image/Black_elephant.png")
    WE = pygame.image.load("./image/White_elephant.png")

    BH = pygame.image.load("./image/Black_horse.png")
    WH = pygame.image.load("./image/White_horse.png")

    BK = pygame.image.load("./image/Black_King.png")
    WK = pygame.image.load("./image/White_King.png")

    BM = pygame.image.load("./image/Black_minister.png")
    WM = pygame.image.load("./image/White_minister.png")

    BP = pygame.image.load("./image/Black_pawn.png")
    WP = pygame.image.load("./image/White_pawn.png")

    BQ = pygame.image.load("./image/Black_queen.png")
    WQ = pygame.image.load("./image/White_queen.png")

    BE = pygame.transform.scale(BE, (100, 100))

    # Game Loop
    running = True
    while running:
        # clock.tick(FPS)  # Limit FPS
        pygame.display.set_caption(f"Chess fps :{clock.tick(FPS)}")
        screen.blit(BE, (100, 100))
        # screen.blit(BE, (100, 100))

        # screen.fill(BLACK)  # Clear screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            board.draw(screen)
                
        pygame.display.flip()




    # Quit Pygame
    pygame.quit()
    sys.exit()

main()