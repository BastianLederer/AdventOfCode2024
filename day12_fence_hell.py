def task1():
    file = open("Input/day12.txt", "r")
    map = []
    for line in file:
        map.append(list(line.replace("\n", "")))
    total = 0
    for i in range(len(map)):
        for k in range(len(map[0])):
            total += calculate_value((i,k), map)

    return total


def calculate_value(pos, map):
    char = map[pos[0]][pos[1]]
    if map[pos[0]][pos[1]] == ".":
        return 0
    plant_positions = [pos]
    prev_plant_count = 0
    while prev_plant_count < len(plant_positions):
        prev_plant_count = len(plant_positions)
        for position in plant_positions:
            i = position[0]
            k = position[1]
            if i  > 0 and map[i - 1][k] == char and (i-1,k) not in plant_positions:
                plant_positions.append((i-1,k))
                map[i-1][k] = "."
            if k  > 0 and map[i][k - 1] == char and (i,k-1) not in plant_positions:
                plant_positions.append((i,k-1))
                map[i][k-1] = "."
            if i + 1 < len(map) and map[i + 1][k] == char and (i+1,k) not in plant_positions:
                plant_positions.append((i+1,k))
                map[i + 1][k] = "."
            if k + 1 < len(map[0]) and map[i][k + 1] == char and (i,k+1) not in plant_positions:
                plant_positions.append((i,k+1))
                map[i][k+1] = "."

    min_i = None
    max_i = None
    min_k = None
    max_k = None
    for position in plant_positions:
        if min_i is None or position[0] < min_i:
            min_i = position[0]
        if max_i is None or position[0] > max_i:
            max_i = position[0]
        if min_k is None or position[1] < min_k:
            min_k = position[1]
        if max_k is None or position[1] > max_k:
            max_k = position[1]

    region_map = [None] * (max_i - min_i + 3)
    for i in range(len(region_map)):
        region_map[i] = ["."] * (max_k - min_k + 3)

    for position in plant_positions:
        region_map[position[0] - min_i + 1][position[1] - min_k + 1] = char

    border_points = []

    perimeter = 0
    for i in range(len(region_map)):
        for k in range(len(region_map[0])):
            if region_map[i][k] == ".":
                # Check cardinal directions
                if i > 0 and region_map[i - 1][k] != ".":
                    border_points.append((i, k))
                    perimeter += 1
                if k > 0 and region_map[i][k - 1] != ".":
                    border_points.append((i, k))
                    perimeter += 1
                if i + 1 < len(region_map) - 1 and region_map[i + 1][k] != ".":
                    border_points.append((i, k))
                    perimeter += 1
                if k + 1 < len(region_map[0]) - 1 and region_map[i][k + 1] != ".":
                    border_points.append((i, k))
                    perimeter += 1

                # Check diagonal directions (no increment to perimeter)
                if i > 0 and k > 0 and region_map[i - 1][k - 1] != ".":
                    border_points.append((i, k))
                if i > 0 and k + 1 < len(region_map[0]) and region_map[i - 1][k + 1] != ".":
                    border_points.append((i, k))
                if i + 1 < len(region_map) - 1 and k > 0 and region_map[i + 1][k - 1] != ".":
                    border_points.append((i, k))
                if i + 1 < len(region_map) - 1 and k + 1 < len(region_map[0]) and region_map[i + 1][k + 1] != ".":
                    border_points.append((i, k))

    region_map = [None] * (max_i - min_i + 3)
    for i in range(len(region_map)):
        region_map[i] = ["."] * (max_k - min_k + 3)

    for position in plant_positions:
        region_map[position[0] - min_i + 1][position[1] - min_k + 1] = char

    n = 0

    for position in plant_positions:
        n += calculate_corners((position[0] - min_i + 1, position[1] - min_k + 1), region_map)

    return n * len(plant_positions)

def calculate_corners(pos, map):
    i = pos[0]
    k = pos[1]
    corners = 0
    # inner corners
    if map[i+1][k] != "." and map[i+1][k+1] == "." and map[i][k+1] != ".":
        corners += 1
    if map[i-1][k] != "." and map[i-1][k+1] == "." and map[i][k+1] != ".":
        corners += 1
    if map[i-1][k] != "." and map[i-1][k-1] == "." and map[i][k-1] != ".":
        corners += 1
    if map[i+1][k] != "." and map[i+1][k-1] == "." and map[i][k-1] != ".":
        corners += 1
    # outer corners
    if map[i+1][k] == "." and map[i][k+1] == ".":
        corners += 1
    if map[i-1][k] == "." and map[i][k+1] == ".":
        corners += 1
    if map[i-1][k] == "." and map[i][k-1] == ".":
        corners += 1
    if map[i+1][k] == "." and map[i][k-1] == ".":
        corners += 1

    return corners


def main():
    print(task1())

if __name__ == "__main__":
    main()