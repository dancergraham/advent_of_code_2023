from pathlib import Path


def parse_input(input_str: str):
    return input_str


def main():
    print(f"{part_1(Path('input.txt').read_text())}")
    print(f"{part_2(Path('input.txt').read_text())}")


def part_1(input_str):
    answer = 0
    for line in input_str.splitlines():
        game, line = line.split(": ")
        game = int(game[5:])
        possible = True
        for grab in line.split("; "):
            for cube in grab.split(", "):
                number, color = cube.split(" ")
                if int(number) > {"red": 12, "green": 13, "blue": 14}[color]:
                    possible = False
        if possible:
            answer += game
    return answer


def part_2(input_str):
    answer = 0
    for line in input_str.splitlines():
        game, line = line.split(": ")
        numbers = {"red": 0, "green": 0, "blue": 0}
        for grab in line.split("; "):
            for cube in grab.split(", "):
                number, color = cube.split(" ")
                numbers[color] = max(int(number), numbers[color])
        answer += numbers["red"] * numbers["green"] * numbers["blue"]
    return answer


if __name__ == '__main__':
    main()
