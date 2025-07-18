import pygame

class Board:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.turn = "white"  # or 'black'
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

    def init_board(self, screen):
        
        for row in range(8):
            # print(f"Drawing row {self.board[row]}")
            for col in range(8):
                color = (255, 255, 255) if (row + col) % 2 == 0 else (50, 100, 150)
                pygame.draw.rect(screen, color, (col * self.square_size, row * self.square_size, self.square_size, self.square_size))


        pass

    def select_square(self, mouse_x, mouse_y,screen):
        col = mouse_x // self.square_size
        row = mouse_y // self.square_size
        if 0 <= row < 8 and 0 <= col < 8:
            piece = self.board[row][col]
            print(f"Selected piece at ({row}, {col}): {piece}")
            if piece > 0:
                moving = 'white'
            elif piece < 0:
                moving = 'black'
            if moving == self.turn:
                print(f"Moving piece: {piece} for {self.turn}")
                pygame.draw.rect(screen, (255, 0, 0), (col * self.square_size, row * self.square_size, self.square_size, self.square_size), 3)
                self.turn = 'black' if self.turn == 'white' else 'white'
        else:
            print("Clicked outside the board")


    def unselect_square(self, mouse_x, mouse_y,screen):
        col = mouse_x // self.square_size
        row = mouse_y // self.square_size
        if 0 <= row < 8 and 0 <= col < 8:
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, (255, 255, 255), (col * self.square_size, row * self.square_size, self.square_size, self.square_size))
            else:
                pygame.draw.rect(screen, (50, 100, 150), (col * self.square_size, row * self.square_size, self.square_size, self.square_size))

    def start_game(self):
        # Initialize the game state and pieces
        END = False
        while END:
            print("Game is running")
            print(f"Current turn: {turn} select a piece")
            turn = 'black' if turn == 'white' else 'white'

        pass

    def move_piece(self, start_row, start_col, end_row, end_col):
        # Move a piece from (start_row, start_col) to (end_row, end_col)
        piece = self.board[start_row][start_col]
        self.board[start_row][start_col] = 0
        self.board[end_row][end_col] = piece

    def draw(self, screen):
        # Draw the chess board on the screen

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

        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece == -1.125:
                    screen.blit(BE, (col * self.square_size, row * self.square_size))
                elif piece == -1.25:
                    screen.blit(BE, (col * self.square_size, row * self.square_size))
                    # black elephant
                elif piece == -0.125:
                    screen.blit(BP, (col * self.square_size, row * self.square_size))
                elif piece == -0.25:
                    screen.blit(BP, (col * self.square_size, row * self.square_size))
                elif piece == -0.375:
                    screen.blit(BP, (col * self.square_size, row * self.square_size))
                elif piece == -0.5:
                    screen.blit(BP, (col * self.square_size, row * self.square_size))
                elif piece == -0.625:
                    screen.blit(BP, (col * self.square_size, row * self.square_size))
                elif piece == -0.75:
                    screen.blit(BP, (col * self.square_size, row * self.square_size))
                elif piece == -0.875:
                    screen.blit(BP, (col * self.square_size, row * self.square_size))
                elif piece == -1:
                    screen.blit(BP, (col * self.square_size, row * self.square_size))
                    # Black pawn
                elif piece == -1.375:
                    screen.blit(BH, (col * self.square_size, row * self.square_size))
                elif piece == -1.5:
                    screen.blit(BH, (col * self.square_size, row * self.square_size))
                    # black horse
                elif piece == -1.875:
                    screen.blit(BM, (col * self.square_size, row * self.square_size))
                elif piece == -1.75:
                    screen.blit(BM, (col * self.square_size, row * self.square_size))
                    # black minister
                elif piece == -2:
                    screen.blit(BQ, (col * self.square_size, row * self.square_size))
                    # black queen
                elif piece == -1.625:
                    screen.blit(BK, (col * self.square_size, row * self.square_size))
                    # black king



                elif piece == 1.125:
                    screen.blit(WE, (col * self.square_size, row * self.square_size))
                elif piece == 1.25:
                    screen.blit(WE, (col * self.square_size, row * self.square_size))
                    # white elephant
                elif piece == 0.125:
                    screen.blit(WP, (col * self.square_size, row * self.square_size))
                elif piece == 0.25:
                    screen.blit(WP, (col * self.square_size, row * self.square_size))
                elif piece == 0.375:
                    screen.blit(WP, (col * self.square_size, row * self.square_size))
                elif piece == 0.5:
                    screen.blit(WP, (col * self.square_size, row * self.square_size))
                elif piece == 0.625:
                    screen.blit(WP, (col * self.square_size, row * self.square_size))
                elif piece == 0.75:
                    screen.blit(WP, (col * self.square_size, row * self.square_size))
                elif piece == 0.875:
                    screen.blit(WP, (col * self.square_size, row * self.square_size))
                elif piece == 1:
                    screen.blit(WP, (col * self.square_size, row * self.square_size))
                    # white pawn
                elif piece == 1.375:
                    screen.blit(WH, (col * self.square_size, row * self.square_size))
                elif piece == 1.5:
                    screen.blit(WH, (col * self.square_size, row * self.square_size))
                    # white horse
                elif piece == 1.875:
                    screen.blit(WM, (col * self.square_size, row * self.square_size))
                elif piece == 1.75:
                    screen.blit(WM, (col * self.square_size, row * self.square_size))
                    # white minister
                elif piece == 2:
                    screen.blit(WQ, (col * self.square_size, row * self.square_size))
                    # white queen
                elif piece == 1.625:
                    screen.blit(WK, (col * self.square_size, row * self.square_size))
                    # white king


        