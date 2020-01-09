import numpy as np
import pygame
import sys
import time
import math

# ------------------------------------------------------------------------ #
N = 9
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
                                               #(left, top, width, height)
    pygame.draw.rect(screen, WHITE, (0, 0, 9 * SQUARESIZE, 9.50 * SQUARESIZE))
    for i in range(N + 1):
        if(i % 3 == 0):
            pygame.draw.rect(screen, BLACK, (i * SQUARESIZE, 0, 3, 9.50 * SQUARESIZE))
            pygame.draw.rect(screen, BLACK, (0, i * SQUARESIZE, 9 * SQUARESIZE, 3))
        else:
            pygame.draw.rect(screen, BLACK, (i * SQUARESIZE, 0, 1, 9 * SQUARESIZE))
            pygame.draw.rect(screen, BLACK, (0, i * SQUARESIZE, 9 * SQUARESIZE, 1))
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

def find_empty_location(grid,l):
    for row in range(N):
        for col in range(N):
            if(grid[row][col]==0):
                l[0]=row
                l[1]=col
                return True
    return False

def is_safe(grid, row, col, num):
    row_safe = True
    col_safe = True
    box_safe = True

    for i in range(N):
        if(grid[row][i] == num):
            row_safe = False

    for j in range(N):
        if(grid[j][col] == num):
            col_safe = False

    for k in range((int)(math.sqrt(N))):
        for m in range((int)(math.sqrt(N))):
            if(grid[k + (row - row%3)][m + (col - col%3)] == num):
                box_safe = False

    return row_safe and col_safe and box_safe

def solve_sudoku(grid):
    l = [0, 0]

    if(not find_empty_location(grid,l)):
        return True

    row=l[0]
    col=l[1]

    for num in range(1, N + 1):
        if(is_safe(grid,row,col,num)):
            grid[row][col]=num
            pygame.display.update()
            print(board)

            #print_board(board)
            if(solve_sudoku(grid)):
                return True
            grid[row][col] = 0
    return False

def print_board(board):
    for col in range(N):
        for row in range(N):
            if grid[row][col] != 0:
                gridLabel = sudokuFont.render(str(grid[row][col]), 1, BLACK)

                screen.blit(gridLabel, (col * SQUARESIZE + SQUARESIZE/2 - 8, row * SQUARESIZE + SQUARESIZE/2 - 8))
                pygame.display.update()
    pygame.display.update()



inputMode = True
board = create_board()
print(board)
clock = pygame.time.Clock()
pygame.init()
height = (int)(SQUARESIZE * (N + 0.5))
screen_size = (9 * SQUARESIZE, height)
screen = pygame.display.set_mode(screen_size)
draw_board(board)
pygame.display.update()
titleFont = pygame.font.SysFont("Century Gothic", 75)
descriptionFont = pygame.font.SysFont("Century Gothic", 22)
buttonFont = pygame.font.SysFont("Century Gothic", 35)
sudokuFont = pygame.font.SysFont("Century Gothic", 35)
grid = [[0 for x in range(9)]for y in range(9)]

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
                    draw_board(board)
                    print(board)
                    pygame.display.update()
                    print_board(board)

                    grid=[[3,0,6,5,0,8,4,0,0],
                          [5,2,0,0,0,0,0,0,0],
                          [0,8,7,0,0,0,0,3,1],
                          [0,0,3,0,1,0,0,8,0],
                          [9,0,0,8,6,3,0,0,5],
                          [0,5,0,0,9,0,6,0,0],
                          [1,3,0,0,0,0,2,5,0],
                          [0,0,0,0,0,0,0,7,4],
                          [0,0,5,2,0,6,3,0,0]]
                    if(solve_sudoku(grid)):
                        print("DONE!")
                        print(count)
                    else:
                        print("No solution")

                    # Run the backtracking algorithm
                    #nqueen_run(board, 0)
                # Quit
                if 285 < posx < 285 + 1.2 * SQUARESIZE and 362 < posy < 400:
                    sys.exit()
                # Increment N
                if 300 < posx < 310 and 338 < posy < 348:
                    N = N + 1
                # Decrement N
                if 210 < posx < 220 and 338 < posy < 348:
                    if N > 4:
                        N = N - 1
