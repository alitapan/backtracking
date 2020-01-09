import numpy as np
import pygame
import sys
import time

# ------------------------------------------------------------------------ #
N = 5
# ------------------------------------------------------------------------ #

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

    image = pygame.image.load(r'resources/queen.png')
    image = pygame.transform.scale(image, (50, 50))

    pygame.draw.rect(screen, BORDER, (0.5 * SQUARESIZE - 5, 1.15 * SQUARESIZE - 5, 4 * SQUARESIZE + 10, 3 * SQUARESIZE + 10))
    pygame.draw.rect(screen, BLACK, (0.5 * SQUARESIZE, 1.15 * SQUARESIZE, 4 * SQUARESIZE, 3 * SQUARESIZE))

    # Increment N Button:
    pygame.draw.polygon(screen, WHITE, ((300, 338), (310, 343), (300, 348)))

    # Decrement N Button:
    pygame.draw.polygon(screen, WHITE, ((220, 338), (210, 343), (220, 348)))

    # Build Button:
    pygame.draw.rect(screen, BORDER, (0.85 * SQUARESIZE, 3.62 * SQUARESIZE, 1.2 * SQUARESIZE, 0.4 * SQUARESIZE))
    pygame.draw.rect(screen, WHITE, (0.85 * SQUARESIZE + 1, 3.62 * SQUARESIZE + 1, 1.2 * SQUARESIZE - 2, 0.4 * SQUARESIZE - 2))

    # Quit Button:
    pygame.draw.rect(screen, BORDER, (2.85 * SQUARESIZE, 3.62 * SQUARESIZE, 1.2 * SQUARESIZE, 0.4 * SQUARESIZE))
    pygame.draw.rect(screen, WHITE, (2.85 * SQUARESIZE + 1, 3.62 * SQUARESIZE + 1, 1.2 * SQUARESIZE - 2, 0.4 * SQUARESIZE - 2))

    titleLabel = titleFont.render("N-QUEENS", 1, WHITE)

    descriptionLabel1 = descriptionFont.render("The n-queens puzzle is the problem of placing N", 1, WHITE)
    descriptionLabel2 = descriptionFont.render("queens on an N×N chessboard such that no two ", 1, WHITE)
    descriptionLabel3 = descriptionFont.render("queens attack each other.", 1, WHITE)

    inputLabel1 = descriptionFont.render("Number of rows and columns can be changed", 1, WHITE)
    inputLabel2 = descriptionFont.render("simply from here:", 1, WHITE)

    currentNLabel = descriptionFont.render("N = " + str(N), 1, WHITE)

    buttonLabel1 = buttonFont.render("BUILD", 1, BORDER)
    buttonLabel2 = buttonFont.render("QUIT", 1, BORDER)

    screen.blit(image, (80, 165))
    screen.blit(titleLabel, (135, 170))
    screen.blit(descriptionLabel1, (75, 235))
    screen.blit(descriptionLabel2, (75, 255))
    screen.blit(descriptionLabel3, (75, 275))
    screen.blit(inputLabel1, (75, 315))
    screen.blit(inputLabel2, (75, 335))
    screen.blit(currentNLabel, (240, 337))
    screen.blit(buttonLabel1, (108, 371))
    screen.blit(buttonLabel2, (2.85 * 108 + 8, 371))

    pygame.display.update()


def place_queen(board, row, col):
    board[row][col] = 1


def is_safe(board, currentRow, currentCol):
    # Check same column
    for col in range(currentCol):
        if board[currentRow][col] == 1:
            return False
    # Check diagonals
    for i, j in zip(range(currentRow, N, 1), range(currentCol, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(currentRow, -1, -1), range(currentCol, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def nqueen_run(board, col):
    if col >= N:
        print_board(board)
        return True
    for row in range(N):
        if is_safe(board, row, col):
            place_queen(board, row, col)
            print(board)
            # pygame.event.pump()
            # print_board(board)
            pygame.display.update()
            if nqueen_run(board, col + 1):
                return True
            board[row][col] = 0
    return False


def print_board(board):
    image = pygame.image.load(r'resources/queen_symbol.png')
    image = pygame.transform.scale(image, (50, 50))

    for col in range(N):
        for row in range(N):
            if board[row][col] == 1:
                pygame.event.pump()
                pygame.time.wait(500)
                screen.blit(image, (int(col * SQUARESIZE + SQUARESIZE / 4), int((row) * SQUARESIZE + SQUARESIZE / 4)))
                pygame.display.update()
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
                    pygame.draw.rect(screen, DARK, (0.85 * SQUARESIZE + 1, 3.62 * SQUARESIZE + 1, 1.2 * SQUARESIZE - 2, 0.4 * SQUARESIZE - 2))
                    buttonLabel1 = buttonFont.render("BUILD", 1, BORDER)
                    screen.blit(buttonLabel1, (108, 371))
                    pygame.display.update()
                # Quit Button Hover
                if 285 < posx < 285 + 1.2 * SQUARESIZE and 362 < posy < 400:
                    pygame.draw.rect(screen, DARK, (2.85 * SQUARESIZE + 1, 3.62 * SQUARESIZE + 1, 1.2 * SQUARESIZE - 2, 0.4 * SQUARESIZE - 2))
                    buttonLabel2 = buttonFont.render("QUIT", 1, BORDER)
                    screen.blit(buttonLabel2, (2.85 * 108 + 8, 371))
                    pygame.display.update()
                # Increment N Hover
                if 295 < posx < 315 and 335 < posy < 352:
                    pygame.draw.polygon(screen, DARK, ((300, 338), (310, 343), (300, 348)))
                    pygame.display.update()
                # Decrement N Hover
                if 205 < posx < 225 and 335 < posy < 352:
                    pygame.draw.polygon(screen, DARK, ((220, 338), (210, 343), (220, 348)))
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
                    nqueen_run(board, 0)
                # Quit
                if 285 < posx < 285 + 1.2 * SQUARESIZE and 362 < posy < 400:
                    sys.exit()
                # Increment N
                if 300 < posx < 310 and 338 < posy < 348:
                    N = N + 1
                # Decrement N
                if 210 < posx < 220 and 338 < posy < 348:
                    if N > 3:
                        N = N - 1
