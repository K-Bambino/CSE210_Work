class Deck:
    """
    A collection of 52 cards with an unpulled deck and a discard pile.
        self.unpulled - all cards that have not been pulled yet
        self.discard - all pulled cards
        self.topcard - the most recently pulled card
    methods
        pull() - choose a random card from unpulled card, 
                    make self.topcard = that card, remove it from unpulled 
                    and add it to discard
        compare_cards() - pull a new card and compare the value of the old card to the value of the new card
    """
    def __init__(self):
        pass
    
    def pull(self):
        pass

    def compare_cards(self):
        pass

class Card:
    """
    A single card with a suit and a deck.
    attributes:
        self.suit
        self.number
    
    """
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def is_lower(self, card):
        pass

    def is_higher(self, card):
        pass

def main():
    pass

if __name__ == "__main__":
    main()
