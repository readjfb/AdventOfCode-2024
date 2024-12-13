from scipy.optimize import linprog
from re import findall

def wrapper(data):
    (ax, ay), (bx, by), (tx, ty) = data

    A_eq = [[ax, bx],
            [ay, by]]
    b_eq = [tx, ty]

    bounds = [(0, None),
              (0, None)]  # A >= 0  # B >= 0

    cost = [3, 1]

    result = linprog(cost, A_eq=A_eq, b_eq=b_eq, bounds=bounds)

    if not result.success:
        return 0
    A, B = result.x

    if round(A, 3) % 1 == 0:
        return (3 * round(A)) + round(B)
    return 0

def day13_pt1(puzzle_in):
    # Linear optimization process

    # Position.x = A*X1 + B*X2
    # Position.y = A*Y1 + B*Y2
    # Cost = 3A + 1B
    # Minimize the cost

    all_res = []
    for row in puzzle_in:
        try:
            all_res.append(findall(r"X\+(\d+), Y\+(\d+)|X=(\d+), Y=(\d+)", row)[0])
        except IndexError:
            continue

    button_a = [(x, y) for x, y, _, __ in all_res[0::3]]
    button_b = [(x, y) for x, y, _, __ in all_res[1::3]]
    targets = [(x, y) for _, __, x, y  in all_res[2::3]]

    total_cost = 0
    for data in zip(button_a, button_b, targets):
        total_cost += wrapper(data)
    return total_cost


def day13_pt2(puzzle_in):
    all_res = []
    for row in puzzle_in:
        try:
            all_res.append(findall(r"X\+(\d+), Y\+(\d+)|X=(\d+), Y=(\d+)", row)[0])
        except IndexError:
            continue

    addin = 10000000000000
    button_a = [(x, y) for x, y, _, __ in all_res[0::3]]
    button_b = [(x, y) for x, y, _, __ in all_res[1::3]]
    targets = [(int(x) + addin, int(y) + addin) for _, __, x, y in all_res[2::3]]

    total_cost = 0
    for data in zip(button_a, button_b, targets):
        total_cost += wrapper(data)
    return total_cost


if __name__ == "__main__":
    with open("AdventOfCode-2024/day13/day13_input.txt") as file:
        puzzle_in = [x.strip() for x in file.readlines()]

    print("Starting")
    print(f"The solution to 13.1 is {day13_pt1(puzzle_in)}")
    print(f"The solution to 13.2 is {day13_pt2(puzzle_in)}")
