from collections import Counter
from enum import Enum
from pathlib import Path


class HandType(Enum):
    HIGHCARD = 1
    ONEPAIR = 2
    TWOPAIR = 3
    THREEOFAKIND = 4
    FULLHOUSE = 5
    FOUROFAKIND = 6
    FIVEOFAKIND = 7

    def __lt__(self, other):
        return self.value < other.value


def rank(card: str):
    ordering = "23456789TJQKA"
    return ordering.find(card)


def rank_2(card: str):
    ordering = "J23456789TQKA"
    return ordering.find(card)


class Hand:
    def __init__(self, cards, bid):
        self.cards = list(cards)
        self.ranks = [rank(card) for card in cards]
        self.ranks_2 = [rank_2(card) for card in cards]
        self.bid = int(bid)
        self.type_ = self.get_type(cards)
        self.type_2 = self.get_type_part_2(cards)

    def __lt__(self, other):
        return (self.type_.value, self.ranks) < (other.type_.value, other.ranks)

    def _lt2(self, other):
        return (self.type_2.value, self.ranks_2) < (other.type_2.value, other.ranks_2)

    def __str__(self):
        return f"Hand({''.join(self.cards)}, {self.bid}, {self.type_})"

    def __repr__(self):
        return f"Hand({''.join(self.cards)}, {self.bid}, {self.type_})"

    def get_type_part_2(self, cards: str):
        jokers = cards.count("J")
        card_counter = Counter(cards.replace("J", ""))
        if card_counter:
            most_common_card = card_counter.most_common(1)[0][0]
            cards = cards.replace("J", most_common_card, jokers)
        return self.get_type(cards=cards)

    def get_type(self, cards: str):
        # check if the hand is valid
        if len(cards) != 5:
            raise ValueError("A hand must consist of 5 cards")

        freq = Counter(cards)
        values = sorted(freq.values(), reverse=True)

        if values == [5]:  # five of a kind
            return HandType.FIVEOFAKIND
        elif values == [4, 1]:  # four of a kind
            return HandType.FOUROFAKIND
        elif values == [3, 2]:  # full house
            return HandType.FULLHOUSE
        elif values == [3, 1, 1]:  # three of a kind
            return HandType.THREEOFAKIND
        elif values == [2, 2, 1]:  # two pair
            return HandType.TWOPAIR
        elif values == [2, 1, 1, 1]:  # one pair
            return HandType.ONEPAIR
        elif values == [1, 1, 1, 1, 1]:  # high card
            return HandType.HIGHCARD
        else:  # invalid hand
            raise ValueError("Invalid hand")


def parse_input(input_str: str):
    return [Hand(*line.split()) for line in input_str.splitlines()]


def main():
    print(f"Part 1: {part_1(Path('input.txt').read_text())}")
    print(f"Part 2: {part_2(Path('input.txt').read_text())}")


def part_1(input_str):
    hands = parse_input(input_str)
    hands = sorted(hands)
    return sum(i * hand.bid for i, hand in enumerate(hands, 1))


def part_2(input_str):
    Hand.__lt__ = Hand._lt2  # Monkey patch 🐒
    hands = sorted(parse_input(input_str))
    return sum(i * hand.bid for i, hand in enumerate(hands, 1))


if __name__ == '__main__':
    main()
