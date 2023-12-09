from .main import part_1, part_2

TEST_INPUT = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def test_part_1():
    assert part_1(TEST_INPUT) == 114


def test_part_2():
    assert part_2(TEST_INPUT) == 2
