from cards import Deck, Card

class Director:
    """
    The direcor that enables the start, end, and turn order of Hilo.
    attributes
        self.deck - a deck of cards
        self.points - an integer point value
        self.keep_playing - a boolean term representing whether or not to host another turn
    methods
        __init__() - initialize instance
        run() - run game loop
        draw_game() - print game board each turn
        get_choice() - get and validate input from user
    """
    def __init__(self):
        self.deck = Deck()
        self.score = 300
        self.game_mode = ""
        self.turn = 0

    def run(self):
    
        self.deck.pull()
        while self.game_mode != "q":
            self.turn += 1
            self.draw_game()
            self.game_mode = self.get_choice()
            if self.game_mode != "q":
                self.score += self.deck.compare_cards(self.game_mode)
            if self.score <= 0:
                self.score = 0
                self.game_mode = "q"
            
        self.draw_game()

        

    def draw_game(self):
        print()
        print(f'-----HiLo-----')
        print(f'score     turn')
        print(f'{self.score:5}{self.turn:9}')
        print(f'--------------')
        print(f'Card: {self.deck.top_card}')
        print()


    def get_choice(self):

        valid_space = False

        # This loop will repeat until the user picks a valid spot.
        while valid_space != True:

            player_move = input("Higher, lower or quit? [h/l/q] ")
            
            if player_move in ["h", "l", "q"]:
                valid_space = True
            else:
                print(f"{player_move} is not a valid option. Please try again.")
        
        return player_move

def main():
    director = Director()
    director.run()

if __name__ == "__main__":
    main()