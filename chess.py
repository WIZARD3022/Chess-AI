# import pygame
# GREEN = (0, 255, 0)
# class Board:
#     def __init__(self, width, height, screen):
#         self.width = width
#         self.height = height
#         self.turn = "white"  # or 'black'
#         self.old_x = None
#         self.old_y = None
#         self.valid = None
#         self.square_size = min(width, height) // 8
#         self.board = [
#             [-1.125,-1.375,-1.875,-2,-1.625,-1.75,-1.5,-1.25],
#             [-0.125,-0.25,-0.375,-0.5,-0.625,-0.75,-0.875,-1],
#             [0,0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0,0],
#             [0.125,0.25,0.375,0.5,0.625,0.75,0.875,1],
#             [1.125,1.375,1.875,2,1.625,1.75,1.5,1.25]
#         ]
#         self.init_board(screen)

#     def select_square(self, mouse_x, mouse_y, screen):
#         col = mouse_x // self.square_size
#         row = mouse_y // self.square_size
#         if 0 <= row < 8 and 0 <= col < 8:
#             piece = self.board[row][col]
#             if piece == 0:
#                 if (self.old_x is not None and self.old_y is not None and (row, col) in self.valid):
#                     self.move_piece(self.old_y, self.old_x, row, col)
#                     self.turn = 'black' if self.turn == 'white' else 'white'
#                     self.old_x, self.old_y, self.valid = None, None, []
#                 return
#             moving = 'white' if piece > 0 else 'black'
#             if moving == self.turn:
#                 self.old_x = col
#                 self.old_y = row
#                 self.valid = self.get_valid_moves_custom((row, col))
#                 self.higlight_square(row, col, screen)

#     def unselect_square(self, col, row, screen):
#         color = (255, 255, 255) if (row + col) % 2 == 0 else (50, 100, 150)
#         pygame.draw.rect(screen, color, (col * self.square_size, row * self.square_size, self.square_size, self.square_size))

#     def move_piece(self, start_row, start_col, end_row, end_col):
#         self.board[end_row][end_col], self.board[start_row][start_col] = self.board[start_row][start_col], 0

#     def higlight_square(self, row, col, screen):
#         for x, y in self.valid:
#             if 0 <= x < 8 and 0 <= y < 8:
#                 pygame.draw.circle(screen, GREEN, (y * self.square_size + self.square_size // 2, x * self.square_size + self.square_size // 2), 10)



#     def init_board(self, screen):
        
#         for row in range(8):
#             # print(f"Drawing row {self.board[row]}")
#             for col in range(8):
#                 color = (255, 255, 255) if (row + col) % 2 == 0 else (50, 100, 150)
#                 pygame.draw.rect(screen, color, (col * self.square_size, row * self.square_size, self.square_size, self.square_size))

#     #     pass

#     # def select_square(self, mouse_x, mouse_y,screen):
#     #     print("-------------------------------------------------------")
#     #     col = mouse_x // self.square_size
#     #     row = mouse_y // self.square_size
#     #     if 0 <= row < 8 and 0 <= col < 8:
#     #         piece = self.board[row][col]
#     #         print(f"Selected piece at ({row}, {col}): {piece}")
#     #         moving = 0
#     #         if piece >= 0:
#     #             moving = 'white'
#     #         elif piece <= 0:
#     #             moving = 'black'
            
