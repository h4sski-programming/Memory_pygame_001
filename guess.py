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
            self.game.btn_q,
            self.game.btn_w,
            self.game.btn_a,
            self.game.btn_s,
        ]))

    def print_player(self):
        tmp_str = []
        for b in self.player:
            tmp_str.append(b.name)
        print(f'P {tmp_str}')

    def add_player(self, btn):
        self.player.append(btn)
        self.print_player()

    def play_correct(self):
        for b in self.correct:
            b.activate()
            print(f'C {b.name}')
            self.game.pg.time.delay(DELAY_TIME)
            b.deactivate()

    '''
    def __init__(self, game):
        self.game = game
        self.correct = []
        self.player = []

        self.add_correct()

    def add_correct(self):
        self.correct.append(random.choice(['q', 'w', 'a', 's']))
        print(f'C {self.correct}')

    def add_player(self, g):
        self.player.append(g)
        print(f'P {self.player}')

    def play_correct(self):
        for i, char in enumerate(self.correct):
            if char == 'q':
                self.game.btn_q.activate()
                # self.game.pg.time.delay(DELAY_TIME)
                # self.game.btn_q.deactivate()
            elif char == 'w':
                self.game.btn_w.activate()
                # self.game.pg.time.delay(DELAY_TIME)
                # self.game.btn_w.deactivate()
            elif char == 'a':
                self.game.btn_a.activate()
                # self.game.pg.time.delay(DELAY_TIME)
                # self.game.btn_a.deactivate()
            elif char == 's':
                self.game.btn_s.activate()
                # self.game.pg.time.delay(DELAY_TIME)
                # self.game.btn_s.deactivate()

    def check(self, btn):
        self.add_player(btn)

        for i, p in enumerate(self.player):
            # not using 'p' since 'self.player[i]' is more readable
            if not self.correct[i] == self.player[i]:
                print(f'incorrect')
                return False

        self.next_level()
        return True

    def next_level(self):
        if len(self.player) == len(self.correct):
            self.game.pg.time.delay(DELAY_TIME * 2)
            self.add_correct()
            self.player = []
            self.play_correct()'''
