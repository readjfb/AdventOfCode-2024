def day10_pt1(puzzle_in):
    puzzle = [[int(x) for x in y] for y in puzzle_in]

    trailheads = []
    visited = set()
    frontier = []
    next_frontier = set()

    max_x, max_y = len(puzzle[0]), len(puzzle)

    scores_df = [[set() for x in range(max_x)] for y in range(max_y)]

    for y in range(max_y):
        for x in range(max_x):
            if puzzle[y][x] == 0:
                trailheads.append((x, y))
            elif puzzle[y][x] == 9:
                scores_df[y][x].add((x, y))
                next_frontier.add((x, y))
                visited.add((x, y))

    while next_frontier:
        frontier = []
        for x, y in next_frontier:
            frontier.append((x, y, set(scores_df[y][x])))
        next_frontier = set()

        while frontier:
            x, y, value = frontier.pop(0)
            for e in range(4):
                dx, dy = (1j**e).real, (1j**e).imag
                nx, ny = int(x + dx), int(y + dy)

                if 0 <= nx < max_x and 0 <= ny < max_y:
                    if puzzle[y][x] - puzzle[ny][nx] != 1:
                        continue

                    scores_df[ny][nx].update(value)

                    if (nx, ny) not in visited:
                        next_frontier.add((nx, ny))
                        visited.add((nx, ny))

    return sum(len(scores_df[y][x]) for x, y in trailheads)


def day10_pt2(puzzle_in):
    puzzle = [[int(x) for x in y] for y in puzzle_in]

    trailheads = []
    visited = set()
    frontier = []
    next_frontier = set()

    max_x, max_y = len(puzzle[0]), len(puzzle)

    scores_df = [[0 for x in range(max_x)] for y in range(max_y)]

    for y in range(max_y):
        for x in range(max_x):
            if puzzle[y][x] == 0:
                trailheads.append((x, y))
            elif puzzle[y][x] == 9:
                scores_df[y][x] = 1
                next_frontier.add((x, y))
                visited.add((x, y))

    while next_frontier:
        frontier = []
        for x, y in next_frontier:
            frontier.append((x, y, scores_df[y][x]))
        next_frontier.clear()

        while frontier:
            x, y, value = frontier.pop(0)
            for e in range(4):
                dx, dy = (1j**e).real, (1j**e).imag
                nx, ny = int(x + dx), int(y + dy)

                if 0 <= nx < max_x and 0 <= ny < max_y:
                    if not puzzle[y][x] - puzzle[ny][nx] == 1:
                        continue

                    scores_df[ny][nx] += value

                    if (nx, ny) not in visited:
                        next_frontier.add((nx, ny))
                        visited.add((nx, ny))

    return sum(scores_df[y][x] for x, y in trailheads)


if __name__ == "__main__":
    with open("AdventOfCode-2024/day10/day10_input.txt") as file:
        puzzle_in = [x.strip() for x in file.readlines()]

    print("Starting")
    print(f"The solution to 10.1 is {day10_pt1(puzzle_in)}")
    print(f"The solution to 10.2 is {day10_pt2(puzzle_in)}")
