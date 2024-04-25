import pygame
from cheakers.board import Board
from cheakers.constants import red,white,grey,blue,square_size
from cheakers.piece import piece

class Game:
    def __init__(self,win):
        self.selected = None
        self.board = Board()
        self.turn =  red
        self.valid_moves = {}
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def reset(self):
        self.selected = None
        self.board = Board()
        self.turn =  red
        self.valid_moves = {}

    def winner(self):
        if self.red_left <= 0:
            return white
        else:
            return red
        
        return None

    def select(self,row,col):
        if self.selected:
            result = self._move(row,col)
            if not result:
                self.selected = None
                self.select(row,col)
        
        
        piece = self.board.get_piece(row,col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
            
        return False
    
    def _move(self,row,col):
        piece = self.board.get_piece(row,col)
        if self.selected and piece == 0 and (row,col) in self.valid_moves:
            self.board.move(self.selected,row,col)
            skipped = self.valid_moves[(row,col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        
        return True
        
    
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == white:
            self.turn = red
        else:
            self.turn = white



    def draw_valid_moves(self,moves):
        for move in moves:
            row,col = move
            pygame.draw.circle(self.win,blue,(col*square_size + square_size//2,row*square_size + square_size//2),15)




