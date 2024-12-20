import heapq
from collections import defaultdict
def task1():
    file = open("Input/day16.txt", "r")
    raw_map = []
    graph = {}
    positions_to_nodes = {}
    for line in file:
        raw_map.append(list(line.replace("\n", "")))

    start_node = None
    end_node = None
    current_node_id = 0

    for i in range(len(raw_map)):
        for k in range(len(raw_map[0])):
            if raw_map[i][k] == ".":
                current_node_id = create_nodes_for_position((i,k), graph, positions_to_nodes, current_node_id)
            elif raw_map[i][k] == "S":
                start_node = current_node_id + 3 # faxing east
                current_node_id = create_nodes_for_position((i,k), graph, positions_to_nodes, current_node_id)
            elif raw_map[i][k] == "E":
                positions_to_nodes[(i,k)] = {
                    "North": current_node_id,
                    "West": current_node_id,
                    "South": current_node_id,
                    "East": current_node_id
                }
                end_node = current_node_id
                graph[current_node_id] = {}
                current_node_id += 1

    for position, nodes in positions_to_nodes.items():
        if (position[0] - 1, position[1]) in positions_to_nodes:
            neighbor_id = positions_to_nodes[(position[0] - 1, position[1])]["North"]
            graph[nodes["North"]][neighbor_id] = 1
        if (position[0] + 1, position[1]) in positions_to_nodes:
            neighbor_id = positions_to_nodes[(position[0] + 1, position[1])]["South"]
            graph[nodes["South"]][neighbor_id] = 1
        if (position[0], position[1] - 1) in positions_to_nodes:
            neighbor_id = positions_to_nodes[(position[0], position[1] - 1)]["West"]
            graph[nodes["West"]][neighbor_id] = 1
        if (position[0], position[1] + 1) in positions_to_nodes:
            neighbor_id = positions_to_nodes[(position[0], position[1] + 1)]["East"]
            graph[nodes["East"]][neighbor_id] = 1

    cost, paths = dijkstra(graph, start_node, end_node)

    best_places = []
    for path in paths:
        for id in path:
            for pos, nodes in positions_to_nodes.items():
                if id in nodes.values():
                    if pos not in best_places:
                        best_places.append(pos)
                    break

    return len(best_places)



def create_nodes_for_position(position, graph, positions_to_nodes, current_node_id):
    graph[current_node_id] = {
        current_node_id + 1: 1000,
        current_node_id + 2: 2000,
        current_node_id + 3: 1000
    }
    positions_to_nodes[position] = {
        "North" : current_node_id
    }
    current_node_id += 1
    graph[current_node_id] = {
        current_node_id - 1: 1000,
        current_node_id + 1: 1000,
        current_node_id + 2: 2000
    }
    positions_to_nodes[position]["West"] = current_node_id
    current_node_id += 1
    graph[current_node_id] = {
        current_node_id - 2: 2000,
        current_node_id - 1: 1000,
        current_node_id + 1: 1000
    }
    positions_to_nodes[position]["South"] = current_node_id
    current_node_id += 1
    graph[current_node_id] = {
        current_node_id - 3: 1000,
        current_node_id - 2: 2000,
        current_node_id - 1: 1000
    }
    positions_to_nodes[position]["East"] = current_node_id
    current_node_id += 1

    return current_node_id

def dijkstra(graph, start_node, end_node):
    # Initialize distances and priority queue
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]  # (current_distance, current_node)
    parents = defaultdict(list)  # To store multiple parents for each node

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip processing if we've already found a shorter path
        if current_distance > distances[current_node]:
            continue

        # Process neighbors
        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                # Found a better path; update distances and reset parents
                distances[neighbor] = new_distance
                parents[neighbor] = [current_node]
                heapq.heappush(priority_queue, (new_distance, neighbor))
            elif new_distance == distances[neighbor]:
                # Found an equally good path; add this parent
                parents[neighbor].append(current_node)

    # Reconstruct all paths from end_node to start_node
    def reconstruct_paths(node, path):
        if node == start_node:
            return [[start_node] + path]
        all_paths = []
        for parent in parents[node]:
            all_paths.extend(reconstruct_paths(parent, [node] + path))
        return all_paths

    all_optimal_paths = reconstruct_paths(end_node, [])

    return distances[end_node], all_optimal_paths

def main():
    print(task1())

if __name__ == "__main__":
    main()