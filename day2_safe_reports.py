def task1():
    file = open("Input/day2.txt", "r")
    safe_count = 0

    for line in file:
        line_split = line.split(" ")
        report = []
        for s in line_split:
            report.append(int(s))

        if report_is_safe(report):
            safe_count += 1

    return safe_count


def report_is_safe(report):
    previous_diff = None
    for i in range(len(report) - 1):
        diff = report[i] - report[i + 1]
        if previous_diff is not None:
            if diff * previous_diff < 0:
                return False

        if abs(diff) < 1 or abs(diff) > 3:
            return False

        previous_diff = diff

    return True

def task2():
    file = open("Input/day2.txt", "r")
    safe_count = 0

    for line in file:
        line_split = line.split(" ")
        report = []
        for s in line_split:
            report.append(int(s))

        is_safe = False
        for mutation in generate_mutations(report):
            if report_is_safe(mutation):
                is_safe = True
                break

        if is_safe:
            safe_count += 1

    return safe_count

def generate_mutations(report):
    mutations = [report]
    for i in range(len(report)):
        report_mod = report.copy()
        del report_mod[i]
        mutations.append(report_mod)

    return mutations


if __name__ == "__main__":

    print(task2())