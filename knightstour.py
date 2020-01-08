import numpy as np
import pygame
import sys
import math

N = 10

board = np.zeros((5, 5))

for row in range(5):
    for col in range(5):
        if row + col < 5:
            board[row - col][col] = 1
print(board)

# def create_board():
#     board = np.zeros()
