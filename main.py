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
        home = Home(self)
        while home.is_running:
            home.run()
            if home.start_game:
                game = Game(self)
                game.run()
                home.start_game = False


if __name__ == '__main__':
    main = Main()
    main.run()

    main.pg.quit()
    sys.exit()
