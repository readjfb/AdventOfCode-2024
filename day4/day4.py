def day4_pt1(puzzle_in):
    count = 0
    len_X = len(puzzle_in[0])
    len_Y = len(puzzle_in)

    dirs = [
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
    ]

    for y in range(len_Y):
        for x in range(len_X):
            if puzzle_in[y][x] not in "XS":
                continue

            for i, j in dirs:
                if not (0 <= x + i * 3 < len_X):
                    continue

                if not (0 <= y + j * 3 < len_Y):
                    continue

                s = ""
                for d in range(4):
                    s += puzzle_in[y + j * d][x + i * d]

                if s in ("XMAS", "SAMX"):
                    count += 1

    return count


def day4_pt2(puzzle_in):
    score = 0
    len_X = len(puzzle_in[0])
    len_Y = len(puzzle_in)

    for y in range(1, len_Y - 1):
        for x in range(1, len_X - 1):
            if puzzle_in[y][x] != "A":
                continue

            spot_count = 0
            for i, j in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
                spot_count += (
                    puzzle_in[y + i][x + j] == "M" and puzzle_in[y - i][x - j] == "S"
                )

            score += spot_count >= 2

    return score


if __name__ == "__main__":
    with open("AdventOfCode-2024/day4/day4_input.txt") as file:
        puzzle_in = [x.strip() for x in file.readlines()]

    print("Starting")
    print(f"The solution to 4.1 is {day4_pt1(puzzle_in)}")

    print(f"The solution to 4.2 is {day4_pt2(puzzle_in)}")
