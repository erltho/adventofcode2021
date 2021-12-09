#!/bin/bash/python3

import statistics as s

with open("data/day7-data.txt", "r") as f:
    input = f.read() # Read all file in case values are not on a single line
    print(input)
    raw_data = input.split(",")  # Convert strings to ints


raw_data.sort()
data = list(map(int, raw_data))
print(raw_data)
print(type(raw_data))
median = s.median(data)
print(median)
