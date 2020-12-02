import pygame
from checkers.config import WIDTH, HEIGHT, SQUARE_SIZE, RED
from checkers.game import Game
from helpers import get_row_col_from_mouse

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        winner = game.winner()
        if winner != None:
            print(winner)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(mouse_pos)
                game.select(row, col)

        game.update()

    pygame.quit()


main()
