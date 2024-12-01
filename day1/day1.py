from collections import Counter

def day1_pt1(puzzle_in):
    left, right = [], []
    for row in puzzle_in:
        left.append(int(row.split(" ")[0]))
        right.append(int(row.split(" ")[-1]))

    left.sort()
    right.sort()

    return sum(abs(l-r) for l, r in zip(left, right))


def day1_pt2(puzzle_in):
    left, right = [], []
    for row in puzzle_in:
        left.append(int(row.split(" ")[0]))
        right.append(int(row.split(" ")[-1]))

    counts_right = Counter(right)

    return sum(counts_right[v] * v for v in left)

if __name__ == "__main__":
    with open("AdventOfCode-2024/day1/day1_input.txt") as file:
        puzzle_in = [x.strip() for x in file.readlines()]

    print(f"The solution to 1.1 is {day1_pt1(puzzle_in)}")
    print(f"The solution to 1.2 is {day1_pt2(puzzle_in)}")
