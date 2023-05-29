from card import Big2Card
import sys

sys.path.append("..")
from Big2.card_pattern import Single, Pair, Straight, FullHouse, CardPatternHandler


card_pattern_handler = CardPatternHandler()
card_pattern_handler.chain()


def test_pattern_chain():
    cards_single = [Big2Card(rank="9", suit="D")]
    cards_pair = [Big2Card(rank="9", suit="D"), Big2Card(rank="9", suit="H")]
    cards_straight = [
        Big2Card(rank="9", suit="D"),
        Big2Card(rank="10", suit="H"),
        Big2Card(rank="J", suit="C"),
        Big2Card(rank="Q", suit="S"),
        Big2Card(rank="K", suit="H"),
    ]
    cards_fullhouse = [
        Big2Card(rank="9", suit="D"),
        Big2Card(rank="9", suit="H"),
        Big2Card(rank="J", suit="C"),
        Big2Card(rank="J", suit="D"),
        Big2Card(rank="J", suit="H"),
    ]
    cards_invalid = [
        Big2Card(rank="9", suit="D"),
        Big2Card(rank="8", suit="H"),
        Big2Card(rank="J", suit="H"),
    ]
    assert isinstance(card_pattern_handler.single(cards=cards_single), Single)
    assert isinstance(card_pattern_handler.single(cards=cards_pair), Pair)
    assert isinstance(card_pattern_handler.single(cards=cards_straight), Straight)
    assert isinstance(card_pattern_handler.single(cards=cards_fullhouse), FullHouse)
    try:
        card_pattern_handler.single(cards=cards_invalid)
    except TypeError as e:
        assert e


card_pattern_handler_a = CardPatternHandler()
card_pattern_handler_a.chain()
card_pattern_handler_b = CardPatternHandler()
card_pattern_handler_b.chain()


def test_single_compare():
    cards_a = [Big2Card(rank="9", suit="D")]
    cards_b = [Big2Card(rank="10", suit="C")]
    single_b = card_pattern_handler_a.single(cards=cards_b)
    single_a = card_pattern_handler_b.single(cards=cards_a)
    single_a.cards
    single_b.cards
    assert not single_a.compare(single_b)
    assert single_b.compare(single_a)


def test_pair_compare():
    cards_a = [Big2Card(rank="9", suit="D"), Big2Card(rank="9", suit="H")]
    cards_b = [Big2Card(rank="9", suit="C"), Big2Card(rank="9", suit="S")]
    single_b = card_pattern_handler_a.single(cards=cards_b)
    single_a = card_pattern_handler_b.single(cards=cards_a)
    single_a.cards
    single_b.cards
    assert not single_a.compare(single_b)
    assert single_b.compare(single_a)


def test_straight_compare():
    cards_a = [
        Big2Card(rank="9", suit="C"),
        Big2Card(rank="10", suit="S"),
        Big2Card(rank="J", suit="H"),
        Big2Card(rank="Q", suit="D"),
        Big2Card(rank="K", suit="D"),
    ]
    cards_b = [
        Big2Card(rank="9", suit="D"),
        Big2Card(rank="10", suit="C"),
        Big2Card(rank="J", suit="D"),
        Big2Card(rank="Q", suit="H"),
        Big2Card(rank="K", suit="S"),
    ]
    single_b = card_pattern_handler_a.single(cards=cards_b)
    single_a = card_pattern_handler_b.single(cards=cards_a)
    single_a.cards
    single_b.cards
    assert not single_a.compare(single_b)
    assert single_b.compare(single_a)


def test_fullhouse_compare():
    cards_a = [
        Big2Card(rank="A", suit="C"),
        Big2Card(rank="A", suit="S"),
        Big2Card(rank="K", suit="H"),
        Big2Card(rank="K", suit="D"),
        Big2Card(rank="K", suit="S"),
    ]
    cards_b = [
        Big2Card(rank="A", suit="D"),
        Big2Card(rank="A", suit="H"),
        Big2Card(rank="2", suit="D"),
        Big2Card(rank="2", suit="H"),
        Big2Card(rank="2", suit="S"),
    ]
    single_b = card_pattern_handler_a.single(cards=cards_b)
    single_a = card_pattern_handler_b.single(cards=cards_a)
    single_a.cards
    single_b.cards
    assert not single_a.compare(single_b)
    assert single_b.compare(single_a)
