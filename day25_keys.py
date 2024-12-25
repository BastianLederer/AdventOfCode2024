def task1():
    file = open("Input/day25.txt", "r")
    keys = []
    locks = []
    current_object = []
    for line in file:
        line = line.replace("\n", "")
        if line == "":
            if current_object[0][0] == ".":
                keys.append(parse_object(current_object, True))
                current_object = []
            else:
                locks.append(parse_object(current_object, False))
                current_object = []
        else:
            current_object.append(list(line))

    pairs = 0
    for key in keys:
        for lock in locks:
            if key_fits_in_lock(key, lock):
                pairs += 1

    return pairs


def parse_object(object, is_key):
    object_heights = []
    if is_key:
        for i in range(len(object[0])):
            for k in range(len(object)):
                if object[k][i] == "#":
                    object_heights.append(6 - k)
                    break
    else:
        for i in range(len(object[0])):
            for k in range(len(object)):
                if object[k][i] == ".":
                    object_heights.append(k - 1)
                    break

    return object_heights
def key_fits_in_lock(key, lock):
    for i in range(len(key)):
        if key[i] + lock[i] > 5:
            return False
    return True

def main():
    print(task1())

if __name__ == "__main__":
    main()