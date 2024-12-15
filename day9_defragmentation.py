def task1():
    file = open("Input/day9.txt", "r")
    disk_map = []
    current_block_id = 0
    for line in file:
        block_flag = True
        for char in line:
            if char == "\n":
                continue
            if block_flag:
                for i in range(int(char)):
                    disk_map.append(current_block_id)
                current_block_id += 1
            else:
                for i in range(int(char)):
                    disk_map.append('F')

            block_flag = not block_flag
    left_index = 0
    right_index = len(disk_map) - 1
    while left_index <= right_index:
        if disk_map[left_index] != "F":
            left_index += 1
            continue
        if disk_map[right_index] == "F":
            right_index -= 1
            continue

        disk_map[left_index] = disk_map[right_index]
        disk_map[right_index] = "F"

    total = 0
    for i in range(left_index):
        total += i * int(disk_map[i])

    return total

def task2():
    file = open("Input/day9.txt", "r")
    disk_map = []
    block_list = []
    current_block_id = 0
    for line in file:
        line = line.replace("\n", "")
        block_flag = True
        for char in line:
            start_index = len(disk_map)
            free_length = 0
            if block_flag:
                for i in range(int(char)):
                    disk_map.append(current_block_id)
                    free_length += 1
                block_list.append([start_index, free_length, current_block_id])
                current_block_id += 1
            else:

                for i in range(int(char)):
                    disk_map.append('F')
                    free_length += 1

                block_list.append([start_index, free_length, "F"])


            block_flag = not block_flag

    for block_index in range(len(block_list) - 1, -1, -1):
        if block_list[block_index][2] != "F":
            for free_index in range(len(block_list)):
                if block_list[free_index][2] == "F" and block_list[free_index][1] >= block_list[block_index][1] and block_list[free_index][0] < block_list[block_index][0]:
                    free_length = block_list[free_index][1]
                    free_start = block_list[free_index][0]
                    block_length = block_list[block_index][1]
                    block_list[block_index][0] = free_start

                    block_list[free_index] = [free_start + block_length, free_length - block_length, "F"]

    total = 0
    for block in block_list:
        if block[2] != "F":
            for i in range(block[1]):
                total += (block[0] + i) * int(block[2])

    return total




def main():
    print(task2())

if __name__ == "__main__":
    main()