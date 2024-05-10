import pygame
import sys

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
ROWS = 4
COLS = 4
SQUARE_SIZE = SCREEN_WIDTH // COLS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("16 Guti")

# Board representation
board = [['-' for _ in range(COLS)] for _ in range(ROWS)]

# Function to draw the board
def draw_board():
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)
    pygame.display.update()

# Main game loop
def main():
    draw_board()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
