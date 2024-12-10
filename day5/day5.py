def day5_pt1(puzzle_in):
    i = 0
    rules = []
    while True:
        if puzzle_in[i] == "":
            i += 1
            break
        k, j = puzzle_in[i].split("|")
        rules.append((k, j))
        i += 1

    pages = []
    page_sets = []
    while i < len(puzzle_in):
        n = [x for x in puzzle_in[i].split(",")]
        pages.append(n)
        page_sets.append(set(n))
        i += 1

    def validate_page(page, page_set):
        for r1, r2 in rules:
            if r1 in page_set and r2 in page_set:
                if not (page.index(r1) < page.index(r2)):
                    return False
        return True

    tally = sum(
        int(page[len(page) // 2])
        for page, page_set in zip(pages, page_sets)
        if validate_page(page, page_set)
    )

    return tally


def day5_pt2(puzzle_in):
    def validate_page(page, page_set):
        for r1, r2 in rules:
            if r1 in page_set and r2 in page_set:
                if not (page.index(r1) < page.index(r2)):
                    return False
        return True

    i = 0
    rules = []
    while True:
        if puzzle_in[i] == "":
            i += 1
            break
        k, j = puzzle_in[i].split("|")
        rules.append((int(k), int(j)))
        i += 1

    pages = []
    page_sets = []
    while i < len(puzzle_in):
        pages.append([int(x) for x in puzzle_in[i].split(",")])
        page_sets.append(set(pages[-1]))
        i += 1

    bad_pgs = []
    bad_pg_sets = []
    for page, page_set in zip(pages, page_sets):
        if not validate_page(page, page_set):
            bad_pgs.append(page)
            bad_pg_sets.append(page_set)

    tally = 0
    for page, pg_set in zip(bad_pgs, bad_pg_sets):
        # Swap positions if things are bad
        new_page = page[:]

        selected_rules = [x for x in rules if x[0] in pg_set and x[1] in pg_set]

        complete = False

        while not complete:
            complete = True
            for i, (r1, r2) in enumerate(selected_rules):

                old_r1, old_r2 = new_page.index(r1), new_page.index(r2)

                if not (old_r1 < old_r2):
                    complete = False
                    new_page[old_r1], new_page[old_r2] = (
                        new_page[old_r2],
                        new_page[old_r1],
                    )

        tally += new_page[len(new_page) // 2]

    return tally


if __name__ == "__main__":
    with open("AdventOfCode-2024/day5/day5_input.txt") as file:
        puzzle_in = [x.strip() for x in file.readlines()]

    print("Starting")
    print(f"The solution to 5.1 is {day5_pt1(puzzle_in)}")

    print(f"The solution to 5.2 is {day5_pt2(puzzle_in)}")
