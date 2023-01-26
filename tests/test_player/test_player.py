import pytest
from src.player import Player
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

@pytest.fixture
def player(deck):
    '''A new player'''
    return Player('Clarisa', deck)

def test_attributes(player, deck):
    ''' A player has attributes '''
    assert player.name == 'Clarisa'
    assert player.deck == deck

def test_has_lost(player):
    ''' A player has lost when their deck is empty '''
    assert player.has_lost() is False
    player.deck.remove_card()
    assert player.has_lost() is False
    player.deck.remove_card()
    player.deck.remove_card()
    assert player.has_lost() is True
    assert player.deck.cards == []

