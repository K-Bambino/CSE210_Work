from pickle import TRUE


class director:
    """
    The director that enables the start, end, and turn order of Hilo.
    attributes
        self.deck - a deck of cards
        self.points - an integer point value
        self.keep_playing - a boolean term representing whether or not to host another turn
    methods
        self.start_game
        self.host_turn
        self.draw_game_board
        self.ask_player
        self.compare_cards
        self.should_continue_game
    """
    def __init__(self):
        self.deck = ""
        self.points = ""
        self.keep_playing = TRUE

    def start_game(self):
        pass