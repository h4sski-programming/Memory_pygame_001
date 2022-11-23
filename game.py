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

        self.btn_q = Btn(self, name='q')
        self.btn_w = Btn(self, name='w')
        self.btn_a = Btn(self, name='a')
        self.btn_s = Btn(self, name='s')
        self.guess = Guess(self)

        self.new_game()

    def update(self):
        self.pg.display.flip()
        self.clock.tick(FPS)
        self.pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill(BLACK)
        self.btn_q.draw()
        self.btn_w.draw()
        self.btn_a.draw()
        self.btn_s.draw()

    def check_events(self):

        def deactive_all_btn(self):
            self.btn_q.deactivate()
            self.btn_w.deactivate()
            self.btn_a.deactivate()
            self.btn_s.deactivate()

        for event in self.pg.event.get():
            keys = self.pg.key.get_pressed()
            if keys[self.pg.K_ESCAPE] or keys[self.pg.K_o]:
                self.is_running = False
                # self.pg.quit()
                # sys.exit()

            if keys:
                deactive_all_btn(self)

            if self.pg.KEYDOWN:
                if keys[self.pg.K_q]:
                    self.btn_q.pressed()
                elif keys[self.pg.K_w]:
                    self.btn_w.pressed()
                elif keys[self.pg.K_a]:
                    self.btn_a.pressed()
                elif keys[self.pg.K_s]:
                    self.btn_s.pressed()

    def new_game(self):
        # pass
        self.update()
        self.draw()
        self.pg.time.delay(DELAY_TIME)
        self.guess.play_correct()

    def run(self):
        while self.is_running:
            self.check_events()
            self.update()
            self.draw()
