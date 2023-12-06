from pathlib import Path


class RangeMap:
    def __init__(self, to, from_, len_):
        self.to = to
        self.from_ = from_
        self.len_ = len_

    def __getitem__(self, item):
        if not self.from_ <= item < self.from_ + self.len_:
            return item
        return self.to + item - self.from_

    def __lt__(self, other):
        return self.from_ < other.from_


class MultiRangeMap:
    def __init__(self, rangemaps):
        self.rangemaps = sorted(rangemaps)

    def __getitem__(self, item):
        for rangemap in self.rangemaps:
            if rangemap.from_ <= item < rangemap.from_ + rangemap.len_:
                return rangemap[item]
        return item


def parse_input(input_str: str):
    lines = iter(input_str.splitlines())
    seeds = next(lines)[7:].split()
    yield [int(seed) for seed in seeds]
    range_maps = None
    for line in lines:
        if not line:
            continue
        if line.endswith("map:"):
            if range_maps is not None:
                yield MultiRangeMap(range_maps)
            range_maps = []
            continue
        range_maps.append(RangeMap(*[int(x) for x in line.split()]))
    yield MultiRangeMap(range_maps)


def main():
    print(f"{part_1(Path('input.txt').read_text())}")
    print(f"{part_2(Path('input.txt').read_text())}")


def part_1(input_str):
    inputs = parse_input(input_str)
    seeds = next(inputs)
    for mapping in inputs:
        for i, seed in enumerate(seeds):
            seeds[i] = mapping[seed]
    return min(seeds)


def part_2(input_str):
    inputs = parse_input(input_str)
    seeds = list(next(inputs))
    range_starts = seeds[::2]
    range_lengths = seeds[1::2]
    answers = []
    mappings = list(inputs)
    for range_start, range_length in zip(range_starts, range_lengths):
        seeds = list(range(range_start, range_start + range_length))
        for mapping in mappings:
            for i, seed in enumerate(seeds):
                seeds[i] = mapping[seed]
        answers.append(min(seeds))
        print(answers)
    return min(answers)


if __name__ == '__main__':
    main()
