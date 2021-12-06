#!/bin/bash/python3
from collections import defaultdict

fish_data = defaultdict(int)

with open("data/day6-data.txt", "r") as f:
    input = f.read() # Read all file in case values are not on a single line
    fish_raw_data = [ int(x) for x in input.split(",") ] # Convert strings to ints
    for i in fish_raw_data:
        fish_data[i] += 1

for day in range(256):
    tmp_fish_data = defaultdict(int)
    for fish_state, count in fish_data.items():
        if fish_state == 0:
            print( "fish state: " + str(fish_state) + " count: " + str(count) )
            tmp_fish_data[8] += count
            tmp_fish_data[6] += count
        else:
            tmp_fish_data[fish_state -1] += count
    fish_data = tmp_fish_data

print(sum(fish_data.values()))






# print(str(len(data_set)))

# for i in range(256):
#     li= 0
#     n = len(data_set)
#     while li < n:
#         if data_set[li] == 0:
#             data_set[li] = 6
#             data_set.append(8)
#         else:
#             data_set[li] -= 1
#         li += 1
# print(str(len(data_set)))

# def solve(fish, days):

