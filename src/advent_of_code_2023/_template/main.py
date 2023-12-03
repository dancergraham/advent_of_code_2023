from pathlib import Path


def parse_input(input_str: str):
    return input_str


def main():
    print(f"{part_1(Path('input.txt').read_text())}")
    print(f"{part_2(Path('input.txt').read_text())}")


def part_1(input_str):
    answer = 0
    input_str = parse_input(input_str)
    return answer


def part_2(input_str):
    answer = 0
    input_str = parse_input(input_str)
    return answer


if __name__ == '__main__':
    main()
