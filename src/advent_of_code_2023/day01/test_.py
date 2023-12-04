from .main import part_1, part_2

TEST_INPUT = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

TEST_2_INPUT = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def test_part_1():
    assert part_1(TEST_INPUT) == 142


def test_part_2():
    assert part_2(TEST_2_INPUT) == 281
