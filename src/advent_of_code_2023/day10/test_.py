from .main import part_1, part_2

TEST_INPUT = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

TEST_INPUT_2 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""

TEST_INPUT_3 = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""


def test_part_1():
    assert part_1(TEST_INPUT) == 8


def test_part_2():
    assert part_2(TEST_INPUT_2) == 4
    assert part_2(TEST_INPUT_3) == 8


if __name__ == '__main__':
    test_part_1()
    test_part_2()
