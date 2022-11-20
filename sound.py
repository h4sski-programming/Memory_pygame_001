

class Sound:
    def __init__(self, game):
        self.game = game
        self.game.pg.mixer.init()

        self.path = 'sound/'
        self.btn_q = self.game.pg.mixer.Sound(self.path + 'q.mp3')
