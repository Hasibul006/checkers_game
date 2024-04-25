import pygame
from cheakers.constants import width,height,fps,square_size,red
from cheakers.board import Board
from cheakers.game import Game

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("cheakers")


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(win)


    while run:
        clock.tick(fps)

        if game.winner() != None:
            print(game.winner())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                row,col = get_row_col_from_mouse(pos)
                game.select(row,col)

        game.update()

    pygame.quit()

def get_row_col_from_mouse(pos):
    x,y = pos
    row = y//square_size
    col = x//square_size
    return row,col

main()

