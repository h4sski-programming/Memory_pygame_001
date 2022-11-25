import random

from settings import *


class Guess:
    def __init__(self, game) -> None:
        self.game = game
        self.pg = self.game.pg
        self.correct = []
        self.player = []
        self.add_correct()

    def add_correct(self):
        self.correct.append(random.choice([
            self.game.buttons['q'],
            self.game.buttons['w'],
            self.game.buttons['a'],
            self.game.buttons['s'],
        ]))

    def print_player(self):
        tmp = []
        for b in self.player:
            tmp.append(b.name)
        print(f'P {tmp}')

    def add_player(self, btn):
        self.player.append(btn)
        self.print_player()

    def next_level(self):
        if len(self.player) == len(self.correct):
            self.pg.time.wait(DELAY_TIME * 2)
            self.add_correct()
            self.player = []
            return True
        else:
            return False

    def check_player_correct(self, new_btn):
        new_btn_number = len(self.player)
        # print(f'{new_btn.name}')
        # print(f'{self.correct[new_btn_number].name}')
        if new_btn.name == self.correct[new_btn_number].name:
            self.add_player(new_btn)
            new_btn.activate()
            return True
        else:
            print('incorrect')
            return False
