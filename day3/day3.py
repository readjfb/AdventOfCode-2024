import re


def day3_pt1(puzzle_in):
    s = 0
    for row in puzzle_in:
        for v in re.findall(r"mul\((\d+,\d+)\)", row):
            i, j = v.split(",")
            s += int(i) * int(j)
    return s


def day3_pt2(puzzle_in):
    s = 0

    active = True
    for row in puzzle_in:
        for p in re.findall(r"mul\((\d+,\d+)\)|(do)\(\)|(don't)\(\)", row):
            if "don't" in p:
                active = False
            elif "do" in p:
                active = True
            elif active:
                i, j = p[0].split(",")
                s += int(i) * int(j)
    return s


if __name__ == "__main__":
    with open("AdventOfCode-2024/day3/day3_input.txt") as file:
        puzzle_in = [x.strip() for x in file.readlines()]

    print("Starting")
    print(f"The solution to 3.1 is {day3_pt1(puzzle_in)}")
    print(f"The solution to 3.2 is {day3_pt2(puzzle_in)}")
