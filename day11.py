#!/bin/bash/python3
import numpy as np

raw_grid = []
with open('data/day11-data.txt') as file: 
    for line in file:
        row = list(line.strip())
        raw_grid.append(row)
        
grid = np.array(raw_grid).astype(int)


did_it_flash = {}
print(grid.shape)
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

def increase_grid(matrix):
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]): 
            matrix[x,y] = int(matrix[x,y]) + 1

def flash(matrix):
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            key = [x,y]
            did_it_flash[str(key)] = False
            if(matrix[x,y] > 9):
                did_it_flash[str(key)] = True
                adj = adj_finder(matrix,[x,y])
                for elem in adj:
                    matrix[elem] += 1

def control_flash(matrix):
    while True:
        for x in range(matrix.shape[0]):
            for y in range(matrix.shape[1]):
                key = [x,y]
                if (did_it_flash[str(key)] == False and matrix[x,y] > 9):
                    adj = adj_finder(matrix,[x,y])
                    for elem in adj:
                        matrix[elem] += 1
                    did_it_flash[str(key)] = True
        if evaluate_end_condition(matrix):
            break
    did_it_flash.clear()

def evaluate_end_condition(matrix):
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            key = [x,y]
            if (did_it_flash[str(key)] == False and matrix[x,y] > 9):
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
#         control_flash(matrix)
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
        control_flash(matrix)
        flashes = reset_flashed(matrix)
        if flashes == grid_size:
            print(index)
            break

main(grid)