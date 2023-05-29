from CardGame import CardGame, Card
from card import Big2Card
import sys

sys.path.append("..")
from Big2.card_pattern import Single, Pair, Straight, FullHouse, CardPatternChain


card_pattern_chain = CardPatternChain()
card_pattern_chain.chain()


def test_pattern_chain():
    cards_single = [Big2Card(rank="9", suit="D")]
    cards_pair = [Big2Card(rank="9", suit="D"), Big2Card(rank="9", suit="H")]
    cards_straight = [Big2Card(rank="9", suit="D"), Big2Card(rank="10", suit="H"), Big2Card(rank="J", suit="C"), Big2Card(rank="Q", suit="S"), Big2Card(rank="K", suit="H")]
    cards_fullhouse = [Big2Card(rank="9", suit="D"), Big2Card(rank="9", suit="H"), Big2Card(rank="J", suit="C"), Big2Card(rank="J", suit="D"), Big2Card(rank="J", suit="H")]
    cards_invalid = [Big2Card(rank="9", suit="D"), Big2Card(rank="8", suit="H"), Big2Card(rank="J", suit="H")]
    assert isinstance(card_pattern_chain.single(cards=cards_single), Single)
    assert isinstance(card_pattern_chain.single(cards=cards_pair), Pair)
    assert isinstance(card_pattern_chain.single(cards=cards_straight), Straight)
    assert isinstance(card_pattern_chain.single(cards=cards_fullhouse), FullHouse)
    try:
        card_pattern_chain.single(cards=cards_invalid)
    except TypeError as e:
        assert e


def test_single_compare():
    cards_a = [Big2Card(rank="9", suit="D")]
    cards_b = [Big2Card(rank="10", suit="C")]
    single_a = card_pattern_chain.single(cards=cards_a)
    single_b = card_pattern_chain.single(cards=cards_b)
    single_a.cards
    single_b.cards
    assert not single_a.compare(single_b)
    assert single_b.compare(single_a)


def test_single
