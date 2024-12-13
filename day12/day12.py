from collections import defaultdict

def day12_pt1(puzzle_in):
    max_x = len(puzzle_in[0])
    max_y = len(puzzle_in)

    scores_arr = [[0 for x in range(max_x)] for y in range(max_y)]

    basic_dirs = []
    for d in range(4):
        dx, dy = int((1j**d).real), int((1j**d).imag)
        basic_dirs.append((dx, dy))

    all_locations = set()
    for y in range(len(puzzle_in)):
        for x in range(len(puzzle_in[0])):
            all_locations.add((x, y))
            c = 0
            for dx, dy in basic_dirs:
                nx = dx + x
                ny = dy + y
                if not ((0 <= ny < max_y) and (0 <= nx < max_x)):
                    c += 1
                elif puzzle_in[ny][nx] != puzzle_in[y][x]:
                    c += 1

            scores_arr[y][x] = c

    # Perform flood to find all groups
    groups = defaultdict(list)
    i = 0
    while all_locations:
        frontier = [all_locations.pop()]

        while frontier:
            x, y = frontier.pop(0)
            groups[i].append((x, y))

            for dx, dy in basic_dirs:
                nx = dx + x
                ny = dy + y

                if not ((0 <= ny < max_y) and (0 <= nx < max_x)):
                    continue

                if ((nx, ny) in all_locations) and (puzzle_in[ny][nx] == puzzle_in[y][x]):
                    all_locations.remove((nx, ny))
                    frontier.append((nx, ny))
        i += 1

    total = 0
    for v in groups.values():
        group_size = len(v)
        group_perim = sum(scores_arr[y][x] for x,y in v)
        total += group_size * group_perim

    return total

def day12_pt2(puzzle_in):
    max_x = len(puzzle_in[0])
    max_y = len(puzzle_in)

    basic_dirs = []
    for d in range(4):
        dx, dy = int((1j**d).real), int((1j**d).imag)
        basic_dirs.append((dx, dy))

    all_locations = set()
    for y in range(len(puzzle_in)):
        for x in range(len(puzzle_in[0])):
            all_locations.add((x, y))

    # Perform flood to find all groups
    groups = defaultdict(list)
    i = 0
    while all_locations:
        frontier = [all_locations.pop()]

        while frontier:
            x, y = frontier.pop(0)
            groups[i].append((x, y))

            for dx, dy in basic_dirs:
                nx, ny = dx + x, dy + y

                if not ((0 <= ny < max_y) and (0 <= nx < max_x)):
                    continue

                if ((nx, ny) in all_locations) and (
                    puzzle_in[ny][nx] == puzzle_in[y][x]
                ):
                    all_locations.remove((nx, ny))
                    frontier.append((nx, ny))
        i += 1

    full_revolve_dirs = []
    for d in range(4):
        x1, y1 = int((1j**d).real), int((1j**d).imag)
        x2, y2 = int((1j ** (d + 1)).real), int((1j ** (d + 1)).imag)

        # Get the nonzero values - this is the easiest way
        x3 = x1 + x2
        y3 = y1 + y2

        x1, y1 = x1 + 1, y1 + 1
        x2, y2 = x2 + 1, y2 + 1
        x3, y3 = x3 + 1, y3 + 1
        full_revolve_dirs.append((x1, x2, x3, y1, y2, y3))

    total = 0
    for v in groups.values():
        x,y = v[0]
        group_value = puzzle_in[y][x]

        group_size = len(v)
        group_corners = 0

        for x, y in v:
            same = []
            for dy in [-1, 0, 1]:
                same.append([])
                for dx in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy

                    if not ((0 <= ny < max_y) and (0 <= nx < max_x)):
                        same[-1].append(False)
                    else:
                        val = puzzle_in[ny][nx] == group_value
                        same[-1].append(val)

            location_corners = 0

            for x1, x2, x3, y1, y2, y3 in full_revolve_dirs:
                if same[y1][x1] and same[y2][x2] and (not same[y3][x3]):
                    location_corners += 1

                if (not same[y1][x1]) and (not same[y2][x2]):
                    location_corners += 1

            group_corners += location_corners
        total += group_corners * group_size

    return total


if __name__ == "__main__":
    with open("AdventOfCode-2024/day12/day12_input.txt") as file:
        puzzle_in = [x.strip() for x in file.readlines()]

    print("Starting")
    print(f"The solution to 12.1 is {day12_pt1(puzzle_in)}")
    print(f"The solution to 12.2 is {day12_pt2(puzzle_in)}")
