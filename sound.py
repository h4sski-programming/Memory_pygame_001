

class Sound:
    def __init__(self, game):
        self.game = game
        self.game.pg.mixer.init()

        self.path = 'sound/'
        self.btn_q = self.game.pg.mixer.Sound(self.path + 'q.wav')
        self.btn_w = self.game.pg.mixer.Sound(self.path + 'w.wav')
        self.btn_a = self.game.pg.mixer.Sound(self.path + 'a.wav')
        self.btn_s = self.game.pg.mixer.Sound(self.path + 's.wav')

    def play_q(self):
        self.btn_q.play()
        self.btn_q.fadeout(700)

    def play_w(self):
        self.btn_w.play()
        self.btn_w.fadeout(700)

    def play_a(self):
        self.btn_a.play()
        self.btn_a.fadeout(700)

    def play_s(self):
        self.btn_s.play()
        self.btn_s.fadeout(700)

