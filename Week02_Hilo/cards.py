import random

class Deck:
    """
    A collection of 52 cards with an unpulled deck and a discard pile.
        self.unpulled - all cards that have not been pulled yet
        self.discard - all pulled cards
        self.top_card - the most recently pulled card
    methods
        pull() - choose a random card from unpulled card, 
                    make self.top_card = that card, remove it from unpulled 
                    and add it to discard
        compare_cards() - pull a new card and compare the value of the old card to the value of the new card
    """
    def __init__(self):
        self.unpulled =[]
        self.discard = []
        self.top_card = None
        numbers = range(1,14)
        suits = ["Spades","Clubs","Diamonds","Hearts"]
        for number in numbers:
            for suit in suits:
               self.unpulled.append(Card(suit,number))
        
        

    def pull(self):
        self.top_card = self.unpulled.pop(random.randrange(0,len(self.unpulled)))
        self.discard.append(self.top_card)
        if len(self.unpulled)==0:
            self.unpulled=self.discard
            self.discard = []
        

    def compare_cards(self,game_mode):
        old_card = self.top_card
        self.pull()
        if self.top_card>old_card and game_mode=='h':
            return 100
        elif self.top_card<old_card and game_mode=='l':
            return 100
        else:
            return -75


        

class Card:
    """
    A single card with a suit and a number.
    attributes:
        self.suit
        self.number
    
    """
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __lt__(self,other_card):
        return self.number<other_card.number

    def __gt__(self, other_card):
        return self.number>other_card.number
        
    def __str__(self):
        if self.number != 1 and self.number<11:
            number = self.number
        elif self.number ==1:
            number = "Ace(1)"
        elif self.number == 11:
            number = "Jack(11)"
        elif self.number ==12:
            number = "Queen(12)"
        elif self.number ==13:
            number = "King(13)"
        else:
            number = "err"
        return f'{number} of {self.suit}'
        

def main():
    Deck.__init__()
    pass

if __name__ == "__main__":
    main()