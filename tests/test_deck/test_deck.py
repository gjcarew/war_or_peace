import pytest
from src.card import Card
from src.deck import Deck

@pytest.fixture
def card1():
    '''Returns queen of diamonds'''
    return Card('diamond', 'Queen', 12)


@pytest.fixture
def card2():
    '''3 of spades'''
    return Card('spade', '3', 3)

@pytest.fixture
def card3():
    '''Ace of hearts'''
    return Card('heart', 'Ace', 14)

@pytest.fixture
def deck(card1, card2, card3):
    '''A deck with  three cards'''
    return Deck([card1, card2, card3])

def test_cards(deck, card1, card2, card3):
    ''' Tests that a card has attributes '''
    assert deck.cards == [card1, card2, card3]

def test_rank_of_card_at(deck):
    assert deck.rank_of_card_at(0) == 12
    assert deck.rank_of_card_at(2) == 14

def test_high_ranking_cards(deck, card1, card3):
    assert deck.high_ranking_cards() == [card1, card3]

def test_percent_high_ranking(deck):
    assert deck.percent_high_ranking == 66.67

def test_remove_card(deck, card1, card2, card3):
    assert deck.remove_card == card1
    assert deck.cards == [card2, card3]

@pytest.fixture
def card4():
    return Card('club', '5', 5)

def test_add_card(deck, card1, card2, card3, card4):
    deck.add_card(card4)
    assert deck.cards == [card1, card2, card3, card4]

    