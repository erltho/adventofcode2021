#!/bin/bash/python3

### Part 1

from os import fdopen
import numpy as np
import os

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



### Part 2
ox_gen = []
c02_scrub = []
with open('data/day3-data.txt') as file: 
    for line in file:
            ox_gen.append(line.strip())
            c02_scrub.append(line.strip())

# print(c02_scrub)
# def iterate_over_list(list, most_or_least):
#     for i in range(0, 12):
#         line_index = 0
#         number_of_elem = 0
#         num_b_one = 0
#         num_b_zero = 0
#         for line in list:
#             if line[i] == '1':
#                 num_b_one += 1
#             else:
#                 num_b_zero += 1
#         if (num_b_one > num_b_zero):
#             most_common_bit = '1'
#             least_common_bit = '0'
#         else: 
#             most_common_bit = '0'
#             least_common_bit = '1'
#         while line_index < number_of_elem:
#             element = list[line_index]
#             if (element[i] == least_common_bit and most_or_least == "most"): 
#                 list.remove(element)
#                 number_of_elem -= 1
#             elif (element[i] == most_common_bit and most_or_least == "least"):
#                 list.remove(element)
#                 number_of_elem -= 1
#             else:
#                 line_index += 1
#     return list


# print(str(iterate_over_list(ox_gen, "most")))


for i in range(0, len(gamma)):
    li = 0
    c02_i = 0
    n = len(ox_gen)
    c02_n = len(c02_scrub)
    one = 0
    zero = 0
    for line in ox_gen:
        if line[i] == '1':
            one += 1
        else:
            zero += 1
    if (one >= zero):
        most_common_bit = '1'
    else:
        most_common_bit = '0'
    while li < n:
        element = ox_gen[li]
        if element[i] != most_common_bit:
            ox_gen.remove(element)
            n -= 1
        else:
            li += 1
#     for line in c02_scrub:
#         if line[i] == '1':
#             one += 1
#         else:
#             zero += 1
#     if (one > zero):
#         least_common_bit = '0'
#     else:
#         least_common_bit = '1'
#     while c02_i < c02_n:
#         element = c02_scrub[c02_i]
#         if element[i] != least_common_bit:
#             c02_scrub.remove(element)
#             c02_n -= 1
#         else:
#             c02_i += 1
for i2 in range(0, len(gamma)):
    li2 = 0
    n2 = len(c02_scrub)
    one = 0
    zero = 0
    for line in c02_scrub:
        if line[i2] == '1':
            one += 1
        else:
            zero += 1
    if (one >= zero):
        most_common_bit = '1'
    else:
        most_common_bit = '0'
    while li2 < n2:
        element = c02_scrub[li2]
        if (len(c02_scrub) == 1 ):
            break
        if element[i2] == most_common_bit:
            c02_scrub.remove(element)
            n2 -= 1
        else:
            li2 += 1



print(ox_gen)
print(c02_scrub)
oxygen_value = int("".join(str(x) for x in ox_gen), 2)
c02_scrubber = int("".join(str(x) for x in c02_scrub), 2)
print("solution " + str(oxygen_value * c02_scrubber))
# # print(oxygen_value)