from .main import part_1, part_2

TEST_INPUT = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def test_part_1():
    assert part_1(TEST_INPUT) == 4361


def test_part_2():
    assert part_2(TEST_INPUT) == 467835
