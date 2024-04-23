import pygame

height = 640
width = 640
rows = 8
cols = 8
square_size = width//cols
fps = 60

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
grey = (128,128,128)
background = (240, 236, 121)

crown = pygame.transform.scale(pygame.image.load('assets\king.png'),(44,25))
