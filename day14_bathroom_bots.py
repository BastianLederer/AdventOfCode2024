import numpy as np
def task1(width = 101, height = 103):
    file = open("Input/day14.txt", "r")
    robots = []
    for line in file:
        temp1 = line.replace("\n", "").split(" ")
        pos_split = temp1[0].split("=")[1].split(",")
        vel_split = temp1[1].split("=")[1].split(",")
        robots.append([(int(pos_split[0]), int(pos_split[1])), (int(vel_split[0]), int(vel_split[1]))])

    safety_scores = [0, 0, 0, 0]

    for i in range(len(robots)):
        for k in range(100):
            robots[i] = simulate_step(robots[i], width, height)

        if robots[i][0][0] < width // 2:
            if robots[i][0][1] < height // 2:
                safety_scores[0] += 1
            elif robots[i][0][1] > height / 2:
                safety_scores[1] += 1
        elif robots[i][0][0] > width / 2:
            if robots[i][0][1] < height // 2:
                safety_scores[3] += 1
            elif robots[i][0][1] > height / 2:
                safety_scores[2] += 1

    return safety_scores[0] * safety_scores[1] * safety_scores[2] * safety_scores[3]

def task2(width = 101, height = 103):
    file = open("Input/day14.txt", "r")
    robots = []
    for line in file:
        temp1 = line.replace("\n", "").split(" ")
        pos_split = temp1[0].split("=")[1].split(",")
        vel_split = temp1[1].split("=")[1].split(",")
        robots.append([(int(pos_split[0]), int(pos_split[1])), (int(vel_split[0]), int(vel_split[1]))])

    safety_scores = [0, 0, 0, 0]
    secs = 0
    maps = []

    for a in range(10000):
        secs += 1
        total_dist = 0
        for i in range(len(robots)):
            robots[i] = simulate_step(robots[i], width, height)

            if robots[i][0][0] < width // 2:
                if robots[i][0][1] < height // 2:
                    safety_scores[0] += 1
                elif robots[i][0][1] > height / 2:
                    safety_scores[1] += 1
            elif robots[i][0][0] > width / 2:
                if robots[i][0][1] < height // 2:
                    safety_scores[3] += 1
                elif robots[i][0][1] > height / 2:
                    safety_scores[2] += 1

        current_map = save_map(robots)
        total_neighbors = 0
        for i in range(len(robots)):
            r = robots[i][0]
            if r[1] + 1 < current_map.shape[1] and current_map[r[0], r[1] + 1] != " ":
                total_neighbors += 1
            if r[1] - 1 >= 0 and current_map[r[0], r[1] - 1] != " ":
                total_neighbors += 1
            if r[0] + 1 < current_map.shape[0] and current_map[r[0] + 1, r[1]] != " ":
                total_neighbors += 1
            if r[0] - 1 >= 0 and current_map[r[0] - 1, r[1]] !=  " ":
                total_neighbors += 1

            if r[1] + 2 < current_map.shape[1] and current_map[r[0], r[1] + 2] != " ":
                total_neighbors += 2
            if r[1] - 2 >= 0 and current_map[r[0], r[1] - 2] != " ":
                total_neighbors += 2
            if r[0] + 2 < current_map.shape[0] and current_map[r[0] + 2, r[1]] != " ":
                total_neighbors += 2
            if r[0] - 2 >= 0 and current_map[r[0] - 2, r[1]] !=  " ":
                total_neighbors += 2

        maps.append([current_map, total_neighbors, secs])


    lowest = None
    suspect = None
    index = None
    for map_l in maps:
        if lowest is None or map_l[1] > lowest:
            lowest = map_l[1]
            suspect = map_l[0]
            index = map_l[2]

    print(lowest)

    for map_l in maps:
        if map_l[2] == index:
            print(map_l[0])

            print(map_l[2])

    return safety_scores[0] * safety_scores[1] * safety_scores[2] * safety_scores[3]

def save_map(robots):
    map = np.full((101, 103), " ")
    for robot in robots:
        map[robot[0][0], robot[0][1]] = "#"
    return map
def simulate_step(robot, witdh, height):
    pos = robot[0]
    vel = robot[1]
    pos = ((pos[0] + vel[0]) % witdh, (pos[1] + vel[1]) % height)
    return [pos, vel]

def main():
    np.set_printoptions(threshold=np.inf)
    np.set_printoptions(threshold=np.inf, linewidth=np.inf)
    print(task2(width=101, height=103))

if __name__ == "__main__":
    main()