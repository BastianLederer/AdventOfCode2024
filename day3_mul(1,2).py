def task1(): # recycled for task 2
    file = open("Input/day3.txt", "r")
    numbers_left = []
    number_right = []
    state = "m"
    total = 0
    do_flag = True

    for line in file:
        state = "m"

        line_split_do = line.split("do()")
        do_marks = []
        current_index = 0
        for sub in line_split_do:
            do_marks.append(current_index + len(sub))
            current_index += len(sub) + 4 # length of do() itself

        line_split_dont = line.split("don't()")
        dont_marks = []
        current_index = 0
        for sub in line_split_dont:
            dont_marks.append(current_index + len(sub))
            current_index +=len(sub) + 7

        line = list(line)
        for i in range(len(line)):
            if i in dont_marks:
                do_flag = False
            elif i in do_marks:
                do_flag = True
            if not do_flag:
                line[i] = " "

        current_number1_string = ""
        current_number2_string = ""
        for char in line:
            if state == "m" and char == "m":
                state = "u"
            elif state == "u" and char == "u":
                state = "l"
            elif state == "l" and char == "l":
                state = "("
            elif state == "(" and char == "(":
                state = "number1"
            elif state == "number1" and char.isdigit():
                current_number1_string += char
            elif state == "number1" and char == ",":
                state = "number2"
            elif state == "number2" and char.isdigit():
                current_number2_string += char
            elif state == "number2" and char == ")":
                if len(current_number1_string) > 0 and len(current_number2_string) > 0:
                    total += int(current_number1_string) * int(current_number2_string)
                    current_number1_string = ""
                    current_number2_string = ""
                    state = "m"
            else:
                current_number1_string = ""
                current_number2_string = ""
                state = "m"

    return total



if __name__ == "__main__":
    print(task1())