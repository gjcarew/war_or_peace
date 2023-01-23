import pytest
from card import Card

@pytest.fixture
def card():
    #Returns an queen of diamonds
    return Card('diamond', 'Queen', 12)

def test_attributes(card):
    assert card.suit == 'diamond'
    assert card.value == 'Queen'
    assert card.rank == 12

