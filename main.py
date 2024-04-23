import pygame
from cheakers.constants import width,height,fps,square_size
from cheakers.board import Board

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("cheakers")


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()


    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                row,col = get_row_col_from_mouse(pos)
                piece = board.get_piece(row,col)
                board.move(piece,4,3)

        board.draw(win)
        pygame.display.update()

    pygame.quit()

def get_row_col_from_mouse(pos):
    x,y = pos
    row = y//square_size
    col = x//square_size
    return row,col

main()

