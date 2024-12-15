import re
import gmpy2

def task1():
    file = open("Input/day13.txt", "r")
    input_list = []
    for line in file:
        input_list.append(line)

    i = 0
    machine_list = []
    while i < len(input_list) - 3:
        a_split = re.sub(r'[^\d,]', '', input_list[i]).split(",")
        a = (int(a_split[0]), int(a_split[1]))
        b_split = re.sub(r'[^\d,]', '', input_list[i + 1]).split(",")
        b = (int(b_split[0]), int(b_split[1]))
        p_split = re.sub(r'[^\d,]', '', input_list[i + 2]).split(",")
        p = (int(p_split[0]), int(p_split[1]))
        machine_list.append([a, b, p])
        i += 4

    total = 0

    for machine in machine_list:
        res = solve_machine(machine)
        if res is not None:
            total += res

    return total

# def solve_machine_p1(machine):
#     a = np.array([machine[0][0], machine[0][1]])
#     b = np.array([machine[1][0], machine[1][1]])
#     t = np.array([machine[2][0], machine[2][1]])
#     cost = 0
#     while (t[0] % b[0] != 0 or t[1] % b [1] != 0 or not(t[0] // b[0] == t[1] // b[1])):
#         if t[0] < 0 and t[1] < 0:
#             return None
#         t[0] -= a[0]
#         t[1] -= a[1]
#         cost += 3
#     cost += t[0] // b[0]
#     return cost

import gmpy2


def solve_machine(machine):
    prize = machine[2]
    a = machine[0]
    b = machine[1]

    # Convert inputs to gmpy2.mpz for handling large numbers
    a_x = a[0]
    a_y = a[1]
    b_x = b[0]
    b_y = b[1]
    prize_x = prize[0] + 10000000000000
    prize_y = prize[1] + 10000000000000

    a_num = prize_x * b_y - prize_y * b_x
    b_num = prize_x * a_y - prize_y * a_x



    d = a_x * b_y - b_x * a_y
    if d == 0 or a_num % d != 0 or b_num % d != 0:
        return 0
    a, b = a_num // d, -b_num // d

    return 3 * a + b




def main():
    print(task1())

if __name__ == "__main__":
    main()