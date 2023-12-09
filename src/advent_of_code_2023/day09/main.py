from pathlib import Path


def parse_input(input_str: str):
    for line in input_str.splitlines():
        yield [int(v) for v in line.split()]


def main():
    print(f"Part 1: {part_1(Path('input.txt').read_text())}")
    print(f"Part 2: {part_2(Path('input.txt').read_text())}")


def part_1(input_str):
    answer = 0
    sequences = parse_input(input_str)
    for sequence in sequences:
        constants = []
        while True:
            constants.append(sequence[0])
            # calculate the differences between sequential values in the sequence
            differences = [j - i for i, j in zip(sequence[:-1], sequence[1:])]
            sequence = differences
            if len(set(sequence)) == 1:
                sequence.append(sequence[-1])
                break
        while constants:
            new_sequence = [constants.pop()]
            for value in sequence:
                new_sequence.append(new_sequence[-1] + value)
            sequence = new_sequence
        answer += sequence[-1]
    return answer


def part_2(input_str):
    answer = 0
    sequences = parse_input(input_str)
    for sequence in sequences:
        sequence = sequence[::-1]
        constants = []
        while True:
            constants.append(sequence[0])
            # calculate the differences between sequential values in the sequence
            differences = [j - i for i, j in zip(sequence[:-1], sequence[1:])]
            sequence = differences
            if len(set(sequence)) == 1:
                sequence.append(sequence[-1])
                break
        while constants:
            new_sequence = [constants.pop()]
            for value in sequence:
                new_sequence.append(new_sequence[-1] + value)
            sequence = new_sequence
        answer += sequence[-1]
    return answer


if __name__ == '__main__':
    main()
