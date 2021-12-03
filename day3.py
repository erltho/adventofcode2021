#!/bin/bash/python3

### Part 1

tmp_byte_one = [0,0,0,0,0,0,0,0,0,0,0,0]
tmp_byte_zero = [0,0,0,0,0,0,0,0,0,0,0,0]
gamma = [0,0,0,0,0,0,0,0,0,0,0,0]
epsilon = [0,0,0,0,0,0,0,0,0,0,0,0]

i = 0

with open('data/day3-data.txt') as file: 
    for line in file:
        for char in line:
            if (char == "1"):
                tmp_byte_one[i] += 1
            if (char == "0" ):
                tmp_byte_zero[i] += 1
            i += 1
        i = 0

for i in range(0, len(tmp_byte_one)):
    if tmp_byte_one[i] > tmp_byte_zero[i]:
        gamma[i] = 1
    else:
        gamma[i] = 0
        

for i in range(0, len(gamma)):
    if gamma[i] == 1:
        epsilon[i] = 0
    else:
        epsilon[i] = 1

gamma_value = int("".join(str(x) for x in gamma), 2)
epsilon_value = int("".join(str(x) for x in epsilon), 2)

print("Solution: " + str(gamma_value * epsilon_value))
