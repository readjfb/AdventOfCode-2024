from collections import defaultdict
from fractions import Fraction


def day8_pt1(puzzle_in):
    antenna_pos = defaultdict(list)

    for y, row in enumerate(puzzle_in):
        for x, v in enumerate(row):
            antenna_pos[v].append((x, y))
    del antenna_pos["."]

    x_max = len(puzzle_in[0])
    y_max = len(puzzle_in)

    found_pos = set()

    for type, positions in antenna_pos.items():
        for i, start_val in enumerate(positions):
            for other_val in positions[i + 1 :]:
                dx = start_val[0] - other_val[0]
                dy = start_val[1] - other_val[1]

                p0 = (other_val[0] - dx, other_val[1] - dy)
                p1 = (start_val[0] + dx, start_val[1] + dy)

                if (0 <= p0[0] < x_max) and (0 <= p0[1] < y_max):
                    found_pos.add(p0)
                if (0 <= p1[0] < x_max) and (0 <= p1[1] < y_max):
                    found_pos.add(p1)

    return len(found_pos)


def day8_pt2(puzzle_in):
    antenna_pos = defaultdict(list)

    for y, row in enumerate(puzzle_in):
        for x, v in enumerate(row):
            antenna_pos[v].append((x, y))
    del antenna_pos["."]

    x_max = len(puzzle_in[0])
    y_max = len(puzzle_in)

    found_pos = set()

    for type, positions in antenna_pos.items():
        for i, start_val in enumerate(positions):
            for other_val in positions[i + 1 :]:
                d = Fraction(start_val[0] - other_val[0], start_val[1] - other_val[1])

                dx, dy = d.numerator, d.denominator

                x, y = start_val
                while (0 <= x < x_max) and (0 <= y < y_max):
                    found_pos.add((x, y))
                    x += dx
                    y += dy

                x, y = start_val
                while (0 <= x < x_max) and (0 <= y < y_max):
                    found_pos.add((x, y))
                    x -= dx
                    y -= dy

    return len(found_pos)


if __name__ == "__main__":
    with open("AdventOfCode-2024/day8/day8_input.txt") as file:
        puzzle_in = [x.strip() for x in file.readlines()]

    print("Starting")
    print(f"The solution to 8.1 is {day8_pt1(puzzle_in)}")
    print(f"The solution to 8.2 is {day8_pt2(puzzle_in)}")
