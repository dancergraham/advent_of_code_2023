import itertools
from pathlib import Path


def parse_input(input_str: str, expansion=2):
    galaxies = set()
    occupied_rows = set()
    occupied_columns = set()
    for y, line in enumerate(input_str.split('\n')):
        for x, char in enumerate(line):
            if char == '#':
                galaxies.add((x, y))
                occupied_rows.add(y)
                occupied_columns.add(x)

    row_mapping = {}
    column_mapping = {}
    x_dest, y_dest = 0, 0
    for column in range(x + 1):
        if column not in occupied_columns:
            x_dest += expansion - 1
        column_mapping[column] = x_dest
        x_dest += 1
    for row in range(y + 1):
        if row not in occupied_rows:
            y_dest += expansion - 1
        row_mapping[row] = y_dest
        y_dest += 1
    mapped_galaxies = set()
    for galaxy in galaxies:
        x, y = galaxy
        mapped_galaxies.add((column_mapping[x], row_mapping[y]))

    return mapped_galaxies


def main():
    print(f"Part 1: {part_1(Path('input.txt').read_text())}")
    print(f"Part 2: {part_2(Path('input.txt').read_text())}")


def part_1(input_str):
    starmap = parse_input(input_str)
    return sum(
        manhatten_distance(combination)
        for combination in itertools.combinations(starmap, 2)
    )


def manhatten_distance(tup):
    return abs(tup[0][0] - tup[1][0]) + abs(tup[0][1] - tup[1][1])


def part_2(input_str, expansion=1000000):
    starmap = parse_input(input_str, expansion=expansion)
    return sum(
        manhatten_distance(combination)
        for combination in itertools.combinations(starmap, 2)
    )


if __name__ == '__main__':
    main()
