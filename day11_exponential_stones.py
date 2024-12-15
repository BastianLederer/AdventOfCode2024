import time
from collections import Counter

def task1(blinks):
    file = open("Input/day11.txt", "r")
    stones = []
    stone_table = {}
    for line in file:
        for stone in line.replace("\n","").split(" "):
            stones.append(int(stone))

    for i in range(blinks):
        start_time = time.perf_counter()
        blink(stones, stone_table)

    d = Counter(stones)
    new_list = list([item for item in d if d[item] > 1])
    print(new_list)
    print(len(new_list) / len(stones))
    return len(stones)

def blink(stones, stone_table):
    i = 0
    while i < len(stones):
        stone = stones[i]
        stone_str = str(stone)
        if stone == 0:
            stones[i] = 1
        elif len(stone_str) % 2 == 0:
            if not stones[i] in stone_table:
                stone_table[stones[i]] = [int(stone_str[:len(stone_str) // 2]), int(stone_str[len(stone_str) // 2:])]
            stones[i] = stone_table[stone][0]
            stones.insert(i + 1, stone_table[stone][1])
            i += 1
        else:
            if stones[i] in stone_table:
                stones[i] = stone_table[stones[i]]
            else:
                stone_table[stones[i]] = stone * 2024
                stones[i] = stone * 2024

        i += 1



    return stones

def task2(blinks=75):
    file = open("Input/day11.txt", "r")
    stones = {}
    for line in file:
        for stone in line.replace("\n","").split(" "):
            stones[int(stone)] = 1

    for i in range(blinks):
        stones = blink_2(stones)


    total = 0
    for stone, amount in stones.items():
        total += amount

    return total

def blink_2(stones):
    new_stones = {}
    for stone, amount in stones.items():
        if stone == 0:
            if 1 in new_stones:
                new_stones[1] += amount
            else:
                new_stones[1] = amount
        elif len(str(stone)) % 2 == 0:

            s1 = int(str(stone)[:len(str(stone)) // 2])
            s2 = int(str(stone)[len(str(stone)) // 2:])
            if s1 in new_stones:
                new_stones[s1] += amount
            else:
                new_stones[s1] = amount
            if s2 in new_stones:
                new_stones[s2] += amount
            else:
                new_stones[s2] = amount
        else:
            if stone * 2024 in new_stones:
                new_stones[stone * 2024] += amount
            else:
                new_stones[stone * 2024] = amount


    return new_stones

def main():
    start_time = time.perf_counter()
    print(task2(10000))
    print(time.perf_counter() - start_time)

if __name__ == "__main__":
    main()


