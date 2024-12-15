import random

def task1():
    file = open("Input/day5.txt", "r")
    rules_raw = []
    prints_raw = []
    prints_started = False
    total = 0
    for line in file:
        line = line.replace("\n", "")
        if line == "":
            prints_started = True
        elif prints_started:
            prints_raw.append(line)
        else:
            rules_raw.append(line)

    rules = []
    for str in rules_raw:
        rules.append(str.split("|"))
    for print_statement in prints_raw:
        print_is_ok = True
        print_split = print_statement.split(",")
        for i in range(len(print_split) - 1):
            for j in range(i, len(print_split)):
                pair = (print_split[i], print_split[j])
                if pair_breaks_rule(pair, rules):
                    print_is_ok = False
                    break

        if print_is_ok:
            total += int(print_split[len(print_split) // 2])

    return total



def pair_breaks_rule(pair, rules):
    for rule in rules:
        if pair[0] == rule[1] and pair[1] == rule[0]:
            return True

    return False

def line_breaks_rule(line, rules):
    for i in range(len(line) - 1):
        for j in range(i, len(line)):
            pair = (line[i], line[j])
            if pair_breaks_rule(pair, rules):
                return True

def fix_line(line, rules):
    i = 0

    while i < len(line) - 1:
        j = i + 1
        while j < len(line):
            pair = (line[i], line[j])
            if pair_breaks_rule(pair, rules):
                mem = line[i]
                line[i] = line[j]
                line[j] = mem
                i = 0
            j += 1

        i += 1
    return line
def task2():
    file = open("Input/day5.txt", "r")
    rules_raw = []
    prints_raw = []
    prints_started = False
    total = 0
    for line in file:
        line = line.replace("\n", "")
        if line == "":
            prints_started = True
        elif prints_started:
            prints_raw.append(line)
        else:
            rules_raw.append(line)

    rules = []
    for str in rules_raw:
        rules.append(str.split("|"))

    for str in rules_raw:
        rules.append(str.split("|"))
    for print_statement in prints_raw:
        print_split = print_statement.split(",")
        if line_breaks_rule(print_split, rules):
            print_split = fix_line(print_split, rules)
            total += int(print_split[len(print_split) // 2])


    return total


def main():
    print(task2())

if __name__ == "__main__":
    main()