from collections import defaultdict


def day9_pt1(puzzle_in):
    puzzle = puzzle_in[0]

    puzzle_list = []
    counter = 0
    for i, c in enumerate(puzzle):
        if i % 2 == 0:
            puzzle_list += [counter] * int(c)
            counter += 1
        else:
            puzzle_list += [None] * int(c)

    i = 0
    reverse_i = len(puzzle_list) - 1

    while i <= reverse_i:
        if puzzle_list[i] is None:
            puzzle_list[i] = puzzle_list[reverse_i]
            puzzle_list[reverse_i] = None

            while puzzle_list[reverse_i] is None:
                reverse_i -= 1
        i += 1

    s = 0
    for i, v in enumerate(puzzle_list):
        if v is None:
            break
        s += i * v

    return s


def day9_pt2(puzzle_in):
    puzzle = puzzle_in[0]

    blocks = []
    spaces = []

    # For numbers:
    # (value, length, curr_position)

    # For spaces
    # (length, starting_index)

    counter = 0
    position = 0

    for i, length in enumerate(puzzle):
        if i % 2 == 0:
            blocks.append([counter, int(length), position])
            counter += 1
        else:
            spaces.append([int(length), position])
        position += int(length)

    spaces_search_pos = defaultdict(int)
    for block in reversed(blocks):
        block_len = block[1]
        space_position = spaces_search_pos[block_len]

        l_spaces = len(spaces)
        while space_position < l_spaces:
            space = spaces[space_position]
            if block[2] <= space[1]:
                break

            if block[1] <= space[0]:
                spaces.append([block[1], block[2]])
                block[2] = space[1]
                space[0] -= block[1]
                space[1] += block[1]
                break

            space_position += 1
        spaces_search_pos[block_len] = space_position

    blocks.sort(key=lambda x: x[2])

    s = 0
    for value, length, position in blocks:
        # Formula for sum of numbers between x and y is S = (y-x)(x + y) / 2
        # Also equals S = length(position + position + length - 1) / 2
        s += ((length * ((2 * position) + length - 1)) // 2) * value

    return s


if __name__ == "__main__":
    with open("AdventOfCode-2024/day9/day9_input.txt") as file:
        puzzle_in = [x.strip() for x in file.readlines()]

    print("Starting")
    print(f"The solution to 9.1 is {day9_pt1(puzzle_in)}")
    print(f"The solution to 9.2 is {day9_pt2(puzzle_in)}")
