from functools import lru_cache


# Leaving this in for posterity, mostly because I'm happy that it worked with
# no typos on the first try
def day11_pt1(puzzle_in):
    stones = [int(x) for x in puzzle_in[0].split(" ")]

    for _ in range(25):
        new_stones = []
        for stone in stones:
            str_stone = str(stone)
            if stone == 0:
                new_stones.append(1)
                continue
            num_digits = len(str_stone)
            if num_digits % 2 == 0:
                new_stones += [
                    int(str_stone[: num_digits // 2]),
                    int(str_stone[num_digits // 2 :]),
                ]
                continue
            new_stones.append(stone * 2024)

        stones = new_stones

    return len(stones)


@lru_cache(None)
def num_digits(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count


@lru_cache(None)
def recursive_parse(stone, steps_left):
    if steps_left <= 0:
        return 1

    if stone == 0:
        return recursive_parse(1, steps_left - 1)

    digits = num_digits(stone)

    if digits % 2 == 0:
        cut_factor = 10 ** (digits // 2)

        front = stone // cut_factor
        back = stone % cut_factor
        return recursive_parse(front, steps_left - 1) + recursive_parse(
            back, steps_left - 1
        )

    else:
        return recursive_parse(stone * 2024, steps_left - 1)


def day11_pt2(puzzle_in):
    stones = [int(x) for x in puzzle_in[0].split(" ")]

    return sum([recursive_parse(stone, 75) for stone in stones])


if __name__ == "__main__":
    with open("AdventOfCode-2024/day11/day11_input.txt") as file:
        puzzle_in = [x.strip() for x in file.readlines()]

    print("Starting")
    print(f"The solution to 11.1 is {day11_pt1(puzzle_in)}")
    print(f"The solution to 11.2 is {day11_pt2(puzzle_in)}")
