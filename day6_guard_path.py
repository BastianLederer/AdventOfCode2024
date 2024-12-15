import numpy as np
import time
import copy
def task1():
    file = open("Input/day6.txt", "r")
    map = []
    for line in file:
        map.append(list(line.replace("\n", "")))

    guard_pos = None
    guard_movement = None
    for i in range(len(map)):
        for k in range(len(map[1])):
            if map[i][k] == "<":
                guard_pos = np.array([i, k])
                guard_movement = np.array([0, -1])
            elif map[i][k] == ">":
                guard_pos = np.array([i, k])
                guard_movement = np.array([0, 1])
            elif map[i][k] == "v":
                guard_pos = np.array([i, k])
                guard_movement = np.array([1, 0])
            elif map[i][k] == "^":
                guard_pos = np.array([i, k])
                guard_movement = np.array([-1, 0])

    active_obstacles = []

    while guard_pos[0] < len(map) and guard_pos[1] < len(map[1]):
        map[guard_pos[0]][guard_pos[1]] = "X"
        next_guard_pos = np.add(guard_pos, guard_movement)
        while next_guard_pos[0] < len(map) and next_guard_pos[1] < len(map[1]) and map[next_guard_pos[0]][next_guard_pos[1]] == "#":
            active_obstacles.append((np.array([next_guard_pos[0],next_guard_pos[1]]), guard_movement))
            guard_movement = turn_right(guard_movement)
            next_guard_pos = np.add(guard_pos, guard_movement)

        map[guard_pos[0]][guard_pos[1]] = "X"
        guard_pos = next_guard_pos

    # x_count = 0
    # for i in range(len(map)):
    #     for k in range(len(map[1])):
    #         if map[i][k] == "X":
    #             x_count += 1
    #
    #
    # return x_count

    loop_count = 0

    for obstacle_tuple in active_obstacles:
        if is_obstacel_art_of_loop(obstacle_tuple, map):
            loop_count += 1



    return loop_count


def is_obstacel_art_of_loop(obstacle_tuple, map):

    obstacle = obstacle_tuple[0]
    direction = obstacle_tuple[1]
    guard_loc = np.subtract(obstacle, direction)
    turn_points = [guard_loc]

    original_guard_pos = guard_loc

    direction = turn_right(direction)
    while map[guard_loc[0]][guard_loc[1]] != "#":
        guard_loc = np.add(guard_loc, direction)
        if guard_loc[0] >= len(map) or guard_loc[1] >= len(map[0]):
            return False

    guard_loc = np.subtract(guard_loc, direction)
    turn_points.append(guard_loc)
    direction = turn_right(direction)


    while map[guard_loc[0]][guard_loc[1]] != "#":
        guard_loc = np.add(guard_loc, direction)
        if guard_loc[0] >= len(map) or guard_loc[1] >= len(map[0]):
            return False

    guard_loc = np.subtract(guard_loc, direction)
    turn_points.append(guard_loc)
    direction = turn_right(direction)

    # maybe this doesnt work

    while not (guard_loc[0] == original_guard_pos[0] or guard_loc[1] == original_guard_pos[1]):
        guard_loc = np.add(guard_loc, direction)
        if guard_loc[0] >= len(map) or guard_loc[1] >= len(map[0]):
            return False

    direction = turn_right(direction)
    while map[guard_loc[0]][guard_loc[1]] != "#":
        guard_loc = np.add(guard_loc, direction)
        if guard_loc[0] >= len(map) or guard_loc[1] >= len(map[0]):
            return False

    if obstacle[0] == guard_loc[0] and obstacle[1] == guard_loc[1]:
        return True
    else:
        return False



def turn_right(vector):
    if vector[0] == 0 and vector[1] == 1:
        return np.array([1,0])
    if vector[0] == 1 and vector[1] == 0:
        return np.array([0,-1])
    if vector[0] == 0 and vector[1] == -1:
        return np.array([-1,0])
    if vector[0] == -1 and vector[1] == 0:
        return np.array([0,1])

def task2_brute_force():
    file = open("Input/day6.txt", "r")
    o_map = []
    for line in file:
        o_map.append(list(line.replace("\n", "")))

    free_fields = []

    for n in range(len(o_map)):
        for m in range(len(o_map)):
            if o_map[n][m] == ".":
                free_fields.append([n, m])
    loop_count = 0
    debug_count = 0
    for field in free_fields:
        debug_count += 1
        if debug_count % 100 == 0:
            print(f"checking {debug_count} of {len(free_fields)}")

        map = copy.deepcopy(o_map)
        map[field[0]][field[1]] = "#"
        loop_found = False


        guard_pos = None
        guard_movement = None
        for i in range(len(map)):
            for k in range(len(map[1])):
                if map[i][k] == "<":
                    guard_pos = np.array([i, k])
                    guard_movement = np.array([0, -1])
                elif map[i][k] == ">":
                    guard_pos = np.array([i, k])
                    guard_movement = np.array([0, 1])
                elif map[i][k] == "v":
                    guard_pos = np.array([i, k])
                    guard_movement = np.array([1, 0])
                elif map[i][k] == "^":
                    guard_pos = np.array([i, k])
                    guard_movement = np.array([-1, 0])

        start_time = time.perf_counter()

        while 0 <= guard_pos[0] < len(map) and 0 <= guard_pos[1] < len(map[1]) and not loop_found:
            next_guard_pos = np.add(guard_pos, guard_movement)
            while 0 <= next_guard_pos[0] < len(map) and 0 <= next_guard_pos[1] < len(map[1]) and map[next_guard_pos[0]][next_guard_pos[1]] == "#":
                if time.perf_counter() - start_time > 0.05:
                    print("loop")
                    loop_count += 1
                    loop_found = True
                    break
                guard_movement = turn_right(guard_movement)
                next_guard_pos = np.add(guard_pos, guard_movement)

            guard_pos = next_guard_pos

    return loop_count


def main():
    print(task2_brute_force())

    # Calculate elapsed time

if __name__ == "__main__":
    main()