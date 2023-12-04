from pathlib import Path

DIGITS = {str(i): i for i in range(1, 10)} | \
         {x: i + 1 for i, x in
          enumerate("one, two, three, four, five, six, seven, eight, nine"
          .split(
              ", "))}


def parse_input(input_str: str):
    return input_str


def main():
    print(f"{part_1(Path('input.txt').read_text())}")
    print(f"{part_2(Path('input.txt').read_text())}")


def part_1(input_str):
    answer = 0
    for line in input_str.splitlines():
        digits = [int(x) for x in line if x.isdigit()]
        answer += 10 * digits[0]
        answer += digits[-1]
    return answer


def minmax(line):
    min_ = [1e6, None]
    max_ = [-1, None]
    for digit, value in DIGITS.items():
        pos = line.find(digit)
        if pos != -1 and pos < min_[0]:
            min_ = [pos, value]
        pos = line.rfind(digit)
        if pos > max_[0]:
            max_ = [pos, value]
    return int(f"{min_[1]}{max_[1]}")


def part_2(input_str):
    answer = 0
    for line in input_str.splitlines():
        answer += minmax(line)
    return answer


if __name__ == '__main__':
    main()
