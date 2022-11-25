from settings import *


class Sound:
    path = 'sound/'

    def __init__(self, game, btn_name) -> None:
        self.game = game
        self.mixer = self.game.pg.mixer
        self.mixer.init()
        self.file = self.mixer.Sound(self.path + f'{btn_name}.wav')

    def play_sound(self):
        self.file.play()
        self.file.fadeout(BTN_DEACTIVATE_TIME)
