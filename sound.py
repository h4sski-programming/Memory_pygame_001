from settings import *
'''
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
'''


class Sound2:
    path = 'sound/'

    def __init__(self, game, btn_name) -> None:
        self.game = game
        self.mixer = self.game.pg.mixer
        self.mixer.init()
        self.file = self.mixer.Sound(self.path + f'{btn_name}.wav')

    def play_sound(self):
        self.file.play()
        self.file.fadeout(BTN_DEACTIVATE_TIME)
