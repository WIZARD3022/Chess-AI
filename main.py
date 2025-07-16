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
    BE = pygame.transform.scale(BE, (100, 100))
    WE = pygame.image.load("./image/White_elephant.png")
    WE = pygame.transform.scale(WE, (100, 100))

    BH = pygame.image.load("./image/Black_horse.png")
    BH = pygame.transform.scale(BH, (100, 100))
    WH = pygame.image.load("./image/White_horse.png")
    WH = pygame.transform.scale(WH, (100, 100))

    BK = pygame.image.load("./image/Black_King.png")
    BK = pygame.transform.scale(BK, (100, 100))
    WK = pygame.image.load("./image/White_King.png")
    WK = pygame.transform.scale(WK, (100, 100))

    BM = pygame.image.load("./image/Black_minister.png")
    BM = pygame.transform.scale(BM, (100, 100))
    WM = pygame.image.load("./image/White_minister.png")
    WM = pygame.transform.scale(WM, (100, 100))

    BP = pygame.image.load("./image/Black_pawn.png")
    BP = pygame.transform.scale(BP, (100, 100))
    WP = pygame.image.load("./image/White_pawn.png")
    WP = pygame.transform.scale(WP, (100, 100))

    BQ = pygame.image.load("./image/Black_queen.png")
    BQ = pygame.transform.scale(BQ, (100, 100))
    WQ = pygame.image.load("./image/White_queen.png")
    WQ = pygame.transform.scale(WQ, (100, 100))


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