#!/bin/bash/python3

import statistics as s
import math

with open("data/day7-data.txt", "r") as f:
    input = f.read() # Read all file in case values are not on a single line
    raw_data = input.split(",")  # Convert strings to ints


data = list(map(int, raw_data))
data.sort()
median = s.median(data)

sum = 0
for elem in data:
    sum += int(abs(elem - median))



### Part 2

avg = s.mean(data)
print(s.mean(data))
sum = 0
for elem in data:
    diff = int(abs(elem - math.floor(avg)))
    for i in range(diff):
        sum += i + 1

print(sum)
