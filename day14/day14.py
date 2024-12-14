import re
from collections import defaultdict


def day14_pt1(puzzle_in):
    all_rows = []
    for line in puzzle_in:
        result = re.findall(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        all_rows.append(tuple(int(x) for x in result[0]))

    seconds = 100
    max_x, max_y = 101, 103

    position_counts = defaultdict(int)
    for robot in all_rows:
        ix, iy, vx, vy = robot

        end_x = (ix + (vx * seconds)) % max_x
        end_y = (iy + (vy * seconds)) % max_y

        position_counts[(end_x, end_y)] += 1

    quadrants = [0, 0, 0, 0]
    for (x, y), v in position_counts.items():
        if x == max_x // 2 or y == max_y // 2:
            continue

        i = ((x / max_x) < 0.5) + (((y / max_y) < 0.5) * 2)
        quadrants[i] += v

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def day14_pt2(puzzle_in):
    # Tried: printing to console (couldn't see anything)
    # Printing to a file
    # Looking for a sequence where the middle is full/horizontal symmetry
    #
    # see how ong until all robots are on unique locations?
    all_rows = []
    for line in puzzle_in:
        result = re.findall(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        all_rows.append(tuple(int(x) for x in result[0]))

    seconds = 100
    max_x, max_y = 101, 103

    while seconds < 1_000_000:
        seconds += 1
        unique_pos = set()
        for ix, iy, vx, vy in all_rows:
            end_x = (ix + (vx * seconds)) % max_x
            end_y = (iy + (vy * seconds)) % max_y

            if (end_x, end_y) in unique_pos:
                break

            unique_pos.add((end_x, end_y))
        else:
            return seconds

    return seconds


def display_part(seconds):
    # idk maybe see how long until they're on unique locations?
    all_rows = []
    for line in puzzle_in:
        result = re.findall(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        all_rows.append(tuple(int(x) for x in result[0]))

    max_x, max_y = 101, 103

    screen = [[" " for x in range(max_x)] for y in range(max_y)]

    for robot in all_rows:
        ix, iy, vx, vy = robot

        end_x = (ix + (vx * seconds)) % max_x
        end_y = (iy + (vy * seconds)) % max_y

        screen[end_y][end_x] = "X"

    with open("display.txt", "w") as file:
        for s in screen:
            file.write("".join(s))


if __name__ == "__main__":
    with open("AdventOfCode-2024/day14/day14_input.txt") as file:
        puzzle_in = [x.strip() for x in file.readlines()]

    print("Starting")
    print(f"The solution to 14.1 is {day14_pt1(puzzle_in)}")
    print(f"The solution to 14.2 is {day14_pt2(puzzle_in)}")

    # display_part(day14_pt2(puzzle_in))
