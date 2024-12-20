possible_designs = []
memo = {}


def task1():
    with open("Input/day19.txt", "r") as file:
        lines = [line.strip() for line in file]

    patterns = lines[0].replace(" ", "").split(",")
    for pattern in patterns:
        possible_designs.append(pattern)

    designs = lines[2:]
    possible = 0

    for design in designs:
        if design_is_possible(0, design, patterns):
            possible += 1

    return possible

def task2():
    with open("Input/day19.txt", "r") as file:
        lines = [line.strip() for line in file]

    patterns = lines[0].replace(" ", "").split(",")
    for pattern in patterns:
        possible_designs.append(pattern)

    pattern_dict = {}
    for pattern in patterns:
        pattern_dict[pattern] = 1

    designs = lines[2:]
    count = 0

    for design in designs:
        count += count_possible_designs(0, design, patterns)

    return count


def design_is_possible(cut, design, patterns):

    if design in possible_designs:
        return True
    if not design:
        return True
    if cut >= len(design):
        return False
    if design in memo:
        return memo[design]

    if design[:cut] in patterns:
        if design_is_possible(0, design[cut:], patterns):
            possible_designs.append(design)
            memo[design] = True
            return True

    memo[design] = design_is_possible(cut + 1, design,patterns)
    return memo[design]

def count_possible_designs(cut, design, patterns):
    if not design:
        return 1
    if cut >= len(design):
        return 0
    if design in memo:
        return memo[design]

    count = 0
    while cut < len(design)+1:
        if design[:cut] in patterns:
            t = count_possible_designs(0, design[cut:], patterns)
            count += t

        cut += 1
    memo[design] = count
    return count

def main():
    print(task2())


if __name__ == "__main__":
    main()
