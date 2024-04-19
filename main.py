import pygame
from cheakers.constants import width,height,fps
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
                pass

        board.draw_board(win)
        pygame.display.update()

    pygame.quit()

main()

