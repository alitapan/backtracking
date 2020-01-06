import numpy as np
import pygame
import sys

# ------------------------------------------------------------------------ #
# Board Size for NQueens - Change the variable as you wish to any integer
N = 7
# ------------------------------------------------------------------------ #

# Global Variables
SQUARESIZE = 100
GREY = (176, 176, 176)
DARK = (190, 190, 190)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BORDER = (41, 54, 63)


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

    image = pygame.image.load(r'queen.png')
    image = pygame.transform.scale(image, (50, 50))

    pygame.draw.rect(screen, BORDER, (0.5 * SQUARESIZE - 5, 1.15 * SQUARESIZE - 5, 4 * SQUARESIZE + 10, 3 * SQUARESIZE + 10))

    pygame.draw.rect(screen, BLACK, (0.5 * SQUARESIZE, 1.15 * SQUARESIZE, 4 * SQUARESIZE, 3 * SQUARESIZE))

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
    inputLabel2 = descriptionFont.render("simply from the source code.", 1, WHITE)

    buttonLabel1 = buttonFont.render("BUILD", 1, BORDER)
    buttonLabel2 = buttonFont.render("QUIT", 1, BORDER)

    screen.blit(image, (80, 165))
    screen.blit(titleLabel, (135, 170))
    screen.blit(descriptionLabel1, (75, 235))
    screen.blit(descriptionLabel2, (75, 255))
    screen.blit(descriptionLabel3, (75, 275))
    screen.blit(inputLabel1, (75, 315))
    screen.blit(inputLabel2, (75, 335))
    screen.blit(buttonLabel1, (108, 371))
    screen.blit(buttonLabel2, (2.85 * 108 + 8, 371))

    pygame.display.update()


def placeQueen(board):
    pass


def isSafe(board, col, currentRow):
    # Check Current Column for other Queens
    for N - row in range(N, currentRow):
        if board[N - row][col] == 1:
            return False
    #for N - row in
    return True


def nqueen_run(board):
    done = False
        if queensPlaced == N:
            return
        else:
            pass


queensPlaced = 0
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
            if inputMode == True and 85 < posx < 205 and 362 < posy < 400:
                pygame.draw.rect(screen, DARK, (0.85 * SQUARESIZE + 1, 3.62 * SQUARESIZE + 1, 1.2 * SQUARESIZE - 2, 0.4 * SQUARESIZE - 2))
                buttonLabel1 = buttonFont.render("BUILD", 1, BORDER)
                screen.blit(buttonLabel1, (108, 371))
                pygame.display.update()

            if inputMode == True and 285 < posx < 285 + 1.2 * SQUARESIZE and 362 < posy < 400:
                pygame.draw.rect(screen, DARK, (2.85 * SQUARESIZE + 1, 3.62 * SQUARESIZE + 1, 1.2 * SQUARESIZE - 2, 0.4 * SQUARESIZE - 2))
                buttonLabel2 = buttonFont.render("QUIT", 1, BORDER)
                screen.blit(buttonLabel2, (2.85 * 108 + 8, 371))
                pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = event.pos[0]
            posy = event.pos[1]
            if inputMode == True:
                if 85 < posx < 205 and 362 < posy < 400:
                    inputMode = False
                    screen_size = (N * SQUARESIZE, N * SQUARESIZE)
                    screen = pygame.display.set_mode(screen_size)
                    draw_board(board)
                    pygame.display.update()
                    # nqueen_run(board)

    # 1) Start in the leftmost column
    # 2) If all queens are placed
    #     return true
    # 3) Try all rows in the current column.  Do following for every tried row.
    #     a) If the queen can be placed safely in this row then mark this [row,
    #         column] as part of the solution and recursively check if placing
    #         queen here leads to a solution.
    #     b) If placing the queen in [row, column] leads to a solution then return
    #         true.
    #     c) If placing queen doesn't lead to a solution then unmark this [row,
    #         column] (Backtrack) and go to step (a) to try other rows.
    # 3) If all rows have been tried and nothing worked, return false to trigger
    #     backtracking.
