import numpy as np
import pygame
import sys
import time
import math



# ------------------------------------------------------------------------ #
N = 9

grid = [[0 for x in range(N)]for y in range(N)]

#Change to the board can be manually made from here
grid=[[3,0,6,5,0,8,4,0,0],
      [5,2,0,0,0,0,0,0,0],
      [0,8,7,0,0,0,0,3,1],
      [0,0,3,0,1,0,0,8,0],
      [9,0,0,8,6,3,0,0,5],
      [0,5,0,0,9,0,6,0,0],
      [1,3,0,0,0,0,2,5,0],
      [0,0,0,0,0,0,0,7,4],
      [0,0,5,2,0,6,3,0,0]]

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
    pygame.draw.rect(screen, WHITE, (0, 0, N * SQUARESIZE, (N + 0.5) * SQUARESIZE))
    for i in range(N + 1):
        if(i % 3 == 0):
            pygame.draw.rect(screen, BLACK, (i * SQUARESIZE, 0, 3, (N + 0.5) * SQUARESIZE))
            pygame.draw.rect(screen, BLACK, (0, i * SQUARESIZE, N * SQUARESIZE, 3))
        else:
            pygame.draw.rect(screen, BLACK, (i * SQUARESIZE, 0, 1, N * SQUARESIZE))
            pygame.draw.rect(screen, BLACK, (0, i * SQUARESIZE, N * SQUARESIZE, 1))
    pygame.display.update()


def input_screen(board):

    title_image = pygame.image.load(r'resources/sudoku.png')
   #title_image = pygame.transform.scale(title_image, ()

    pygame.draw.rect(screen, RED, ((math.sqrt(N) - 1) * SQUARESIZE - 5, 1.15 * SQUARESIZE - 5, (math.sqrt(N) + 2) * SQUARESIZE + 10, ((math.sqrt(N) + 1)) * SQUARESIZE + 10))
    pygame.draw.rect(screen, BLACK, ((math.sqrt(N) - 1) * SQUARESIZE, 1.15 * SQUARESIZE, (math.sqrt(N) + 2) * SQUARESIZE, ((math.sqrt(N) + 1)) * SQUARESIZE))


    # Build Button:
    pygame.draw.rect(screen, BORDER, (290, 4.2 * SQUARESIZE, 1.2 * SQUARESIZE, 0.4 * SQUARESIZE))
    pygame.draw.rect(screen, WHITE, (290 + 1, 4.2 * SQUARESIZE + 1, 1.2 * SQUARESIZE - 2, 0.4 * SQUARESIZE - 2))

    # Quit Button:
    pygame.draw.rect(screen, BORDER, (490, 4.2 * SQUARESIZE, 1.2 * SQUARESIZE, 0.4 * SQUARESIZE))
    pygame.draw.rect(screen, WHITE, (490, 4.2 * SQUARESIZE + 1, 1.2 * SQUARESIZE - 2, 0.4 * SQUARESIZE - 2))


    descriptionLabel1 = descriptionFont.render("This program is a sudoku solver using", 1, WHITE)
    descriptionLabel2 = descriptionFont.render("backtracking algorithm. You may change", 1, WHITE)
    descriptionLabel3 = descriptionFont.render("the sudoku board from the source file.", 1, WHITE)



    buttonLabel1 = buttonFont.render("SOLVE", 1, BORDER)
    buttonLabel2 = buttonFont.render("QUIT", 1, BORDER)

    screen.blit(title_image, (190, 165))
    screen.blit(descriptionLabel1, (300, 285))
    screen.blit(descriptionLabel2, (300, 305))
    screen.blit(descriptionLabel3, (300, 325))
    screen.blit(buttonLabel1, (310, 429))
    screen.blit(buttonLabel2, (515, 429))

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
            grid[row][col]= num
            print(grid)
            if(solve_sudoku(grid)):
                return True
            grid[row][col] = 0
    return False

def print_board(board, grid):
    for col in range(N):
        for row in range(N):
            if grid[row][col] != 0:
                gridLabel = sudokuFont.render(str(grid[row][col]), 1, BLACK)
                pygame.event.pump()
                pygame.time.wait(1)
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
                if 280 < posx < 420 and 415 < posy < 460:
                    pygame.draw.rect(screen, DARK, (290 + 1, 4.2 * SQUARESIZE + 1, 1.2 * SQUARESIZE - 2, 0.4 * SQUARESIZE - 2))
                    buttonLabel1 = buttonFont.render("BUILD", 1, BORDER)
                    screen.blit(buttonLabel1, (310, 429))
                    pygame.display.update()
                # Quit Button Hover
                if 480 < posx < 620 and 415 < posy < 460:
                    pygame.draw.rect(screen, DARK, (490, 4.2 * SQUARESIZE + 1, 1.2 * SQUARESIZE - 2, 0.4 * SQUARESIZE - 2))
                    buttonLabel2 = buttonFont.render("QUIT", 1, BORDER)
                    screen.blit(buttonLabel2, (515, 429))
                    pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = event.pos[0]
            posy = event.pos[1]
            if inputMode == True:
                # Build
                if 280 < posx < 420 and 415 < posy < 460:
                    inputMode = False

                    draw_board(board)
                    print(grid)
                    pygame.display.update()
                    print_board(board, grid)

                    if(solve_sudoku(grid)):
                        print_board(board, grid)
                    else:
                        print("No solution")
                # Quit
                if 480 < posx < 620 and 415 < posy < 460:
                    sys.exit()
