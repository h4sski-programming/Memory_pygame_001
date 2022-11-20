from settings import *


class Btn:
    def __init__(self, game, name):
        self.game = game
        self.name = name
        self.is_active = False
        self.pos = 0, 0
        self.color = BLUE
        self.initial_settings()

    def initial_settings(self):
        if self.name == 'w':
            self.pos = 1, 0
            self.color = RED
        elif self.name == 'a':
            self.pos = 0, 1
            self.color = GREEN
        elif self.name == 's':
            self.pos = 1, 1
            self.color = ORANGE

    def draw(self):
        if self.is_active:
            self.game.pg.draw.rect(self.game.screen, self.color,
                         (self.pos[0] * BTN_WIDTH, self.pos[1] * BTN_HEIGHT, BTN_WIDTH, BTN_HEIGHT))
        else:
            self.game.pg.draw.rect(self.game.screen, self.color + '4',
                         (self.pos[0] * BTN_WIDTH, self.pos[1] * BTN_HEIGHT, BTN_WIDTH, BTN_HEIGHT))

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False
