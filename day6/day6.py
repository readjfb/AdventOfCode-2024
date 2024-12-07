from copy import deepcopy

def day6_pt1(puzzle_in):
    # Find starting location
    location = None
    direction = 3
    for y, l in enumerate(puzzle_in):
        for x, v in enumerate(l):
            if v == "^":
                location = (x, y)
                break

    locations = set()

    max_x = len(puzzle_in[0])
    max_y = len(puzzle_in)

    x, y = location

    while 0 <= x < max_x and 0<= y < max_y:
        locations.add((x, y))

        dx = int((1j**direction).real)
        dy = int((1j**direction).imag)
        new_x = x + dx
        new_y = y + dy

        if not (0 <= new_x < max_x and 0 <= new_y < max_y):
            return len(locations)

        if puzzle_in[new_y][new_x] == "#":
            direction = (direction + 1) % 4
        else:
            x = new_x
            y = new_y


def day6_pt2(puzzle_in):
    # Find starting location
    starting_location = None
    direction = 3
    for y, l in enumerate(puzzle_in):
        for x, v in enumerate(l):
            if v == "^":
                starting_location = (x, y)
                break

    locations = set()

    max_x = len(puzzle_in[0])
    max_y = len(puzzle_in)

    x, y = starting_location

    while 0 <= x < max_x and 0 <= y < max_y:
        locations.add((x, y))

        dx = int((1j**direction).real)
        dy = int((1j**direction).imag)
        new_x = x + dx
        new_y = y + dy

        if not (0 <= new_x < max_x and 0 <= new_y < max_y):
            break

        if puzzle_in[new_y][new_x] == "#":
            direction = (direction + 1) % 4
        else:
            x = new_x
            y = new_y

    # Try placing obstructions at each position, other than the starting position
    count = 0
    for i, new_block in enumerate(locations):
        if new_block == starting_location:
            continue

        if puzzle_in[new_block[1]][new_block[0]] == "#":
            continue

        # Check if there's another hittable block based on the new block

        x, y = starting_location
        direction = 3

        blocks_hit = set()
        while 0 <= x < max_x and 0 <= y < max_y:
            dx = int((1j**direction).real)
            dy = int((1j**direction).imag)
            new_x = x + dx
            new_y = y + dy

            if not (0 <= new_x < max_x and 0 <= new_y < max_y):
                break

            if ((new_x, new_y) == new_block) or puzzle_in[new_y][new_x] == "#":
                if (new_x, new_y, direction) in blocks_hit:
                    count += 1
                    break

                blocks_hit.add((new_x, new_y, direction))
                direction = (direction + 1) % 4
            else:
                x = new_x
                y = new_y
    return count




if __name__ == "__main__":
    with open("AdventOfCode-2024/day6/day6_input.txt") as file:
        puzzle_in = [x.strip() for x in file.readlines()]

    print(f"The solution to 6.1 is {day6_pt1(puzzle_in)}")

    print(f"The solution to 6.2 is {day6_pt2(puzzle_in)}")
