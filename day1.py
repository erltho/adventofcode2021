#!/bin/bash


### Part one
# previous_measure = 0
# increased_measure = 0
# with open('data.txt') as file: 
#     for line in file:
#         if str(line) > str(previous_measure):
#             increased_measure += 1
#         previous_measure = line

# print(increased_measure)

### Part two
queue = []
previous_window = 0
increased = 0
with open('data.txt') as file:
    for line in file: 
        if len(queue) < 3:
            queue.append(int(line))
        elif (len(queue) == 3):
            previous_window = sum(queue)
            queue.pop(0)
            queue.append(int(line))
            if(sum(queue) > previous_window):
                increased += 1
            print("previous " + str(previous_window))
            print("queue " + str(sum(queue)))
print("increased part two: " + str(increased))
        

