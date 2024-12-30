import heapq
from collections import defaultdict
import math
from timeit import default_timer as timer

def read_file_lines(file_name, strip_lines=False):
    with open(file_name, 'r') as f:
        lines =  []
        for line in f:
            lines.append(line)

    if strip_lines:
        lines = [line.strip() for line in lines]

    return lines

def benchmark(func):
    def wrapper(*args, **kwargs):
        start = timer()
        result = func(*args, **kwargs)
        end = timer()

        print(f'Function {func.__name__} took {(end-start)*1000:.4f}ms to complete.')
        return result
    return wrapper


def transpose(grid):
    return list(zip(*grid))

def turn_left(di, dj):
    if (di, dj) == (1,0):
        return (0,1)
    if (di, dj) == (0,1):
        return (-1,0)
    if (di, dj) == (-1,0):
        return (0,-1)
    if (di, dj) == (0,-1):
        return (1,0)
    
def turn_right(di, dj):
    if (di, dj) == (1,0):
        return (0,-1)
    if (di, dj) == (0,-1):
        return (-1,0)
    if (di, dj) == (-1,0):
        return (0,1)
    if (di, dj) == (0,1):
        return (1,0)

def is_on_grid(i,j,grid):
    return 0<=i<len(grid) and 0<=j<len(grid[0])

def coor_on_grid(coor, grid):
    return 0<=coor[0]<len(grid) and 0<=coor[1]<len(grid[0])

ADJ4 = [(1,0),(0,1),(-1,0),(0,-1)] # down, right, up, left
ADJ8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)] # down, dr , right, ru , up, ul , left, ld


class Graph:
    def __init__(self, n=0, symmetric=False):
        self.nodes = set(range(n))
        self.edges = defaultdict(list)
        self.distances = {}
        self.symmetric = symmetric

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[from_node, to_node] = distance
        if self.symmetric:
            self.edges[to_node].append(from_node)
            self.distances[to_node, from_node] = distance


def dijkstra(graph, start, goal=None):
    visited = {start: 0}
    h = [(0, start)]
    path = {}

    nodes = set(graph.nodes)

    while nodes and h:
        current_weight, min_node = heapq.heappop(h)
        try:
            while min_node not in nodes:
                current_weight, min_node = heapq.heappop(h)
        except IndexError:
            break

        nodes.remove(min_node)

        if goal == min_node:
            return visited, path

        for v in graph.edges[min_node]:
            weight = current_weight + graph.distances[min_node, v]
            if v not in visited or weight < visited[v]:
                visited[v] = weight
                heapq.heappush(h, (weight, v))
                path[v] = min_node

    return visited, path

def a_star(graph, start, goal, heuristic):
    visited = {start: 0}
    h = [(0 + heuristic(start, goal), 0, start)]
    path = {}

    nodes = set(graph.nodes)

    while nodes and h:
        _, current_weight, min_node = heapq.heappop(h)
        try:
            while min_node not in nodes:
                _, current_weight, min_node = heapq.heappop(h)
        except IndexError:
            break

        nodes.remove(min_node)

        for v in graph.edges[min_node]:
            weight = current_weight + graph.distances[min_node, v]
            if v not in visited or weight < visited[v]:
                visited[v] = weight
                heuristic_dist = heuristic(v, goal)
                heapq.heappush(h, (weight+heuristic_dist, weight, v))
                path[v] = min_node

    return visited, path

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def gcd(a, b):
    return math.gcd(a,b)