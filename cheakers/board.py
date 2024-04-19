import pygame
from cheakers.constants import black, rows, cols, square_size, red

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0

    def draw_board(self, win):
        win.fill(black)
        for row in range(rows):
            for col in range(row % 2, rows, 2):
                pygame.draw.rect(win, red, (row * square_size, col * square_size, square_size, square_size))

    
    