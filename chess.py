import pygame

class Board:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.square_size = min(width, height) // 8
        self.board = [
            [-1.125,-1.375,-1.875,-2,-1.625,-1.75,-1.5,-1.25],
            [-0.125,-0.25,-0.375,-0.5,-0.625,-0.75,-0.875,-1],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0.125,0.25,0.375,0.5,0.625,0.75,0.875,1],
            [1.125,1.375,1.875,2,1.625,1.75,1.5,1.25]
        ]
        self.init_board(screen)

    def init_board(self, screen):
        


        pass

    def draw(self, screen):
        # Draw the chess board on the screen
        for row in range(8):
            print(f"Drawing row {self.board[row]}")
            for col in range(8):
                color = (255, 255, 255) if (row + col) % 2 == 0 else (50, 100, 150)
                pygame.draw.rect(screen, color, (col * self.square_size, row * self.square_size, self.square_size, self.square_size))

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

        screen.blit(BE, (100, 100))


        