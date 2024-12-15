def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()


def day15_pt1(puzzle_in):
    grid = []

    x = None
    y = None
    i = 0
    while puzzle_in[i]:
        grid.append([x for x in puzzle_in[i]])

        if "@" in puzzle_in[i]:
            y = i
            x = puzzle_in[i].index("@")
        i += 1
    i += 1

    moves = []
    while i < len(puzzle_in):
        moves += [x for x in puzzle_in[i]]

        i += 1

    for move in moves:
        if move == "<":
            dx = -1
            dy = 0
        elif move == ">":
            dx = 1
            dy = 0
        elif move == "^":
            dx = 0
            dy = -1
        elif move == "v":
            dx = 0
            dy = 1

        if grid[y + dy][x + dx] == ".":
            grid[y + dy][x + dx] = "@"
            grid[y][x] = "."
            x += dx
            y += dy
        elif grid[y + dy][x + dx] == "#":
            continue
        elif grid[y + dy][x + dx] == "O":
            # Find if there is a open spot in this direction
            nx, ny = x + dx, y + dy
            while grid[ny][nx] == "O":
                nx, ny = nx + dx, ny + dy
            if grid[ny][nx] == "#":
                continue
            elif grid[ny][nx] == ".":
                grid[ny][nx] = "O"
                grid[y + dy][x + dx] = "@"
                grid[y][x] = "."
                x += dx
                y += dy
            else:
                print("Something went wrong 1")

        else:
            print(move, grid[y + dy][x + dx], "Something went wrong 2")

    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "O":
                total += (100 * y) + x
    return total


def day15_pt2(puzzle_in):
    grid = []

    x = None
    y = None
    i = 0
    while puzzle_in[i]:
        next_row = []
        for v in puzzle_in[i]:
            if v == "O":
                next_row += ["[", "]"]
            elif v == "@":
                next_row += ["@", "."]
            else:
                next_row += [v] * 2

        if "@" in next_row:
            x = next_row.index("@")
            y = i

        grid.append(next_row)
        i += 1
    i += 1

    moves = []
    while i < len(puzzle_in):
        moves += [x for x in puzzle_in[i]]

        i += 1

    for move in moves:
        if move == "<":
            dx, dy = -1, 0
        elif move == ">":
            dx, dy = 1, 0
        elif move == "^":
            dx, dy = 0, -1
        elif move == "v":
            dx, dy = 0, 1

        if grid[y + dy][x + dx] == ".":
            grid[y + dy][x + dx] = "@"
            grid[y][x] = "."
            x += dx
            y += dy
        elif grid[y + dy][x + dx] == "#":
            continue
        elif grid[y + dy][x + dx] in "[]":
            unresolved = []
            boxes_to_move = set()
            found_solve = True
            unresolved.append((x + dx, y + dy))

            while unresolved:
                next_box = unresolved.pop(0)
                if next_box in boxes_to_move:
                    continue
                nx, ny = next_box
                if grid[ny][nx] == "[":
                    unresolved.append((nx + 1, ny))
                elif grid[ny][nx] == "]":
                    unresolved.append((nx - 1, ny))

                if grid[ny + dy][nx + dx] in "[]":
                    unresolved.append((nx + dx, ny + dy))
                    boxes_to_move.add(next_box)
                elif grid[ny + dy][nx + dx] == "#":
                    found_solve = False
                    break
                elif grid[ny + dy][nx + dx] == ".":
                    boxes_to_move.add(next_box)
                    continue
                else:
                    print(grid[ny + dy][nx + dx], "Something went wrong 3")

            if not found_solve:
                continue

            boxes_to_move = list(boxes_to_move)

            if dx == 1:
                boxes_to_move.sort(key=lambda x: x[0], reverse=True)
            elif dx == -1:
                boxes_to_move.sort(key=lambda x: x[0], reverse=False)
            if dy == 1:
                boxes_to_move.sort(key=lambda x: x[1], reverse=True)
            elif dy == -1:
                boxes_to_move.sort(key=lambda x: x[1], reverse=False)

            for box in boxes_to_move:
                bx, by = box
                grid[by + dy][bx + dx], grid[by][bx] = (
                    grid[by][bx],
                    grid[by + dy][bx + dx],
                )
            grid[y + dy][x + dx], grid[y][x] = (
                grid[y][x],
                grid[y + dy][x + dx],
            )

            x += dx
            y += dy

        else:
            print(move, grid[y + dy][x + dx], "Something went wrong 2")

    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "[":
                total += (100 * y) + x

    return total


if __name__ == "__main__":
    with open("AdventOfCode-2024/day15/day15_input.txt") as file:
        puzzle_in = [x.strip() for x in file.readlines()]

    print("Starting")
    print(f"The solution to 15.1 is {day15_pt1(puzzle_in)}")

    print(f"The solution to 15.2 is {day15_pt2(puzzle_in)}")
