import numpy as np
import pygame
import sys
import time

N = 5
START_ROW = 0
START_COLUMN = 0
# Global Variables
SQUARESIZE = 100
GREY = (176, 176, 176)
DARK = (190, 190, 190)
LIGHT = (130, 130, 130)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BORDER = (41, 54, 63)
RADIUS = int(SQUARESIZE / 2 - 5)


def create_board():
    board = np.zeros((N, N))
    return board


def draw_board(board):
    if inputMode == True:
        alternate = False
        for column in range(5):
            for row in range(5):
                if alternate == False:
                                                    #(left, top, width, height)
                    pygame.draw.rect(screen, WHITE, (column * SQUARESIZE, (row - 1) * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                else:
                    pygame.draw.rect(screen, GREY, (column * SQUARESIZE, (row - 1) * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                alternate = not alternate

    else:
        alternate = False
        for column in range(N):
            for row in range(N):
                if alternate == False:
                    pygame.draw.rect(screen, WHITE, (column * SQUARESIZE, (row - 1) * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                else:
                    pygame.draw.rect(screen, GREY, (column * SQUARESIZE, (row - 1) * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                alternate = not alternate
            if N % 2 == 0:
                alternate = not alternate
    pygame.display.update()


def input_screen(board):

    title_image = pygame.image.load(r'resources/title_knights_tour.png')
    surface = pygame.image.load(r'resources/parchment.jpg')
    surface = pygame.transform.scale(surface, (400, 350))

    pygame.draw.rect(screen, BLACK, (45, 75, 410, 360))
    # pygame.draw.rect(screen, WHITE, (0.5 * SQUARESIZE, 1.15 * SQUARESIZE, 4 * SQUARESIZE, 3 * SQUARESIZE))

    # Increment N Button:
    pygame.draw.polygon(surface, BLACK, ((265, 227), (275, 232), (265, 237)))

    # Decrement N Button:
    pygame.draw.polygon(surface, BLACK, ((155, 227), (145, 232), (155, 237)))

    # Increment Row Button:
    pygame.draw.polygon(surface, BLACK, ((265, 247), (275, 252), (265, 257)))

    # Decrement Row Button:
    pygame.draw.polygon(surface, BLACK, ((155, 247), (145, 252), (155, 257)))

    # Increment Col Button:
    pygame.draw.polygon(surface, BLACK, ((265, 267), (275, 272), (265, 277)))

    # Decrement Col Button:
    pygame.draw.polygon(surface, BLACK, ((155, 267), (145, 272), (155, 277)))

    # Build Button:
    pygame.draw.rect(surface, GREY, (236, 292, 118, 40))

    # Quit Button:
    pygame.draw.rect(surface, GREY, (35, 292, 118, 40))

    descriptionLabel1 = descriptionFont.render("The knights tour is a sequence of moves of a knight", 1, BLACK)
    descriptionLabel2 = descriptionFont.render("on a chessboard such that the knight visits every", 1, BLACK)
    descriptionLabel3 = descriptionFont.render("square only once. If the knight ends on a square that", 1, BLACK)
    descriptionLabel4 = descriptionFont.render("is one knight's move from the beginning square (so ", 1, BLACK)
    descriptionLabel5 = descriptionFont.render("that it could tour the board again immediately, ", 1, BLACK)
    descriptionLabel6 = descriptionFont.render("following the same path), the tour is closed;", 1, BLACK)
    descriptionLabel7 = descriptionFont.render("otherwise, it is open.", 1, BLACK)

    inputLabel1 = descriptionFont.render("NxN board size: ", 1, BLACK)
    inputLabel2 = descriptionFont.render("Starting Row: ", 1, BLACK)
    inputLabel3 = descriptionFont.render("Starting Column: ", 1, BLACK)

    currentNLabel = descriptionFont.render("N = " + str(N), 1, BLACK)
    currentRowLabel = descriptionFont.render("Row = " + str(START_ROW + 1), 1, BLACK)
    currentColumnLabel = descriptionFont.render("Col = " + str(START_COLUMN + 1), 1, BLACK)

    buttonLabel1 = buttonFont.render("BUILD", 1, BORDER)
    buttonLabel2 = buttonFont.render("QUIT", 1, BORDER)

    screen.blit(surface, (50, 80))
    screen.blit(title_image, (55, 105))

    screen.blit(descriptionLabel1, (65, 185))
    screen.blit(descriptionLabel2, (65, 200))
    screen.blit(descriptionLabel3, (65, 215))
    screen.blit(descriptionLabel4, (65, 230))
    screen.blit(descriptionLabel5, (65, 245))
    screen.blit(descriptionLabel6, (65, 260))
    screen.blit(descriptionLabel7, (65, 275))

    screen.blit(inputLabel1, (65, 305))
    screen.blit(inputLabel2, (65, 325))
    screen.blit(inputLabel3, (65, 345))

    screen.blit(currentNLabel, (235, 305))
    screen.blit(currentRowLabel, (235, 325))
    screen.blit(currentColumnLabel, (235, 345))

    screen.blit(buttonLabel1, (108, 381))
    screen.blit(buttonLabel2, (2.85 * 108 + 8, 381))

    pygame.display.update()


def place_knight(board, row, col):
    board[row][col] = 1


def print_board(board):
    image = pygame.image.load(r'resources/queen_symbol.png')
    image = pygame.transform.scale(image, (50, 50))
    for col in range(N):
        for row in range(N):
            if board[row][col] == 1:
                screen.blit(image, (int(col * SQUARESIZE + SQUARESIZE / 4), int((row) * SQUARESIZE + SQUARESIZE / 4)))
                # pygame.draw.circle(screen, BLACK, (int(col * SQUARESIZE + SQUARESIZE / 2), int((row - 1) * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()


inputMode = True
board = create_board()
print(board)

clock = pygame.time.Clock()
pygame.init()
screen_size = (5 * SQUARESIZE, 5 * SQUARESIZE)
screen = pygame.display.set_mode(screen_size)
draw_board(board)
pygame.display.update()

titleFont = pygame.font.SysFont("Century Gothic", 75)
descriptionFont = pygame.font.SysFont("Century Gothic", 22)
buttonFont = pygame.font.SysFont("Century Gothic", 35)


while(1):
    for event in pygame.event.get():
        if inputMode == True:
            input_screen(board)

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            posx = event.pos[0]
            posy = event.pos[1]
            if inputMode == True:
                # Build Button Hover
                if 85 < posx < 205 and 362 < posy < 400:
                    pygame.draw.rect(screen, DARK, (0.85 * SQUARESIZE + 1, 3.62 * SQUARESIZE + 11, 1.2 * SQUARESIZE - 2, 0.4 * SQUARESIZE - 2))
                    buttonLabel1 = buttonFont.render("BUILD", 1, BORDER)
                    screen.blit(buttonLabel1, (108, 381))
                    pygame.display.update()
                # Quit Button Hover
                if 285 < posx < 285 + 1.2 * SQUARESIZE and 362 < posy < 400:
                    pygame.draw.rect(screen, DARK, (2.85 * SQUARESIZE + 1, 3.62 * SQUARESIZE + 11, 1.2 * SQUARESIZE - 2, 0.4 * SQUARESIZE - 2))
                    buttonLabel2 = buttonFont.render("QUIT", 1, BORDER)
                    screen.blit(buttonLabel2, (2.85 * 108 + 8, 381))
                    pygame.display.update()
                # Increment N Hover
                if 300 < posx < 325 and 300 < posy < 325:
                    pygame.draw.polygon(screen, DARK, ((315, 307), (325, 312), (315, 317)))
                    pygame.display.update()
                # Decrement N Hover
                if 175 < posx < 205 and 300 < posy < 325:
                    pygame.draw.polygon(screen, DARK, ((205, 307), (195, 312), (205, 317)))
                    pygame.display.update()
                # Increment Starting Row
                if 300 < posx < 325 and 320 < posy < 345:
                    pygame.draw.polygon(screen, DARK, ((315, 327), (325, 332), (315, 337)))
                    pygame.display.update()
                # Decrement Starting Row
                if 175 < posx < 205 and 320 < posy < 345:
                    pygame.draw.polygon(screen, DARK, ((205, 327), (195, 332), (205, 337)))
                    pygame.display.update()
                # Increment Starting Col
                if 300 < posx < 325 and 340 < posy < 365:
                    pygame.draw.polygon(screen, DARK, ((315, 347), (325, 352), (315, 357)))
                    pygame.display.update()
                # Decrement Starting Col
                if 175 < posx < 205 and 340 < posy < 365:
                    pygame.draw.polygon(screen, DARK, ((205, 347), (195, 352), (205, 357)))
                    pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = event.pos[0]
            posy = event.pos[1]
            if inputMode == True:
                # Build
                if 85 < posx < 205 and 362 < posy < 400:
                    inputMode = False
                    board = create_board()
                    screen_size = (N * SQUARESIZE, N * SQUARESIZE)
                    screen = pygame.display.set_mode(screen_size)
                    draw_board(board)
                    pygame.display.update()

                    # Run the backtracking algorithm
                    # nqueen_run(board, 0)
                # Quit
                if 285 < posx < 285 + 1.2 * SQUARESIZE and 362 < posy < 400:
                    sys.exit()

                # Increment N
                if 300 < posx < 325 and 300 < posy < 325:
                    N = N + 1
                # Decrement N
                if 175 < posx < 205 and 300 < posy < 325:
                    if N > 3:
                        if START_ROW == N - 1:
                            START_ROW = START_ROW - 1
                        if START_COLUMN == N - 1:
                            START_COLUMN = START_COLUMN - 1
                        N = N - 1
                # Increment Starting Row
                if 300 < posx < 325 and 320 < posy < 345:
                    if START_ROW < N - 1:
                        START_ROW = START_ROW + 1
                # Decrement Starting Row
                if 175 < posx < 205 and 320 < posy < 345:
                    if START_ROW > 0:
                        START_ROW = START_ROW - 1
                # Increment Starting Col
                if 300 < posx < 325 and 340 < posy < 365:
                    if START_COLUMN < N - 1:
                        START_COLUMN = START_COLUMN + 1
                # Decrement Starting Col
                if 175 < posx < 205 and 340 < posy < 365:
                    if START_COLUMN > 0:
                        START_COLUMN = START_COLUMN - 1

    pygame.display.update()
    clock.tick(1)
