import pygame
import sys
from chess import Board

def load_image(path):
    return pygame.transform.scale(path, (100, 100))


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
    BE = load_image(BE)
    WE = pygame.image.load("./image/White_elephant.png")
    WE = load_image(WE)

    BH = pygame.image.load("./image/Black_horse.png")
    BH = load_image(BH)
    WH = pygame.image.load("./image/White_horse.png")
    WH = load_image(WH)

    BK = pygame.image.load("./image/Black_King.png")
    BK = load_image(BK)
    WK = pygame.image.load("./image/White_King.png")
    WK = load_image(WK)

    BM = pygame.image.load("./image/Black_minister.png")
    BM = load_image(BM)
    WM = pygame.image.load("./image/White_minister.png")
    WM = load_image(WM)

    BP = pygame.image.load("./image/Black_pawn.png")
    BP = load_image(BP)
    WP = pygame.image.load("./image/White_pawn.png")
    WP = load_image(WP)

    BQ = pygame.image.load("./image/Black_queen.png")
    BQ = load_image(BQ)
    WQ = pygame.image.load("./image/White_queen.png")
    WQ = load_image(WQ)


    # Game Loop
    running = True
    while running:
        # clock.tick(FPS)  # Limit FPS
        pygame.display.set_caption(f"Chess fps :{clock.tick(FPS)}")
        screen.blit(BE, (100, 100))
        screen.blit(WE, (200, 100))
        screen.blit(BQ, (300, 100))
        screen.blit(WQ, (400, 100))
        screen.blit(BK, (200, 300))
        screen.blit(WK, (200, 300))
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