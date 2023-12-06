from .main import part_1, part_2

TEST_INPUT = """Time:      7  15   30
Distance:  9  40  200"""


def test_part_1():
    assert part_1(TEST_INPUT) == 288


def test_part_2():
    assert part_2(TEST_INPUT) == 71503
