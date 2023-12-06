import math
from pathlib import Path


class Race:
    def __init__(self, time, distance):
        self.time = time
        self.distance = distance


def parse_input(input_str: str):
    times, distances = input_str.splitlines()
    times = [int(time) for time in list(times.split())[1:]]
    distances = [int(distance) for distance in list(distances.split())[1:]]
    return [Race(time, distance) for time, distance in zip(times, distances)]


def parse_input_2(input_str: str):
    times, distances = input_str.splitlines()
    time = int("".join(c for c in times if c.isdigit()))
    distance = int("".join(c for c in distances if c.isdigit()))
    return Race(time, distance)


def main():
    print(f"{part_1(Path('input.txt').read_text())}")
    print(f"{part_2(Path('input.txt').read_text())}")


def part_1(input_str):
    ways_to_win = []
    races = parse_input(input_str)
    for race in races:
        wins = 0
        for button_duration in range(1, race.time):
            if button_duration * (race.time - button_duration) > race.distance:
                wins += 1
        if wins:
            ways_to_win.append(wins)
    return math.prod(ways_to_win)


def part_2(input_str):
    race = parse_input_2(input_str)
    wins = 0
    for button_duration in range(1, race.time):
        if button_duration * (race.time - button_duration) > race.distance:
            wins += 1
    return wins


if __name__ == '__main__':
    main()
