import math
from collections import defaultdict
from itertools import cycle
from pathlib import Path


def parse_input(input_str: str):
    instructions, network = input_str.split("\n\n")
    mapping = defaultdict(dict)
    for line in network.splitlines():
        k, v = line.split(" = ")
        mapping[k]["L"], mapping[k]["R"] = v[1:-1].split(", ")

    return instructions, mapping


def main():
    print(f"Part 1: {part_1(Path('input.txt').read_text())}")
    print(f"Part 2: {part_2(Path('input.txt').read_text())}")


def part_1(input_str):
    instructions, mapping = parse_input(input_str)
    position = "AAA"
    for step, c in enumerate(cycle(instructions), 1):
        position = mapping[position][c]
        if position == "ZZZ":
            break
    return step


def part_2(input_str):
    instructions, mapping = parse_input(input_str)
    positions = [position for position in mapping.keys() if position.endswith("A")]
    zs = defaultdict(list)
    for step, c in enumerate(cycle(instructions), 1):
        for i, position in enumerate(positions):
            positions[i] = mapping[position][c]
        if all(position.endswith("Z") for position in positions):
            break
        for j, position in enumerate(positions):
            if position.endswith("Z"):
                zs[j].append(step)
        if len(zs) == len(positions):
            break
    return math.lcm(*[v[0] for v in zs.values()])


if __name__ == '__main__':
    main()
