'''Deck'''

class Deck(object):
    '''Deck class'''
    def __init__(self, cards):
        self.cards = cards

    def rank_of_card_at(self, index):
        '''Returns rank of card at an index position'''
        return self.cards[index].rank

    def high_ranking_cards(self):
        '''Returns all cards with rank over 10 in a deck'''
        return [card for card in self.cards if card.rank >= 11]

    def percent_high_ranking(self):
        '''Percent of cards in a deck with a rank more than 10'''
        return round(len(self.high_ranking_cards()) * 100 / len(self.cards), 2)

    def remove_card(self):
        ''' Removes the card in the 0 index position from the deck '''
        return self.cards.pop(0)

    def add_card(self, card):
        '''Add a card to the back of the deck'''
        self.cards.append(card)