#     #         if moving == self.turn:
#     #             print(f"Moving piece: {piece} for {self.turn}")
#     #             pygame.draw.rect(screen, (255, 0, 0), (col * self.square_size, row * self.square_size, self.square_size, self.square_size), 3)
#     #             if self.old_x is not None and self.old_y is not None:
#     #                 self.unselect_square(self.old_x, self.old_y, screen)
#     #             self.old_x = col
#     #             self.old_y = row
#     #             print(f"Old position set to: ({self.old_y}, {self.old_x})")
#     #                 # self.unhiglight_square(row, col, screen)
#     #             print(f"Valid moves: {self.valid}")
#     #             if self.valid is not None:
#     #                 for (col, row) in self.valid:
#     #                     print(f"valid Move piece from ({self.old_x}, {self.old_y}) to ({row}, {col})")
#     #                     self.move_piece(self.old_y, self.old_x, row, col)  # Example move logic
#     #                     self.turn = 'black' if self.turn == 'white' else 'white'
#     #                 if piece == 0:
#     #                     print("No piece selected")
#     #                     self.old_x = None
#     #                     self.old_y = None
#     #                     self.valid = None
#     #                     self.unselect_square(col, row, screen)
#     #             else:
#     #                 print(f"Cannot move {piece} for {self.turn}, it's {moving}'s turn")
#     #             # if piece == 0:
#     #             self.higlight_square(row, col, screen)
#     #             print(f"Valid moves: {self.valid}")
#     #     else:
#     #         print("Clicked outside the board")

#     # def unselect_square(self, col, row, screen):
#     #     if 0 <= row < 8 and 0 <= col < 8:
#     #         if (row + col) % 2 == 0:
#     #             pygame.draw.rect(screen, (255, 255, 255), (col * self.square_size, row * self.square_size, self.square_size, self.square_size))
#     #         else:
#     #             pygame.draw.rect(screen, (50, 100, 150), (col * self.square_size, row * self.square_size, self.square_size, self.square_size))

#     # def start_game(self):
#     #     # Initialize the game state and pieces
#     #     END = False
#     #     while END:
#     #         print("Game is running")
#     #         print(f"Current turn: {turn} select a piece")
#     #         turn = 'black' if turn == 'white' else 'white'

#     #     pass

#     # def move_piece(self, start_row, start_col, end_row, end_col):
#     #     # Move a piece from (start_row, start_col) to (end_row, end_col)
        
#     #     # piece = self.board[start_row][start_col]
#     #     # self.board[start_row][start_col] = 0
#     #     # self.board[end_row][end_col] = piece
#     #     self.board[end_row][end_col], self.board[start_row][start_col] = self.board[start_row][start_col], self.board[end_row][end_col]
#     #     print(f"Moved piece from ({start_row}, {start_col}) to ({end_row}, {end_col})")
#     #     for i in range(8):
#     #         print(self.board[i])

#     # def higlight_square(self, row, col, screen):
#     #     # Highlight the square at (row, col) with a red border
#     #     if self.valid is not None:
#     #         for x, y in self.valid:
#     #             if 0 <= x < 8 and 0 <= y < 8:
#     #                 if (x + y) % 2 == 0:
#     #                     pygame.draw.circle(screen, (255, 255, 255), (y * self.square_size + self.square_size // 2, x * self.square_size + self.square_size // 2), 10)
#     #                 else:
#     #                     pygame.draw.circle(screen, (50, 100, 150), (y * self.square_size + self.square_size // 2, x * self.square_size + self.square_size // 2), 10)
#     #     self.valid = self.get_valid_moves_custom((row, col))
#     #     for x, y in self.valid:
#     #         if 0 <= x < 8 and 0 <= y < 8:
#     #                 pygame.draw.circle(screen, GREEN, (y * self.square_size + self.square_size // 2, x * self.square_size + self.square_size // 2), 10)

#     def dashboard(self, screen):
#         # Draw the dashboard with game information
#         font = pygame.font.SysFont(None, 36)
#         pygame.draw.rect(screen, (0, 0, 0), (900, 0, 550, 800))  # Dashboard background
#         text = font.render(f"Turn: {self.turn}, old :{self.old_x,self.old_y}", True, (255, 255, 255))
#         screen.blit(text, (950, 50))
#         # Add more dashboard elements as needed

#     def get_valid_moves_custom(self, pos):
#         row, col = pos
#         piece = self.board[row][col]

#         if piece == 0:
#             return []

#         is_white = piece > 0
#         moves = []

