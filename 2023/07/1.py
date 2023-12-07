from collections import Counter
import numpy as np

# Hands:
# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456


hand_ranks = {
        "High Card": 0,
        "One Pair": 1,
        "Two Pair": 2,
        "Three of a Kind": 3,
        "Full House": 4,
        "Four of a Kind": 5,
        "Five of a Kind": 6,
    }


def get_hand_rank(hand):
    counts = Counter(hand)
    if len(counts) == 1:
        rank = hand_ranks["Five of a Kind"]
    elif len(counts) == 2:
        if 4 in counts.values():
            rank = hand_ranks["Four of a Kind"]
        else:
            rank = hand_ranks["Full House"]
    elif len(counts) == 3:
        if 3 in counts.values():
            rank = hand_ranks["Three of a Kind"]
        else:
            rank = hand_ranks["Two Pair"]
    elif len(counts) == 4:
        rank = hand_ranks["One Pair"]
    else:
        rank = hand_ranks["High Card"]

    return (rank, hand)


if __name__ == "__main__":
    bids = {}

    # to have easier sorting we will convert 'TJQKA' to 'ABCDE'
    translation = str.maketrans('TJQKA', 'ABCDE')
    with open("07/input.txt") as f:
        for line in f.readlines():
            hand, bid = line.split()
            bids[hand.translate(translation)] = int(bid)

    ordered_hands = sorted(bids, key=get_hand_rank)

    print(np.sum([(ind + 1) * bids[hand] for ind, hand in enumerate(ordered_hands)]))
    