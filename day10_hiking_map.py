def task1():
    file = open("Input/day10.txt", "r")
    topo = []
    for line in file:
        topo.append(list(line.replace("\n", "")))


    targets = []
    for i in range(len(topo)):
        for k in range(len(topo[0])):
            if topo[i][k] == "9":
                targets.append((i, k))

    score = 0
    for i in range(len(topo)):
        for k in range(len(topo[0])):
            if topo[i][k] == "0":
                score += calculate_score(topo, (i,k))

    return score
def calculate_score(topo, trailhead):
    score = 0
    found_targets = []
    current_routepoints = [trailhead]
    while len(current_routepoints) > 0:
        for routepoint in current_routepoints:

            if int(topo[routepoint[0]][routepoint[1]]) == 9:    # found targets restraint weggemacht ez task2 gelöst
                found_targets.append(routepoint)
                score += 1
                current_routepoints.remove(routepoint)
                continue


            if routepoint[0] < len(topo) - 1 and int(topo[routepoint[0] + 1][routepoint[1]]) == int(topo[routepoint[0]][routepoint[1]]) + 1:
                current_routepoints.append((routepoint[0] + 1, routepoint[1]))
            if routepoint[1] < len(topo[0]) - 1 and  int(topo[routepoint[0]][routepoint[1] + 1]) == int(topo[routepoint[0]][routepoint[1]]) + 1:
                current_routepoints.append((routepoint[0], routepoint[1] + 1))
            if routepoint[0] > 0 and int(topo[routepoint[0] - 1][routepoint[1]]) == int(topo[routepoint[0]][routepoint[1]]) + 1:
                current_routepoints.append((routepoint[0] - 1, routepoint[1]))
            if routepoint[1] > 0 and int(topo[routepoint[0]][routepoint[1] - 1]) == int(topo[routepoint[0]][routepoint[1]]) + 1:
                current_routepoints.append((routepoint[0], routepoint[1] - 1))

            current_routepoints.remove(routepoint)

    return score

def main():
    print(task1())

if __name__ == "__main__":
    main()



