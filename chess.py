import pygame

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.init_board()

    def init_board(self):
        # Initialize the chess board with pieces
        # This is a placeholder for actual piece initialization
        pass

    def draw(self, screen):
        # Draw the chess board on the screen
        square_size = min(self.width, self.height) // 8
        for row in range(8):
            for col in range(8):
                color = (255, 255, 255) if (row + col) % 2 == 0 else (0, 0, 0)
                pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))