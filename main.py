import sys
import pygame as pg

from home import Home
from game import Game
from settings import *


class Main:
    def __init__(self) -> None:
        self.pg = pg
        self.pg.init()
        self.screen = pg.display.set_mode(RESOLUTION)
        self.clock = pg.time.Clock()

    def run(self):
        self.home = Home(self)
        while self.home.is_running:
            self.home.run()
            if self.home.start_game:
                game = Game(self)
                game.run()
                self.home.start_game = False


if __name__ == '__main__':
    main = Main()
    main.run()

    main.pg.quit()
    sys.exit()
