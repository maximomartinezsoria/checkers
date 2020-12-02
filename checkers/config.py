import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# RGB
RED = (179, 20, 20)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

crown_image = pygame.image.load('assets/crown.png')
CROWN = pygame.transform.scale(crown_image, (45, 35))
