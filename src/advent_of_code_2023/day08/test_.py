from .main import part_1, part_2

TEST_INPUT = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

TEST_INPUT_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

TEST_INPUT_3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


def test_part_1():
    assert part_1(TEST_INPUT) == 2
    assert part_1(TEST_INPUT_2) == 6


def test_part_2():
    assert part_2(TEST_INPUT_3) == 6