#         def is_valid(r, c):
#             return 0 <= r < 8 and 0 <= c < 8

#         def is_empty(r, c):
#             return self.board[r][c] == 0

#         def is_opponent(r, c):
#             return self.board[r][c] < 0 if is_white else self.board[r][c] > 0

#         # Pawn Logic
#         if abs(piece) >= 0.125 and abs(piece) <= 1:
#             direction = -1 if is_white else 1
#             start_row = 6 if is_white else 1

#             # Forward move
#             if is_valid(row + direction, col) and is_empty(row + direction, col):
#                 moves.append((row + direction, col))
#                 # Two-square move from start
#                 if row == start_row and is_empty(row + 2 * direction, col):
#                     moves.append((row + 2 * direction, col))

#             # Diagonal captures
#             for dc in [-1, 1]:
#                 r, c = row + direction, col + dc
#                 if is_valid(r, c) and is_opponent(r, c):
#                     moves.append((r, c))

#         # Rook Logic
#         elif abs(piece) in [1.125, 1.25]:
#             directions = [(1,0), (-1,0), (0,1), (0,-1)]
#             for dr, dc in directions:
#                 r, c = row + dr, col + dc
#                 while is_valid(r, c):
#                     if is_empty(r, c):
#                         moves.append((r, c))
#                     elif is_opponent(r, c):
#                         moves.append((r, c))
#                         break
#                     else:
#                         break
#                     r += dr
#                     c += dc

#         # Knight Logic
#         elif abs(piece) in [1.375, 1.5]:
#             deltas = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
#             for dr, dc in deltas:
#                 r, c = row + dr, col + dc
#                 if is_valid(r, c) and (is_empty(r, c) or is_opponent(r, c)):
#                     moves.append((r, c))

#         # Bishop (Minister) Logic
#         elif abs(piece) in [1.875, 1.75]:
#             directions = [(1,1), (-1,-1), (1,-1), (-1,1)]
#             for dr, dc in directions:
#                 r, c = row + dr, col + dc
#                 while is_valid(r, c):
#                     if is_empty(r, c):
#                         moves.append((r, c))
#                     elif is_opponent(r, c):
#                         moves.append((r, c))
#                         break
#                     else:
#                         break
#                     r += dr
#                     c += dc

#         # Queen Logic
#         elif abs(piece) == 2:
#             directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
#             for dr, dc in directions:
#                 r, c = row + dr, col + dc
#                 while is_valid(r, c):
#                     if is_empty(r, c):
#                         moves.append((r, c))
#                     elif is_opponent(r, c):
#                         moves.append((r, c))
#                         break
#                     else:
#                         break
#                     r += dr
#                     c += dc

#         # King Logic
#         elif abs(piece) == 1.625:
#             directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
#             for dr, dc in directions:
#                 r, c = row + dr, col + dc
#                 if is_valid(r, c) and (is_empty(r, c) or is_opponent(r, c)):
#                     moves.append((r, c))
#             # (Optional) Castling can be added here

#         return moves
import pygame

GREEN = (0, 255, 0)

class Board:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.turn = "white"  # 'white' or 'black'
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
        for i in range(8):
            print(self.board[i])
        self.draw(self.screen)

    def capture_piece(self, captured_piece, row, col):
        # For now, just print what was captured
        print(f"Captured piece {captured_piece} at ({row}, {col})")
        
        # You could later store captured pieces like this:
        # self.captured_pieces.append((captured_piece, row, col))

        # Optional: flash or animate capture location
        pygame.draw.rect(self.screen, (255, 0, 0), (col * self.square_size, row * self.square_size, self.square_size, self.square_size))

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
        pygame.draw.rect(screen, (0, 0, 0), (900, 0, 550, 800))
        text = font.render(f"Turn: {self.turn}, Selected: {self.old_x, self.old_y}", True, (255, 255, 255))
        screen.blit(text, (950, 50))


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



