import numpy as np
import heapq

def task1():
    # Read input file
    with open("Input/day18.txt", "r") as file:
        bytes = []
        for line in file:
            x, y = map(int, line.strip().split(","))
            bytes.append((x, y))

    power = 1
    precise_mode = False
    byte_counter = len(bytes) // 2
    while True:
        # Initialize grid
        grid = np.zeros((71, 71))
        for i in range(byte_counter):
            byte = bytes[i]
            grid[byte[1], byte[0]] = 1

        # Build graph
        graph = {}
        for i in range(grid.shape[0]):
            for k in range(grid.shape[1]):
                pos = (i, k)
                graph[pos] = {}
                set_weights(pos, graph, grid)

        # Find shortest path using Dijkstra
        dist, path = dijkstra(graph, (0, 0), (70, 70))
        if dist == float("inf"):
            byte_counter -= 1
            precise_mode = True
        elif not precise_mode:
            power += 1
            byte_counter += len(bytes) // int(pow(2, power))
        else:
            return bytes[byte_counter]

    return dist

def set_weights(pos, graph, grid):
    rows, cols = grid.shape

    # Check neighbors and set weights for valid moves
    x, y = pos
    if x + 1 < rows and grid[x + 1, y] == 0:  # Move down
        graph[pos][(x + 1, y)] = 1
    if x - 1 >= 0 and grid[x - 1, y] == 0:  # Move up
        graph[pos][(x - 1, y)] = 1
    if y + 1 < cols and grid[x, y + 1] == 0:  # Move right
        graph[pos][(x, y + 1)] = 1
    if y - 1 >= 0 and grid[x, y - 1] == 0:  # Move left
        graph[pos][(x, y - 1)] = 1

def dijkstra(graph, start_node, end_node):
    # Initialize distances and priority queue
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]  # (current_distance, current_node)
    parents = {start_node: None}  # To reconstruct the path later

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip processing if we've already found a shorter path
        if current_distance > distances[current_node]:
            continue

        # Process neighbors
        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                parents[neighbor] = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor))

        # Early termination if we've reached the end node
        if current_node == end_node:
            break

    # Reconstruct path if needed
    path = []
    node = end_node
    while node is not None:
        path.append(node)
        node = parents.get(node)
    path.reverse()

    # Return distance and path
    if distances[end_node] == float('inf'):
        return float('inf'), []  # No path exists

    return distances[end_node], path


def main():
    print(task1())

if __name__ == "__main__":
    main()