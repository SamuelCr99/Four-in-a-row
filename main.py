import pygame
import numpy
from pygame.constants import KEYDOWN, MOUSEBUTTONDOWN

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

WIDTH, HEIGHT = 700, 600
CIRCLE_RADIUS = 45
OFFSET = 50
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def draw_screen(win, game_field):
    win.fill(BLUE)
    for x in range(7):
        for y in range(6):
            if game_field[x][y] == 1:
                pygame.draw.circle(
                    win, RED, (x*100+OFFSET, y*100+OFFSET), CIRCLE_RADIUS, 0)
            elif game_field[x][y] == 2:
                pygame.draw.circle(
                    win, YELLOW, (x*100+OFFSET, y*100+OFFSET), CIRCLE_RADIUS, 0)

            else:
                pygame.draw.circle(
                    win, WHITE, (x*100+OFFSET, y*100+OFFSET), CIRCLE_RADIUS, 0)

    pygame.display.update()


def swap_player(player):
    if player == 1:
        return 2
    return 1


def get_depth(game_field, x_value):
    for depth in range(6):
        if game_field[x_value][depth] == 1 or game_field[x_value][depth] == 2:
            return depth - 1
    return 5


def check_winner(game_field): #TODO this is some very bad code and should probably be fixed up 
    for y in range(6):
        for x in range(3):
            value = game_field[x][y]
            if value != 1 and value != 2:
                continue
            count = 0
            for dx in range(1, 4):
                if game_field[x+dx][y] == value:
                    count += 1
            if count == 3:
                return True
    for x in range(7):  # TODO 
        for y in range(3):
            value = game_field[x][y]
            if value != 1 and value != 2:
                continue
            count = 0
            for dy in range(1, 4):
                if game_field[x][y+dy] == value:
                    count += 1
            if count == 3:
                return True
    for x in range(7):
        for y in range(6):
            value = game_field[x][y]
            if value != 1 and value != 2:
                continue
            count = 0
            for dy in range(1, 4):
                try:
                    if game_field[x+dy][y+dy] == value:
                        count += 1
                except:
                    break
            if count == 3:
                return True

    for x in range(7):
        for y in range(6):
            value = game_field[x][y]
            if value != 1 and value != 2:
                continue
            count = 0
            for dy in range(1, 4):
                try:
                    if game_field[x-dy][y+dy] == value:
                        count += 1
                except:
                    break
            if count == 3:
                return True

    return False


def main():
    game_field = numpy.empty((7, 6))
    player = 1
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                x_value = (int(mouse_pos[0]/(WIDTH/7)))
                y_value = get_depth(game_field, x_value)
                if x_value > -1 and y_value > -1:
                    game_field[x_value][y_value] = player
                player = swap_player(player)
        draw_screen(WIN, game_field)
        if check_winner(game_field) == True:
            pygame.quit()
        pygame.display.update


if __name__ == "__main__":
    main()
