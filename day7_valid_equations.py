from itertools import product
def task1():
    file = open("Input/day7.txt", "r")
    total = 0
    for line in file:
        split1 = line.split(":")
        result = int(split1[0])
        operands_strings = split1[1].split(" ")
        operands = []
        for op in operands_strings:
            if op != "":
                operands.append(int(op.replace("\n", "")))
        if equation_has_solution_concat(result, operands):
            total += result

    return total



def equation_has_solution(result, operands):
    for i in range(int(2**(len(operands) - 1))):
        operators = []
        for k in range(len(operands) - 1):
            operators.append("+")
        i_copy = i
        index = 0
        while index in range(len(operators)):
            if i_copy % 2 == 0:
                operators[index]="*"

            i_copy = i_copy // 2
            index += 1

        indermediate = operands[0]
        for j in range(len(operators)):
            if operators[j] == "+":
                indermediate += operands[j + 1]
            else:
                indermediate *= operands[j + 1]

        if indermediate == result:
            return True

    return False

def equation_has_solution_concat(result, operands):
    prod = product("+*|", repeat = len(operands)-1)
    for perm in prod:
        operators = "".join(perm)
        indermediate = operands[0]
        offset = 1
        for i in range(len(operators)):
            if operators[i] == "+":
                indermediate += operands[i + offset]
            elif operators[i] == "*":
                indermediate *= operands[i + offset]
            elif operators[i] == "|":
                indermediate = int(str(indermediate) + str(operands[i+offset]))

        if indermediate == result:
            return True

    return False





def main():
    print(task1())

if __name__ == "__main__":
    main()
