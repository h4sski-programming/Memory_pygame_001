import sys

import pygame as pg
from pygame import mixer

from button import Btn
from settings import *
from sound import Sound


class Game:
    def __init__(self):
        self.pg = pg
        self.pg.init()
        self.screen = self.pg.display.set_mode(RESOLUTION)
        self.clock = self.pg.time.Clock()
        self.sound = Sound(self)

        self.is_running = True
        self.new_game()

    def new_game(self):
        # pass
        self.btn_q = Btn(self, name='q')
        self.btn_w = Btn(self, name='w')
        self.btn_a = Btn(self, name='a')
        self.btn_s = Btn(self, name='s')

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
                    self.btn_q.pressed()
                    self.sound.btn_q.play()

    def run(self):
        while self.is_running:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
