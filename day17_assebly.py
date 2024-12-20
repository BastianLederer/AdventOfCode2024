import math
import time
from itertools import product

registers = {
    'A':0,
    'B':0,
    'C':0,
    "IP": 0,
    "out": ""
}

def task1():
    a_oct = []
    file = open("Input/day17.txt")
    lines = []
    for line in file:
        lines.append(line.replace("\n", ""))

    registers["A"] = int(lines[0].split(":")[1])
    # registers["A"] = 0b110101010010010111101110010001101111010001
    # registers["A"] = 457732203388
    registers["B"] = int(lines[1].split(":")[1])
    registers["B"] = int(lines[2].split(":")[1])

    Program_raw = list(lines[4].split(":")[1].replace(" ","").split(","))
    Prog_comp = lines[4].split(":")[1].replace(" ","").replace(",", "")
    Program = []
    for elem in Program_raw:
        Program.append(int(elem))

    opcode_map = {
        0: div_to_a,
        1: xor,
        2: modulo,
        3: jump,
        4: xor_b_c,
        5: out,
        6: div_to_b,
        7: div_to_c
    }

    Prog_original = lines[4].split(":")[1].replace(" ","")

    while registers["IP"] < len(Program):
        opcode_map[Program[registers["IP"]]](Program[registers["IP"] + 1])
        registers["IP"] += 2

    current_a = 0
    for prog_counter in range(len(Program)):
        a_oct.append([])
        for i in range(8):
            for j in range(16):
                for k in range(16):

                    registers["A"] = 8 * current_a + i
                    registers["B"] = j
                    registers["C"] = k
                    registers["IP"] = 0
                    registers["out"] = ""
                    while registers["IP"] < len(Program):
                        opcode_map[Program[registers["IP"]]](Program[registers["IP"] + 1])
                        registers["IP"] += 2
                    if registers["out"] in Prog_comp[(len(Program) - prog_counter - 1):]:
                        if i not in a_oct[prog_counter]:
                            a_oct[prog_counter].append(i)

    # combinations = list(product(*a_oct))
    # print("trying permutations")
    # count = 0
    # for combo in combinations:
    #     if count % 100000 == 0:
    #         print(count)
    #     count+=1
    #
    #     a_attempt = "".join(map(str, combo))
    #     registers["A"] = int(a_attempt, 8)
    #     registers["B"] = 0
    #     registers["C"] = 0
    #     registers["IP"] = 0
    #     registers["out"] = ""
    #     while registers["IP"] < len(Program):
    #         opcode_map[Program[registers["IP"]]](Program[registers["IP"] + 1])
    #         registers["IP"] += 2
    #     if registers["out"] in Prog_comp:
    #         print(combo)

    print(a_oct)
    a = 0
    # for i in range(len(a_oct)):
    #     a += a_oct[i] * math.pow(8, len(a_oct) - i -1)
    return registers["out"]

def get_combo_operand_value(operand):
    if operand < 4 and operand > -1:
        return operand
    elif operand == 4:
        return registers["A"]
    elif operand == 5:
        return registers["B"]
    elif operand == 6:
        return registers["C"]
    else:
        print("invalid operand in get_operand_value")
        return None
def div_to_a(operand):
    operand = get_combo_operand_value(operand)
    registers["A"] = int(registers["A"] // int(math.pow(2, operand)))

def xor(operand):
    registers["B"] = registers["B"] ^ operand

def modulo(operand):
    operand = get_combo_operand_value(operand)
    registers["B"] = operand % 8

def jump(operand):
    if registers["A"] != 0:
        registers["IP"] = operand - 2 # bc lazy

def xor_b_c(operand):
    registers["B"] = registers["B"] ^ registers["C"]

def out(operand):
    operand = get_combo_operand_value(operand) % 8
    if registers["out"] == "":
        registers["out"] += str(operand)
    else:
        registers["out"] += str(operand)

def div_to_b(operand):
    operand = get_combo_operand_value(operand)
    registers["B"] = int(registers["A"] // int(math.pow(2, operand)))

def div_to_c(operand):
    operand = get_combo_operand_value(operand)
    registers["C"] = int(registers["A"] // int(math.pow(2, operand)))

def part_2():
    with open("Input/day17.txt", "r") as f:
        ps = f.read().split("\n\n")

    prog = list(map(int, ps[1].split(":")[1].split(",")))
    to_visit = [(len(prog), 0)]
    while to_visit:
        pos, a = to_visit.pop(0)
        for i in range(8):
            n_a = a * 8 + i
            o = list(map(int, exec(prog, [n_a, 0, 0])))
            if o == prog[pos - 1:]:
                to_visit.append((pos - 1, n_a))
                if len(o) == len(prog):
                    print(n_a)

def exec(prog, reg):
    pc = 0
    output = []

    while True:
        if pc > len(prog) - 1:
            return output

        op = prog[pc]
        opreand = prog[pc+1]
        assert 0 <= opreand < 7
        combo = opreand if opreand < 4 else reg[opreand-4]

        if op == 0:  # adv
            reg[0] = reg[0] // 2 ** combo
        elif op == 1:  # bxl
            reg[1] ^= opreand
        elif op == 2:  # bst
            reg[1] = combo % 8
        elif op == 3:  # jnz
            if reg[0] != 0:
                pc = opreand
                continue
        elif op == 4:  # bxl
            reg[1] ^= reg[2]
        elif op == 5:
            output.append(str(combo % 8))
        elif op == 6:  # bdv
            reg[1] = reg[0] // 2 ** combo
        elif op == 7:  # cdv
            reg[2] = reg[0] // 2 ** combo

        pc += 2

def main():
    print(task1())
    print(oct(236539226447469))

if __name__ == "__main__":
    main()

