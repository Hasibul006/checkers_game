import pygame
from cheakers.constants import black, rows, cols, square_size, red,white,grey
from cheakers.piece import piece

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.grey_kings = self.white_kings = 0
        self.create_board()

    def draw_board(self, win):
        win.fill(black)
        for row in range(rows):
            for col in range(row % 2, rows, 2):
                pygame.draw.rect(win, red, (row * square_size, col * square_size, square_size, square_size))

    def create_board(self):
        for row in range(rows):
            self.board.append([])
            for col in range(cols):
                if col % 2 == ((row + 1)%2):
                    if row<3:
                        self.board[row].append(piece(row,col,white))
                    elif row>4:
                        self.board[row].append(piece(row,col,grey))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self,win):
        self.draw_board(win)
        for row in range(rows):
            for col in range(cols):
                piece = self.board[row][col]
                if(piece!=0):
                    piece.draw(win)

    def move(self, piece, row, col):
        temp = self.board[piece.row][piece.col]
        self.board[piece.row][piece.col] = self.board[row][col]
        self.board[row][col]= temp
        piece.move(row,col)

        if row == rows or row == 0:
            piece.make_king()
            if piece.color == white:
                self.white_kings += 1
            else:
                self.grey_kings+=1

    def get_piece(self,row,col):
        return self.board[row][col]

