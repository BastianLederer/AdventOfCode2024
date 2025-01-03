from typing import Set, Tuple, Generator

Point = Tuple[int, int]

DIRS = NORTH, EAST, SOUTH, WEST = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def manhattan(dist: int) -> Generator[Point, None, None]:
    for y in range(-dist, dist + 1):
        for x in range(-(dist - abs(y)), dist - abs(y) + 1):
            yield x, y

def read_input(path="Input/day20.txt") -> Tuple[Set[Point], Point, Point]:
    points: Set[Point] = set()
    start_pos = end_pos = None
    with open(path) as f:
        for y, line in enumerate(f):
            line = line.strip()
            if not line:
                break
            for x, ch in enumerate(line):
                if ch in 'SE.':
                    points.add((x, y))
                    if ch == 'S':
                        start_pos = (x, y)
                    elif ch == 'E':
                        end_pos = (x, y)
    assert start_pos is not None
    assert end_pos is not None
    return points, start_pos, end_pos

def get_track(points: Set[Point], start_pos: Point, end_pos: Point) -> dict:
    x, y = start_pos
    track = {}  # pos: score
    score = 0
    while (x, y) != end_pos:
        track[x, y] = score
        for dx, dy in DIRS:
            newpos = x + dx, y + dy
            if newpos not in track and newpos in points:
                x, y = newpos
                break
        else:
            raise Exception("No route to end")
        score += 1
    track[x, y] = score  # End
    return track

def num_cheats(track: dict, dist: int, saving_required: int) -> int:
    tot = 0
    for (x, y), score in track.items():
        for dx, dy in manhattan(dist):
            if dy == dx == 0:
                continue
            x2, y2 = x + dx, y + dy

            if (x2, y2) in track:
                saved = track[x2, y2] - score - abs(dx) - abs(dy)
                if saved >= saving_required:
                    tot += 1

    return tot

# Main execution
points, start_pos, end_pos = read_input()
track = get_track(points, start_pos, end_pos)
print(num_cheats(track, 2, 100))
print(num_cheats(track, 20, 100))