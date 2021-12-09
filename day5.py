#!/bin/bash/python3

import numpy as np
import math

start_coordinates = []
end_coordinates = []
solution_matrice = np.array([],[])

vent_matrice = np.array([],[])


with open('data/day5-data.txt') as file: 
    for line in file:
        raw_tmp_start_coordinates, raw_tmp_end_coordinates = line.split("->")
        tmp_start_coordinates = raw_tmp_start_coordinates.split(",")
        tmp_end_coordinates = raw_tmp_end_coordinates.split(",")
        if (if_not_diagonal(tmp_start_coordinates, tmp_end_coordinates)):


        start_coordinates.append(tmp_start_coordinates)
        end_coordinates.append(tmp_end_coordinates)


def if_not_diagonal(start,end):
    if(start[0] == end[0] or start[1] == end[1]):
        return True
    else:
        return False



def prepare_data(list):
    list_coordinates_x = []
    list_coordinates_y = []
    for elem in list:
        value_coordinates_x, vaule_coordinates_y = elem.split(",")
        list_coordinates_x.append(value_coordinates_x.strip())
        list_coordinates_y.append(vaule_coordinates_y.strip())

    return list_coordinates_x, list_coordinates_y

start_coordinates = prepare_data(start_coordinates)
end_coordinates = prepare_data(end_coordinates)



def solution(start_list, end_list):
    print(start_list[0])
    for i in range(len(start_list[0])):
        print(str(start_list[0][i]) + "and" + str(end_list[0][i]))
        if (start_list[0][i] == end_list[0][i]):
            if (start_list[1][i] > end_list[1][i]):
                print(start_list[1][i])
                range_loop = int(start_list[1][i])-int(end_list[1][i])
                for coordinate in range(range_loop):
                    solution_matrice[int(end_list[0][i + coordinate]), int(end_list[1][i] += 1)]
            if (start_list[1][i] < end_list[1][i]):
                for coordinate in range(end_list[1][i] - start_list[1][i] + 1): #TODO: refactor this to be not redundant. Move for loop above, with absolute value. 
                    solution_matrice[start_list[0][i + coordinate], start_list[1][i]] += 1

solution(start_coordinates, end_coordinates)
print(solution_matrice)