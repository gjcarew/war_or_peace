'''Deck class'''
class Deck(object):
    '''Deck class'''
    def __init__(self, cards):
        self.cards = cards
    
    def rank_of_card_at(self, index):
        return self.cards[index].rank

    def high_ranking_cards(self):
        import ipdb; ipdb.set_trace()
        high_ranking = []
        for card in self.cards:
            if card.rank > 10:
                high_ranking.append(card)
        return high_ranking

