import multiprocessing


# Use recursive backtracking to assess
def pt1_turtle(rem_vals, cur_sum, target):
    if not rem_vals:
        return cur_sum == target

    if cur_sum >= target:
        return False

    return pt1_turtle(rem_vals[1:], cur_sum + rem_vals[0], target) or pt1_turtle(
        rem_vals[1:], cur_sum * rem_vals[0], target
    )


def pt1_turtle_passthrough(data):
    target, values = data

    if pt1_turtle(values[1:], values[0], target):
        return target
    return 0


def day7_pt1(puzzle_in):
    targets, vals = [], []
    for line in puzzle_in:
        s = line.split(": ")
        targets.append(int(s[0]))
        vals.append([int(x) for x in s[1].split()])

    with multiprocessing.Pool() as pool:
        total = sum(pool.map(pt1_turtle_passthrough, zip(targets, vals)))
    pool.join()

    return total


# Use recursive backtracking to assess
def pt2_turtle(rem_vals, cur_sum, target):
    if cur_sum > target:
        return False

    if not rem_vals:
        return cur_sum == target

    return (
        pt2_turtle(rem_vals[1:], cur_sum + rem_vals[0], target)
        or pt2_turtle(rem_vals[1:], cur_sum * rem_vals[0], target)
        or pt2_turtle(rem_vals[1:], int(str(cur_sum) + str(rem_vals[0])), target)
    )


def pt2_turtle_passthrough(data):
    target, values = data

    if pt2_turtle(values[1:], values[0], target):
        return target

    return 0


def day7_pt2(puzzle_in):
    targets, vals = [], []
    for line in puzzle_in:
        s = line.split(": ")
        targets.append(int(s[0]))
        vals.append([int(x) for x in s[1].split()])

    with multiprocessing.Pool() as pool:
        total = sum(pool.map(pt2_turtle_passthrough, zip(targets, vals)))
    pool.join()

    return total


if __name__ == "__main__":
    with open("AdventOfCode-2024/day7/day7_input.txt") as file:
        puzzle_in = [x.strip() for x in file.readlines()]

    print(f"The solution to 7.1 is {day7_pt1(puzzle_in)}")

    print(f"The solution to 7.2 is {day7_pt2(puzzle_in)}")
