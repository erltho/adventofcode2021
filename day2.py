#!/bin/bash/python3

### Part 1
x = y = 0

with open('data/day2-data.txt') as file: 
    for line in file:
        command, value = line.split()
        value = int(value)
        match command: 
            case 'up': 
                y -= value
            case 'down':
                y += value
            case 'forward':
                x += value

print("Part 1: " + str(x*y))

### Part 2

x = y = aim = 0

with open('data/day2-data.txt') as file: 
    for line in file:
        command, value = line.split()
        value = int(value)
        match command: 
            case 'up': 
                aim -= value
            case 'down':
                aim += value
            case 'forward':
                x += value
                y += aim * value

print("Part 2: " + str(x*y))