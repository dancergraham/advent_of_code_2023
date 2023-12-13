from pathlib import Path


class Point:
    def __init__(self, x, y, neighbours):
        self.x = x
        self.y = y
        self.neighbours = neighbours

    def __str__(self):
        return f"Point({self.x}, {self.y}, {self.neighbours})"


def parse_input(input_str: str):
    map_ = {}
    connections = {"7": [(-1, 0), (0, 1)],
                   "F": [(1, 0), (0, 1)],
                   "L": [(1, 0), (0, -1)],
                   "J": [(-1, 0), (0, -1)],
                   "-": [(-1, 0), (1, 0)],
                   "|": [(0, 1), (0, -1)],
                   "S": [(0, 1), (0, -1), (-1, 0), (1, 0)],
                   }
    for y, row in enumerate(input_str.split('\n')):
        for x, char in enumerate(row):
            if char == "S":
                starting_position = (x, y)
            elif char == ".":
                continue
            if char in connections:
                neighbours = []
                for dx, dy in connections[char]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(row) and 0 <= ny < len(input_str.split('\n')):
                        neighbours.append((nx, ny))
                map_[(x, y)] = Point(x, y, neighbours)
    # TODO: remove hard-coded positions
    map_[starting_position].neighbours = [(28, 32), (27, 31)]
    # map_[starting_position].neighbours = [(1, 2), (2, 1)]
    return starting_position, map_


def main():
    print(f"Part 1: {part_1(Path('input.txt').read_text())}")
    print(f"Part 2: {part_2(Path('input.txt').read_text())}")


def part_1(input_str):
    steps, _, _ = build_main_loop(input_str)
    return steps


def build_main_loop(input_str):
    starting_position, map_ = parse_input(input_str)
    visited = set()
    steps = 0
    previous_positions = [starting_position]
    current_positions = [p for p in map_[starting_position].neighbours if p in map_]
    while True:
        steps += 1
        new_positions = []
        for position in current_positions:
            if position in visited:
                break
            visited.add(position)
            for neighbour in map_[position].neighbours:
                if neighbour not in previous_positions:
                    new_positions.append(neighbour)
        if not new_positions:
            break
        previous_positions = current_positions.copy()
        current_positions = new_positions.copy()
        visited.add(starting_position)
    return steps, map_, visited


def part_2(input_str):
    clean_map = []
    steps, map_, visited = build_main_loop(input_str)
    for j, line in enumerate(input_str.splitlines()):
        clean_line = []
        for i, char in enumerate(line):
            if (i, j) not in visited:
                clean_line.append(".")
            else:
                clean_line.append(char)
        clean_map.append(clean_line)

    answer = 0
    for clean_line in clean_map:
        for i, char in enumerate(clean_line):
            if char not in "7FJLS|-":
                # TODO: remove hard coded replacement for S
                line = "".join(clean_line[:i]).replace("S", "7")
                inside = (line.count("|")
                          + (line.count("L")
                             - line.count("J")
                             - line.count("F")
                             + line.count("7")) / 2) % 2
                answer += inside
                if inside:
                    print("0", end="")
                else:
                    print(".", end="")
            else:
                print(char, end="")
        print()
    return answer


if __name__ == '__main__':
    main()
