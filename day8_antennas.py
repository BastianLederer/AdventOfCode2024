import numpy as np
def task1():
    file = open("Input/day8.txt", "r")
    radio_map = []
    for line in file:
        radio_map.append(list(line.replace("\n", "")))

    antennas_by_frequency = {}
    for i in range(len(radio_map)):
        for j in range(len(radio_map[0])):
            if radio_map[i][j] != ".":
                if radio_map[i][j] not in antennas_by_frequency:
                    antennas_by_frequency[radio_map[i][j]] = [np.array([i, j])]
                else:
                    antennas_by_frequency[radio_map[i][j]].append(np.array([i, j]))

    total = 0

    for frequency, antennas in antennas_by_frequency.items():
        for i in range(len(antennas) - 1):
            antenna_1 = antennas[i]
            for k in range(i+1, len(antennas)):
                antenna_2 = antennas[k]
                vec = antenna_2 - antenna_1
                overlay_1 = antenna_1 - vec
                overlay_2 = antenna_2 + vec

                if (0 <= overlay_1[0] < len(radio_map) and
                        0 <= overlay_1[1] < len(radio_map[0]) and
                        radio_map[overlay_1[0]][overlay_1[1]] != "#"):
                    radio_map[overlay_1[0]][overlay_1[1]] = "#"
                    total += 1
                if (0 <= overlay_2[0] < len(radio_map) and
                        0 <= overlay_2[1] < len(radio_map[0]) and radio_map[overlay_2[0]][overlay_2[1]] != "#"):
                    radio_map[overlay_2[0]][overlay_2[1]] = "#"
                    total += 1


    return total


def task2():
    file = open("Input/day8.txt", "r")
    radio_map = []
    for line in file:
        radio_map.append(list(line.replace("\n", "")))

    antennas_by_frequency = {}
    for i in range(len(radio_map)):
        for j in range(len(radio_map[0])):
            if radio_map[i][j] != ".":
                if radio_map[i][j] not in antennas_by_frequency:
                    antennas_by_frequency[radio_map[i][j]] = [np.array([i, j])]
                else:
                    antennas_by_frequency[radio_map[i][j]].append(np.array([i, j]))

    total = 0

    for frequency, antennas in antennas_by_frequency.items():
        for i in range(len(antennas) - 1):
            antenna_1 = antennas[i]
            for k in range(i+1, len(antennas)):
                antenna_2 = antennas[k]
                vec = antenna_2 - antenna_1
                v = 0
                overlay_1 = antenna_1 - vec * v
                overlay_2 = antenna_2 + vec * v
                while ((0 <= overlay_1[0] < len(radio_map) and
                        0 <= overlay_1[1] < len(radio_map[0])) or (0 <= overlay_2[0] < len(radio_map) and
                        0 <= overlay_2[1] < len(radio_map[0]))):


                    if (0 <= overlay_1[0] < len(radio_map) and
                            0 <= overlay_1[1] < len(radio_map[0]) and
                            radio_map[overlay_1[0]][overlay_1[1]] != "#"):
                        radio_map[overlay_1[0]][overlay_1[1]] = "#"
                        total += 1
                    if (0 <= overlay_2[0] < len(radio_map) and
                            0 <= overlay_2[1] < len(radio_map[0]) and radio_map[overlay_2[0]][overlay_2[1]] != "#"):
                        radio_map[overlay_2[0]][overlay_2[1]] = "#"
                        total += 1

                    v += 1
                    overlay_1 = antenna_1 - vec * v
                    overlay_2 = antenna_2 + vec * v

    return total

def main():
    print(task2())

if __name__ == "__main__":
    main()




