#!/bin/bash/python3
import numpy as np

draw_number = []

raw_grid = []

with open('data/day4-data.txt') as file: 
    draw_numer = file.readline()
    i = 0
    while (line := file.readline()):
        if(line == "\n"):



grid = np.array(raw_grid).astype(int)

def increase_grid(matrix):
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]): 
            matrix[x,y] = matrix[x,y] + 1
            did_it_flash[str([x,y])] = False

def flash(matrix):
    while True:
        for x in range(matrix.shape[0]):
            for y in range(matrix.shape[1]):
                if(matrix[x,y] > 9 and did_it_flash[str([x,y])] == False ):
                    adj = adj_finder(matrix,[x,y])
                    for elem in adj:
                        matrix[elem] += 1
                    did_it_flash[str([x,y])] = True
        if evaluate_end_condition(matrix):
            break
    did_it_flash.clear

def adj_finder(matrix, position):
    adj = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            rangeX = range(0, matrix.shape[0])  # X bounds
            rangeY = range(0, matrix.shape[1])  # Y bounds
            
            (newX, newY) = (position[0]+dx, position[1]+dy)  # adjacent cell
            
            if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                adj.append((newX, newY))
    return adj

def evaluate_end_condition(matrix):
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            if (did_it_flash[str([x,y])] == False and matrix[x,y] > 9):
                return False
    return True


def reset_flashed(matrix):
    flashed = 0
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            if(matrix[x,y] > 9):
                flashed += 1
                matrix[x,y] = 0
    return flashed


# def main(matrix, steps):
#     flashed = 0
#     for i in range(steps):
#         increase_grid(matrix)
#         flash(matrix)
#         flashed += reset_flashed(matrix)
#     return flashed

# print(main(grid, 100))


## part 2

def main(matrix):
    grid_size = grid.shape[0]*grid.shape[1]
    index = 0
    while True:
        index += 1
        increase_grid(matrix)
        flash(matrix)
        flashes = reset_flashed(matrix)
        if flashes == grid_size:
            return index
            break

print(main(grid))