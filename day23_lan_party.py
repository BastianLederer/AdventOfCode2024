import time


def generate_rdf():
    file = open("Input/day23.txt", "r")
    output = open("rdf/day23_graph.ttl", "w")
    output.write("@prefix lan:    <http://example.org/lan/> .")
    for line in file:
        line_split = line.replace("\n", "").split("-")
        rdf_triple = f"lan:{line_split[0]} lan:connectedTo lan:{line_split[1]} .\n"
        rdf_triple_reversed = f"lan:{line_split[1]} lan:connectedTo lan:{line_split[0]} .\n"
        output.write(rdf_triple)
        output.write(rdf_triple_reversed)

def task2():
    file = open("Input/day23.txt", "r")
    graph = {}
    for line in file:
        line_split = line.replace("\n", "").split("-")
        if line_split[0] not in graph.keys():
            graph[line_split[0]] = {line_split[1]}
        else:
            graph[line_split[0]].add(line_split[1])

        if line_split[1] not in graph.keys():
            graph[line_split[1]] = {line_split[0]}
        else:
            graph[line_split[1]].add(line_split[0])

    largest_subgraph = []
    for node in graph.keys():
        subgraph = create_subgraph(node, graph)
        if len(subgraph) > len(largest_subgraph):
            largest_subgraph = subgraph

    largest_subgraph = sorted(largest_subgraph)
    return ",".join(largest_subgraph)

def create_subgraph(start_node, graph):
    subgraph = [start_node]
    prev_node_count = 0
    current_node_count = 1
    while current_node_count > prev_node_count:
        prev_node_count = current_node_count
        for node, edges in graph.items():
            node_connected = True
            for connected_node in subgraph:
                if connected_node not in edges:
                    node_connected = False
                    break
            if node_connected:
                subgraph.append(node)
                current_node_count += 1

    return subgraph
def main():
    t = time.perf_counter()
    print(task2())
    print(time.perf_counter()-t)

if __name__ == "__main__":
    main()