from collections import defaultdict
from pathlib import Path


def parse_input(input_str: str):
    for line in input_str.splitlines():
        card, line = line.split(": ")
        card = int(card[5:])
        winning, have = line.split(" | ")
        winning = set(winning.split())
        have = set(have.split())
        yield card, winning, have


def main():
    print(f"{part_1(Path('input.txt').read_text())}")
    print(f"{part_2(Path('input.txt').read_text())}")


def part_1(input_str):
    answer = 0
    for _, winning, have in parse_input(input_str):
        if winning.intersection(have):
            answer += 2 ** (len(winning.intersection(have)) - 1)
    return answer


def part_2(input_str):
    duplicates = defaultdict(int)
    for card, winning, have in parse_input(input_str):
        matches = len(winning.intersection(have))
        for won_card in range(card + 1, card + matches + 1):
            duplicates[won_card] += (1 + duplicates[card])
    return card + sum(duplicates.values())


if __name__ == '__main__':
    main()
