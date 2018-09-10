# The graphical interface for the Tetris game. We used python 3 as the environment for this project.

import pygame
import random
import sys


# board configuration
cell_size = 20
columns = 10
rows = 23
maxfps = 60
time = 25
# piecesamplesize = 250

colors = [

    (0, 255, 255),
    (0, 0, 255),
    (255, 140, 0),
    (255, 255, 0),
    (124, 252, 0),
    (128, 0, 128),
    (255, 0, 0)

]

tetris_shapes = [
    [[1,1,1,1]],

    [[2,0,0],
     [2,2,2]],

    [[0, 0, 3],
     [3, 3, 3]],

    [[4, 4],
     [4, 4]]

    [[0, 5, 5],
     [5, 5, 0]],

    [[6, 6, 6],
     [0, 6, 0]],

    [[7, 7, 0],
     [0, 7, 7]]
]
