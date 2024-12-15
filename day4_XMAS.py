import numpy as np
def task1():
    file = open("Input/day4.txt", "r")
    puzzle = []
    total = 0
    for line in file:
        puzzle.append(list(line.replace("\n", "")))

    puzzle = np.array(puzzle)
    kernel_size = 4
    for i in range(len(puzzle[0,:]) - 3):
        for j in range(len(puzzle) - 3):
            current_slice = []
            for k in range(kernel_size):
                current_slice.append(puzzle[j+k][i:i+kernel_size])

            total += find_xmas_diagonal(np.array(current_slice))

    for i in range(0, len(puzzle[0,:])):
        for j in range(len(puzzle) - 3):
            slice = puzzle[i,j:j+4]
            if "".join(slice) == "XMAS" or "".join(slice) == "SAMX":
                total += 1

    for i in range(0, len(puzzle[0,:]) - 3):
        for j in range(len(puzzle)):
            slice = puzzle[i : i + 4,j]
            if "".join(slice) == "XMAS" or "".join(slice) == "SAMX":
                total += 1



    return total






def find_xmas_diagonal(sliced_input):
    count = 0

    diagonals = get_dioagonals(sliced_input)
    for diag in diagonals:
        if "".join(diag) == "XMAS" or "".join(diag) == "SAMX":
            count += 1
    return count
def get_dioagonals(sliced_input):
    diag1 = [sliced_input[0][0], sliced_input[1][1], sliced_input[2][2], sliced_input[3][3]]
    diag2 = [sliced_input[0][3], sliced_input[1][2], sliced_input[2][1], sliced_input[3][0]]
    return [diag1, diag2]


def task2():
    file = open("Input/day4.txt", "r")
    puzzle = []
    total = 0

    for line in file:
        puzzle.append(list(line.replace("\n", "")))

    puzzle = np.array(puzzle)
    kernel_size = 3

    for i in range(len(puzzle[0,:]) - 2):
        for j in range(len(puzzle) - 2):
            current_slice = []
            for k in range(kernel_size):
                current_slice.append(puzzle[j+k][i:i+kernel_size])

            total += find_crosses(np.array(current_slice))

    return total
def find_crosses(slice):
    count = 0

    diagonals = get_dioagonals_short(slice)
    dia1 = "".join(diagonals[0])
    dia2 = "".join(diagonals[1])
    if (dia1 == "SAM" or dia1 == "MAS") and (dia2 == "SAM" or dia2=="MAS"):
        count += 1
    return count

def get_dioagonals_short(sliced_input):
    diag1 = [sliced_input[0][0], sliced_input[1][1], sliced_input[2][2]]
    diag2 = [sliced_input[0][2], sliced_input[1][1], sliced_input[2][0]]
    return [diag1, diag2]

if __name__ == "__main__":
    print(task2())