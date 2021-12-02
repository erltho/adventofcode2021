#!/bin/bash/python3

### Part 1
x = 0
y = 0

with open('data/day2-data.txt') as file: 
    for line in file:
        data = line.split(" ", 1)
        command = data[0]
        value = int(data[1])
        match command: 
            case 'up': 
                y -= value
            case 'down':
                y += value
            case 'forward':
                x += value

print("Part 1: " + str(x*y))

### Part 2

x = 0
y = 0
aim = 0

with open('data/day2-data.txt') as file: 
    for line in file:
        data = line.split(" ", 1)
        command = data[0]
        value = int(data[1])
        match command: 
            case 'up': 
                aim -= value
            case 'down':
                aim += value
            case 'forward':
                x += value
                y += aim * value

print("Part 2: " + str(x*y))