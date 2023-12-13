from .main import part_1, part_2

TEST_INPUT = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


def test_part_1():
    assert part_1(TEST_INPUT) == 374


def test_part_2():
    assert part_2(TEST_INPUT, expansion=10) == 1030
    assert part_2(TEST_INPUT, expansion=100) == 8410


if __name__ == '__main__':
    test_part_1()
    test_part_2()
