import time


def task1():
    file = open("Input/day22.txt", "r")
    numbers = []
    for line in file:
        numbers.append(int(line.replace("\n", "")))

    total = 0
    for num in numbers:
        for i in range(2000):
            num = simulate_step(num)
        total += num

    return total

sequences = {}


def task2():
    file = open("Input/day22.txt", "r")
    numbers = []
    for line in file:
        numbers.append(int(line.strip()))  # Use strip() to avoid trailing spaces/newlines

    total = 0
    for num in numbers:
        current_sequence = []
        seen_sequences = set()
        prev = num % 10
        for i in range(2000):
            num = simulate_step(num)
            last = num % 10

            diff = last - prev
            current_sequence.append(diff)

            # Only when the sequence has 4 elements, process it
            if len(current_sequence) == 4:
                seq_tuple = tuple(current_sequence)
                if seq_tuple not in seen_sequences:
                    seen_sequences.add(seq_tuple)
                    if seq_tuple in sequences:
                        sequences[seq_tuple] += last
                    else:
                        sequences[seq_tuple] = last

                # Now slide the window by removing the first element
                current_sequence.pop(0)

            prev = last

    # Find the sequence with the maximum value
    max_key = None
    max_value = None
    for key, value in sequences.items():
        if max_value is None or value > max_value:
            max_key = key
            max_value = value

    print(max_key)
    print(max_value)


def simulate_step(secret):
    intermediate = secret * 64
    secret = (secret ^ intermediate) % 16777216

    intermediate = secret // 32
    secret = (secret ^ intermediate) % 16777216

    intermediate = secret * 2048
    secret = (secret ^ intermediate) % 16777216

    return secret

def main():
    start = time.perf_counter()
    print(task2())
    print(time.perf_counter() - start)
if __name__ == "__main__":
    main()