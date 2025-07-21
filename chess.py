import pygame
import copy
import sys
GREEN = (0, 255, 0)
class Board:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.turn = "white"
        self.old_x = None
        self.old_y = None
        self.valid = []
        self.screen = screen
        self.square_size = min(width, height) // 8
        self.board = [
            [-1.125, -1.375, -1.875, -2, -1.625, -1.75, -1.5, -1.25],
            [-0.125, -0.25, -0.375, -0.5, -0.625, -0.75, -0.875, -1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1],
            [1.125, 1.375, 1.875, 2, 1.625, 1.75, 1.5, 1.25]
        ]
        self.point = [0, 0]
        self.init_board(screen)
        self.draw(screen)

    def init_board(self, screen):
        for row in range(8):
            for col in range(8):
                color = (255, 255, 255) if (row + col) % 2 == 0 else (50, 100, 150)
                pygame.draw.rect(screen, color, (col * self.square_size, row * self.square_size, self.square_size, self.square_size))

    def select_square(self, mouse_x, mouse_y, screen):
        col = mouse_x // self.square_size
        row = mouse_y // self.square_size
        print(f"Clicked on square: ({row}, {col})")
        if 0 <= row < 8 and 0 <= col < 8:
            piece = self.board[row][col]
            # if piece == 0:
            if (self.old_x is not None and self.old_y is not None and (row, col) in self.valid):
                self.move_piece(self.old_y, self.old_x, row, col)
                self.turn = 'black' if self.turn == 'white' else 'white'
                self.old_x, self.old_y, self.valid = None, None, []
                return
            moving = 'white' if piece > 0 else 'black'
            if moving == self.turn:
                self.old_x = col
                self.old_y = row
                self.valid = self.get_valid_moves_custom((row, col))
                print(f"Valid moves for piece at ({row}, {col}): {self.valid}")
                self.higlight_square(row, col, screen)

    def unselect_square(self, col, row, screen):
        color = (255, 255, 255) if (row + col) % 2 == 0 else (50, 100, 150)
        pygame.draw.rect(screen, color, (col * self.square_size, row * self.square_size, self.square_size, self.square_size))

    def move_piece(self, start_row, start_col, end_row, end_col):
        moving_piece = self.board[start_row][start_col]
        target_piece = self.board[end_row][end_col]

        if target_piece != 0:  # Capturing enemy try
            self.capture_piece(target_piece, end_row, end_col)

        self.board[end_row][end_col] = moving_piece
        self.board[start_row][start_col] = 0
        # for i in range(8):
        #     print(self.board[i])
        self.draw(self.screen)

        


    def capture_piece(self, captured_piece, row, col):
        # For now, just print what was captured
        print(f"Captured piece {captured_piece} at ({row}, {col})")
        if captured_piece < 0:
            print("Captured a black piece")
            self.point[0] += abs(captured_piece)
        else:
            print("Captured a white piece")
            self.point[1] += abs(captured_piece)
        # You could later store captured pieces like this:
        # self.captured_pieces.append((captured_piece, row, col))

        # Optional: flash or animate capture location
        # pygame.draw.rect(self.screen, (255, 0, 0), (col * self.square_size, row * self.square_size, self.square_size, self.square_size))

    def higlight_square(self, row, col, screen):
        for x, y in self.valid:
            if 0 <= x < 8 and 0 <= y < 8:
                pygame.draw.circle(screen, GREEN, (y * self.square_size + self.square_size // 2, x * self.square_size + self.square_size // 2), 10)

    def get_valid_moves_custom(self, pos):
        moves = []
        r, c = pos
        piece = self.board[r][c]
        is_white = piece > 0
        direction = -1 if is_white else 1

        def inside(x, y): return 0 <= x < 8 and 0 <= y < 8
        def empty(x, y): return self.board[x][y] == 0
        def enemy(x, y): return (self.board[x][y] < 0 if is_white else self.board[x][y] > 0)

        if abs(piece) <= 1:  # Pawn
            if inside(r + direction, c) and empty(r + direction, c):
                moves.append((r + direction, c))
                if (r == 6 and is_white) or (r == 1 and not is_white):
                    if empty(r + 2 * direction, c):
                        moves.append((r + 2 * direction, c))
            for dc in [-1, 1]:
                if inside(r + direction, c + dc) and enemy(r + direction, c + dc):
                    moves.append((r + direction, c + dc))

        elif abs(piece) in [1.125, 1.25]:  # Rook
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                for i in range(1, 8):
                    nr, nc = r + dr*i, c + dc*i
                    if not inside(nr, nc): break
                    if empty(nr, nc):
                        moves.append((nr, nc))
                    elif enemy(nr, nc):
                        moves.append((nr, nc)); break
                    else: break

        elif abs(piece) in [1.375, 1.5]:  # Knight
            for dr, dc in [(2, 1), (1, 2), (-1, 2), (-2, 1),
                           (-2, -1), (-1, -2), (1, -2), (2, -1)]:
                nr, nc = r + dr, c + dc
                if inside(nr, nc) and (empty(nr, nc) or enemy(nr, nc)):
                    moves.append((nr, nc))

        elif abs(piece) in [1.875, 1.75]:  # Bishop
            for dr, dc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                for i in range(1, 8):
                    nr, nc = r + dr*i, c + dc*i
                    if not inside(nr, nc): break
                    if empty(nr, nc):
                        moves.append((nr, nc))
                    elif enemy(nr, nc):
                        moves.append((nr, nc)); break
                    else: break

        elif abs(piece) == 2:  # Queen
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1),
                           (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                for i in range(1, 8):
                    nr, nc = r + dr*i, c + dc*i
                    if not inside(nr, nc): break
                    if empty(nr, nc):
                        moves.append((nr, nc))
                    elif enemy(nr, nc):
                        moves.append((nr, nc)); break
                    else: break

        elif abs(piece) == 1.625:  # King
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0: continue
                    nr, nc = r + dr, c + dc
                    if inside(nr, nc) and (empty(nr, nc) or enemy(nr, nc)):
                        moves.append((nr, nc))

        return moves

    def dashboard(self, screen):
        font = pygame.font.SysFont(None, 36)
        pygame.draw.rect(screen, (0, 0, 0), (900, 0, 550, 120))
        text1 = font.render(f"Turn: {self.turn}, Selected: {self.old_x, self.old_y}", True, (255, 255, 255))
        screen.blit(text1, (950, 50))
        text2 = font.render(f"Black Score: {self.point[1]}, Black Score: {self.point[0]}", True, (255, 255, 255))
        screen.blit(text2, (950, 90))

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
                color = (255, 255, 255) if (row + col) % 2 == 0 else (50, 100, 150)
                if piece == 0:
                    pygame.draw.rect(screen, color, (col * self.square_size, row * self.square_size, self.square_size, self.square_size))
                elif piece == -1.125:
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



