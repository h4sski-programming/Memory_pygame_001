import sys
import pygame as pg

from settings import *
from button import Btn
from sound import Sound
from guess import Guess


class Game:
    def __init__(self):
        self.pg = pg
        self.pg.init()
        self.screen = self.pg.display.set_mode(RESOLUTION)
        self.clock = self.pg.time.Clock()
        self.sound = Sound(self)

        self.btn_q = Btn(self, name='q')
        self.btn_w = Btn(self, name='w')
        self.btn_a = Btn(self, name='a')
        self.btn_s = Btn(self, name='s')
        self.guess = Guess(self)

        self.is_running = True
        self.new_game()

    def new_game(self):
        self.update()
        self.draw()
        self.pg.time.delay(DELAY_TIME)
        self.guess.play_correct()

    def update(self):
        self.pg.display.flip()
        self.clock.tick(FPS)
        self.pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('black')
        self.btn_q.draw()
        self.btn_w.draw()
        self.btn_a.draw()
        self.btn_s.draw()

    def check_events(self):
        for event in self.pg.event.get():
            if event.type == self.pg.QUIT or (event.type == self.pg.KEYDOWN and event.key == self.pg.K_ESCAPE):
                self.is_running = False
                self.pg.quit()
                sys.exit()

            if event.type == self.pg.KEYDOWN:
                keys = self.pg.key.get_pressed()
                if keys[self.pg.K_q]:
                    if self.guess.check(self.btn_q.name):
                        self.btn_q.activate()
                        # self.pg.time.delay(DELAY_TIME)
                elif keys[self.pg.K_w]:
                    if self.guess.check(self.btn_w.name):
                        self.btn_w.activate()
                    # self.btn_w.press()
                elif keys[self.pg.K_a]:
                    if self.guess.check(self.btn_a.name):
                        self.btn_a.activate()
                    # self.btn_a.press()
                elif keys[self.pg.K_s]:
                    if self.guess.check(self.btn_s.name):
                        self.btn_s.activate()
                    # self.btn_s.press()

    def run(self):
        while self.is_running:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
