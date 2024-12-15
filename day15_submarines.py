import numpy as np
import sys

def task1():
    file = open("Input/day15.txt", "r")
    ware_map = []
    comms = []
    comms_started = False
    command_map = {
        "<": np.array([0, -1]),
        "^": np.array([-1, 0]),
        ">": np.array([0, 1]),
        "v": np.array([1, 0])
    }
    for line in file:
        line = line.replace("\n", "")
        if not comms_started and line != "":
            ware_map.append(list(line))
        elif line == "":
            comms_started = True
        else:
            for char in line:
                comms.append(char)
    robot_position = None
    for i in range(len(ware_map)):
        for k in range(len(ware_map)):
            if ware_map[i][k] == "@":
                robot_position = np.array([i, k])

    for command in comms:
        new_pos = move_object(robot_position, command_map[command], ware_map)
        if new_pos is not None:
            robot_position = new_pos

    total = 0

    for i in range(len(ware_map)):
        for k in range(len(ware_map)):
            if ware_map[i][k] == "O":
                total += 100 * i + k

    for line in ware_map:
        print(line)
    return total



def move_object(position, movement, map):
    target_position = position + movement
    if map[target_position[0]][target_position[1]] == ".":
        map[target_position[0]][target_position[1]] = map[position[0]][position[1]]
        map[position[0]][position[1]] = "."
        return target_position
    elif map[target_position[0]][target_position[1]] == "#":
        return None
    else:
        if move_object(target_position, movement, map) is not None:
            map[target_position[0]][target_position[1]] = map[position[0]][position[1]]
            map[position[0]][position[1]] = "."
            return target_position
        else:
            return None

def task2():
    file = open("Input/day15.txt", "r")
    ware_map = []
    comms = []
    comms_started = False
    command_map = {
        "<": np.array([0, -1]),
        "^": np.array([-1, 0]),
        ">": np.array([0, 1]),
        "v": np.array([1, 0])
    }

    boxes = {}
    current_box_id = 0
    for line in file:
        line = line.replace("\n", "").replace("#", "##").replace(".", "..").replace("@", "@.").replace("O", "[]")
        if not comms_started and line != "":
            ware_map.append(list(line))
        elif line == "":
            comms_started = True
        else:
            for char in line:
                comms.append(char)
    robot_position = None
    for i in range(len(ware_map)):
        for k in range(len(ware_map[0])):
            if ware_map[i][k] == "@":
                robot_position = np.array([i, k]).reshape(1, -1)
            elif ware_map[i][k] == "[":
                boxes[current_box_id] = np.array([[i,k], [i, k+1]])
                ware_map[i][k] = current_box_id
                ware_map[i][k+1] = current_box_id
                current_box_id += 1

    for command in comms:

        if move_is_possible(robot_position, command_map[command], boxes, ware_map):
            robot_position = execute_move(robot_position, command_map[command],boxes, ware_map)

    total = 0

    for key, box in boxes.items():
        if key != "@":
            total += box[0][0] * 100 + box[0][1]

    for line in ware_map:
        print("".join(str(x) for x in line))
    return total

def move_is_possible(position, movement, boxes, ware_map):

    key = ware_map[position[0][0]][position[0][1]]

    target_position = []
    for row in position:
        target_position.append(row + movement)
    for pos in target_position:
        if ware_map[pos[0]][pos[1]] == "#":
            return False
    affected_boxes = []
    for pos in target_position:
        if ware_map[pos[0]][pos[1]] != "." and ware_map[pos[0]][pos[1]] != key:
            affected_boxes.append(boxes[ware_map[pos[0]][pos[1]]])
    if len(affected_boxes) == 0:
        return True

    move_possible = True
    for pos in affected_boxes:
        if not move_is_possible(pos, movement, boxes, ware_map):
            move_possible = False
    return move_possible

def execute_move(position, movement, boxes, ware_map):
    # target_position = position + movement
    key = ware_map[position[0][0]][position[0][1]]
    target_position = []
    for row in position:
        target_position.append(row + movement)
    affected_boxes = []
    for pos in target_position:
        if (ware_map[pos[0]][pos[1]] != "." and ware_map[pos[0]][pos[1]] != key and
                ware_map[pos[0]][pos[1]] not in affected_boxes):
            affected_boxes.append(ware_map[pos[0]][pos[1]])
            execute_move(boxes[ware_map[pos[0]][pos[1]]], movement, boxes, ware_map)

    ware_map[position[0][0]][position[0][1]] = "."
    if len(position) > 1:
        ware_map[position[1][0]][position[1][1]] = "."

    for pos in target_position:
        ware_map[pos[0]][pos[1]] = key
        boxes[ware_map[pos[0]][pos[1]]] = np.array(target_position)

    return target_position



def main():
    print(task2())

if __name__ == "__main__":
    main()
