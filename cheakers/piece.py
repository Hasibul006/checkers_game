from .constants import black,white,red,blue,rows,cols,square_size,grey,background,crown
import pygame
class piece:
    def __init__(self,row,col,color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = self.col*square_size+square_size//2
        self.y = self.row*square_size+square_size//2

    def make_king(self):
        self.king = True

    def draw(self,win):
        radius = square_size//2 - 15
        pygame.draw.circle(win, background, (self.x,self.y), radius+2)
        pygame.draw.circle(win, self.color, (self.x,self.y), radius-3)
        if(self.king == True):
            win.blit(crown,(self.x - crown.get_width()//2,self.y - crown.get_height()//2))

    def move(self,row,col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self) -> str:
        return str(self.color)