def day2_pt1(puzzle_in):
    puzzle = []
    for row in puzzle_in:
        puzzle.append([int(x) for x in row.split()])

    count = 0
    for seq in puzzle:
        inc, dec, differ = True, True, True

        for i, j in zip(seq, seq[1:]):
            if not i < j:
                inc = False
            if not i > j:
                dec = False

            if not (abs(i-j) <= 3):
                differ = False
                break

            if not (inc or dec):
                break

        if (inc or dec) and differ:
            count += 1

    return count


def day2_pt2(puzzle_in):
    puzzle = []
    for row in puzzle_in:
        puzzle.append([int(x) for x in row.split()])

    count = 0
    for seq in puzzle:
        for i in range(-1, len(seq)):
            seq_mod = []
            if i == -1:
                seq_mod = seq
            else:
                seq_mod = seq[:i] + seq[i+1:]

            inc, dec, differ = True, True, True

            for i, j in zip(seq_mod, seq_mod[1:]):
                if not i < j:
                    inc = False
                if not i > j:
                    dec = False
                if not (abs(i - j) <= 3):
                    differ = False
                    break

                if not (inc or dec):
                    break

            if (inc or dec) and differ:
                count += 1
                break
    return count


if __name__ == "__main__":
    with open("AdventOfCode-2024/day2/day2_input.txt") as file:
        puzzle_in = [x.strip() for x in file.readlines()]

    print("Starting")
    print(f"The solution to 2.1 is {day2_pt1(puzzle_in)}")

    print(f"The solution to 2.2 is {day2_pt2(puzzle_in)}")
