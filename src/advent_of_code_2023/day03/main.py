import math
from pathlib import Path


def get_neighbours(start, stop):
    for x in range(start[0] - 1, stop[0] + 2):
        for y in range(start[1] - 1, stop[1] + 2):
            if 0 <= min(x, y):
                yield (x, y)


def parse_input(input_str: str):
    part_numbers = []
    part_locations = set()
    gear_locations = set()
    for y, line in enumerate(input_str.splitlines()):
        num = []
        line += "."  # easily evaluate end of line
        for x, char in enumerate(line):
            location = (x, y)
            if char.isdigit():
                if not num:
                    num_start = location
                num.append(char)
            else:
                if num:
                    part_numbers.append({
                        "start": num_start,
                        "end": (num_start[0] + len(num) - 1, num_start[1]),
                        "num": int("".join(num))
                    })
                    num = []
            if is_part(char):
                part_locations.add(location)
                if is_gear(char):
                    gear_locations.add(location)
    return part_numbers, part_locations, gear_locations


def is_part(char):
    return char != "." and not char.isdigit()


def is_gear(char):
    return char == "*"


def main():
    print(f"{part_1(Path('input.txt').read_text())}")
    print(f"{part_2(Path('input.txt').read_text())}")


def part_1(input_str):
    answer = 0
    part_numbers, part_locations, _ = parse_input(input_str)
    for part_num in part_numbers:
        if any(location in part_locations for location in get_neighbours(part_num["start"], part_num["end"])):
            answer += part_num["num"]

    return answer


def part_2(input_str):
    answer = 0
    part_numbers, part_locations, gear_locations = parse_input(input_str)
    for gear_location in gear_locations:
        neighbours = []
        for part_num in part_numbers:
            if any(location == gear_location for location in get_neighbours(part_num["start"], part_num["end"])):
                neighbours.append(part_num["num"])
        if len(neighbours) == 2:
            answer += math.prod(neighbours)

    return answer


if __name__ == '__main__':
    main()
