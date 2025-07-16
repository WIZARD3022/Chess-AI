import pygame

class Board:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.init_board(screen)

    def load_image(path):
        return pygame.transform.scale(path, (100, 100))

    def init_board(self, screen):
        BE = pygame.image.load("./image/Black_elephant.png")
        BE = self.load_image(BE)
        WE = pygame.image.load("./image/White_elephant.png")
        WE = self.load_image(WE)

        BH = pygame.image.load("./image/Black_horse.png")
        BH = self.load_image(BH)
        WH = pygame.image.load("./image/White_horse.png")
        WH = self.load_image(WH)

        BK = pygame.image.load("./image/Black_King.png")
        BK = self.load_image(BK)
        WK = pygame.image.load("./image/White_King.png")
        WK = self.load_image(WK)

        BM = pygame.image.load("./image/Black_minister.png")
        BM = self.load_image(BM)
        WM = pygame.image.load("./image/White_minister.png")
        WM = self.load_image(WM)

        BP = pygame.image.load("./image/Black_pawn.png")
        BP = self.load_image(BP)
        WP = pygame.image.load("./image/White_pawn.png")
        WP = self.load_image(WP)

        BQ = pygame.image.load("./image/Black_queen.png")
        BQ = self.load_image(BQ)
        WQ = pygame.image.load("./image/White_queen.png")
        WQ = self.load_image(WQ)

        screen.blit(BE, (100, 100))


        pass

    def draw(self, screen):
        # Draw the chess board on the screen
        square_size = min(self.width, self.height) // 8
        for row in range(8):
            for col in range(8):
                color = (255, 255, 255) if (row + col) % 2 == 0 else (0, 0, 0)
                pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))