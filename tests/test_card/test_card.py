'''Tests for card class'''
import pytest
from src.card import Card

@pytest.fixture
def card():
    '''Test fixture'''
    return Card('diamond', 'Queen', 12)

def test_attributes(card):
    ''' Tests that a card has attributes '''
    assert card.suit == 'diamond'
    assert card.value == 'Queen'
    assert card.rank == 12
