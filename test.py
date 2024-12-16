from helper import *

def heuristic(node, goal):
    # Simple heuristic function for testing (Manhattan distance for grid-like graphs)
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def main():
    # Create a simple 2D grid graph
    graph = Graph(symmetric=True)
    
    # Define the grid size
    rows, cols = 5, 5
    
    # Add nodes (optional, as they are added implicitly with edges)
    for i in range(rows):
        for j in range(cols):
            graph.add_node((i, j))
    
    # Add edges with distances (4-connected grid)
    for i in range(rows):
        for j in range(cols):
            if i > 0:
                graph.add_edge((i, j), (i-1, j), 1)  # Up
            if i < rows - 1:
                graph.add_edge((i, j), (i+1, j), 1)  # Down
            if j > 0:
                graph.add_edge((i, j), (i, j-1), 1)  # Left
            if j < cols - 1:
                graph.add_edge((i, j), (i, j+1), 1)  # Right
    
    # Test Dijkstra's algorithm
    start_node = (0, 0)
    goal_node = (4, 4)
    visited, path = dijkstra(graph, start_node, goal_node)
    print("Dijkstra's algorithm:")
    print("Visited nodes and distances:", visited)
    print("Path:", path)
    
    # Test A* algorithm
    visited, path = a_star(graph, start_node, goal_node, heuristic)
    print("A* algorithm:")
    print("Visited nodes and distances:", visited)
    print("Path:", path)



if __name__ == "__main__":
    main()