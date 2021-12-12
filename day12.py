#!/bin/bash/python3

from collections import defaultdict

def read_input(graph): 
    with open("data/day12-data.txt", "r") as file:
        for line in file:
            u,v = line.split("-")
            addEdge(graph,u.strip(),v.strip())
            addEdge(graph,v.strip(),u.strip())

def addEdge(graph,u,v):
	graph[u].append(v)


def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path or node.isupper():
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

def main():
    graph = defaultdict(list)
    read_input(graph)
    paths = find_all_paths(graph,"start","end")
    return len(paths)

print(main())
