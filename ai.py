import pygame
import sys
from chess import Board

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)




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
                if count == 64:
                    pygame.draw.circle(screen, BLACK, (int(825), int(135 + (count) * 10 + 5)), 5)
                else:
                    pygame.draw.circle(screen, WHITE, (int(825), int(135 + (count) * 10 + 5)), 5)
        pass