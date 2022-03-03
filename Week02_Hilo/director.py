import cards.py

class director:
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
        self.deck = ""
        self.score = ""
        self.game_mode = True

    def run(self):
        while self.game_mode != quit:
            director.draw_scoreboard(self,score,turn)
            director.get_choice(self)
        pass

    def draw_scoreboard(self,score,turn):
        print(f'-----HiLo-----')
        print(f'score     turn')
        print(f'{score:5}{turn:9}')
        print(f'--------------')
        pass



    def get_choice(self):
        pass


director.draw_scoreboard(0,150,3)