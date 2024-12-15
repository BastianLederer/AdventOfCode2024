def task1():
    file = open("Input/day1.txt", "r")
    numbers_left = []
    number_right = []
    for line in file:
        line_split = line.split("   ")
        numbers_left.append(line_split[0])
        number_right.append(line_split[-1])
    numbers_left = sorted(numbers_left)
    number_right = sorted(number_right)

    distance_sum = 0
    for i in range(len(numbers_left)):
        distance_sum += abs(int(numbers_left[i]) - int(number_right[i]))

    return distance_sum

def task2():
    file = open("Input/day1.txt", "r")
    numbers_left = []
    number_right = []

    count_dict = {}
    total_sum = 0

    for line in file:
        line_split = line.split("   ")
        numbers_left.append(int(line_split[0]))
        number_right.append(int(line_split[-1]))

    for number in numbers_left:
        if number in count_dict:
            total_sum += count_dict[number]
        else:
            number_count = 0
            for num_r in number_right:
                if num_r == number:
                    number_count += 1
            inc = number_count * number
            count_dict[number] = inc
            total_sum += inc

    return total_sum





if __name__ == "__main__":
    print(task2())