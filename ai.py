import pygame
import sys
from chess import Board

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)
BROWN = (165, 42, 42)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
DARK_GRAY = (169, 169, 169)
DARK_BLUE = (0, 0, 139)
DARK_GREEN = (0, 100, 0)
DARK_RED = (139, 0, 0)
DARK_PINK = (255, 20, 147)

class AI():
    def __init__(self, width, height, screen, b):
        self.width = width
        self.height = height
        self.screen = screen
        self.board = b.board
        self.weight = 0.5
        self.learning_rate = 0.1
        self.epochs = 1000
        self.draw(screen)

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW, (800, 120, self.width, self.height))
        count = 0
        for i in range(8):
            # print(self.board[i])
            for _ in range(8):
                count += 1
                piece = self.board[i][_]
                if piece == 0:
                    color = WHITE
                    # empty square

                elif piece == -1.125:
                    color = PURPLE
                elif piece == -1.25:
                    color = PURPLE
                    # black elephant
                elif piece == -0.125:
                    color = DARK_GRAY
                elif piece == -0.25:
                    color = DARK_GRAY
                elif piece == -0.375:
                    color = DARK_GRAY
                elif piece == -0.5:
                    color = DARK_GRAY
                elif piece == -0.625:
                    color = DARK_GRAY
                elif piece == -0.75:
                    color = DARK_GRAY
                elif piece == -0.875:
                    color = DARK_GRAY
                elif piece == -1:
                    color = DARK_GRAY
                    # Black pawn
                elif piece == -1.375:
                    color = DARK_BLUE
                elif piece == -1.5:
                    color = DARK_BLUE
                    # black horse
                elif piece == -1.875:
                    color = DARK_GREEN
                elif piece == -1.75:
                    color = DARK_GREEN
                    # black minister
                elif piece == -2:
                    color = DARK_PINK
                    # black queen
                elif piece == -1.625:
                    color = DARK_RED
                    # black king



                elif piece == 1.125:
                    color = BROWN
                elif piece == 1.25:
                    color = BROWN
                    # white elephant
                elif piece == 0.125:
                    color = ORANGE
                elif piece == 0.25:
                    color = ORANGE
                elif piece == 0.375:
                    color = ORANGE
                elif piece == 0.5:
                    color = ORANGE
                elif piece == 0.625:
                    color = ORANGE
                elif piece == 0.75:
                    color = ORANGE
                elif piece == 0.875:
                    color = ORANGE
                elif piece == 1:
                    color = ORANGE
                    # white pawn
                elif piece == 1.375:
                    color = BLUE
                elif piece == 1.5:
                    color = BLUE
                    # white horse
                elif piece == 1.875:
                    color = GREEN
                elif piece == 1.75:
                    color = GREEN
                    # white minister
                elif piece == 2:
                    color = PINK
                    # white queen
                elif piece == 1.625:
                    color = RED
                    # white king
                
                pygame.draw.circle(screen, color, (int(825), int(135 + (count) * 10 + 5)), 5)





        pass