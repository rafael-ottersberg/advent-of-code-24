import time
import random

# Define grid size
rows, cols = 10000, 10000

# Initialize 2D array (list of lists)
grid = [[0 for _ in range(cols)] for _ in range(rows)]

# Initialize set with pairs
occupied_positions = set()

# Populate the grid and set with random positions
for _ in range(10000):
    r = random.randint(0, rows - 1)
    c = random.randint(0, cols - 1)
    grid[r][c] = 1
    occupied_positions.add((r, c))

# Access speed test for 2D array
start_time = time.time()
for _ in range(10000):
    r = random.randint(0, rows - 1)
    c = random.randint(0, cols - 1)
    value = grid[r][c]
end_time = time.time()
print(f"2D array access time: {end_time - start_time:.6f} seconds")

# Access speed test for set with pairs
start_time = time.time()
for _ in range(10000):
    r = random.randint(0, rows - 1)
    c = random.randint(0, cols - 1)
    value = (r, c) in occupied_positions
end_time = time.time()
print(f"Set with pairs access time: {end_time - start_time:.6f} seconds")