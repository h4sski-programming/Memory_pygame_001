import sys

from settings import *
from button import Btn
# from sound import Sound
from guess import Guess


class Game:
    def __init__(self, main):
        self.m = main
        self.pg = main.pg
        self.screen = main.screen
        self.clock = main.clock
        self.is_running = True

        # btn_q = Btn(self, name='q'),
        # btn_w = Btn(self, name='w'),
        # btn_a = Btn(self, name='a'),
        # btn_s = Btn(self, name='s'),
        self.buttons = {
            'q': Btn(self, name='q'),
            'w': Btn(self, name='w'),
            'a': Btn(self, name='a'),
            's': Btn(self, name='s'),
        }
        self.guess = Guess(self)

        self.new_game()

    def update(self):
        self.pg.display.update()
        self.pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill(BLACK)
        for btn in self.buttons.values():
            btn.draw()

    def deactivate_buttons(self):
        for btn in self.buttons.values():
            if self.pg.time.get_ticks() - btn.activate_time >= BTN_DEACTIVATE_TIME:
                btn.deactivate()

    def check_events(self):
        self.deactivate_buttons()

        if self.guess.next_level():
            self.play_correct()

        for event in self.pg.event.get():
            keys = self.pg.key.get_pressed()

            if event.type == self.pg.QUIT:
                self.is_running = False
                self.m.home.is_running = False
            if keys[self.pg.K_ESCAPE]:
                self.is_running = False

            if event.type == self.pg.KEYDOWN:
                if keys[self.pg.K_q]:
                    self.guess.check_player_correct(self.buttons['q'])
                    # self.buttons['q'].pressed()
                elif keys[self.pg.K_w]:
                    self.guess.check_player_correct(self.buttons['w'])
                    # self.buttons['w'].pressed()
                elif keys[self.pg.K_a]:
                    self.guess.check_player_correct(self.buttons['a'])
                    # self.buttons['a'].pressed()
                elif keys[self.pg.K_s]:
                    self.guess.check_player_correct(self.buttons['s'])
                    # self.buttons['s'].pressed()

    def play_correct(self):
        tmp = []
        for correct_btn in self.guess.correct:
            self.deactivate_buttons()
            correct_btn.activate()
            self.draw()
            self.update()
            self.pg.time.wait(DELAY_TIME)
            tmp.append(correct_btn.name)
        print(tmp)

    def new_game(self):
        # pass
        self.clock.tick(FPS)
        self.play_correct()
        # self.pg.time.delay(DELAY_TIME)

    def run(self):
        while self.is_running:
            self.check_events()
            self.draw()
            self.update()
