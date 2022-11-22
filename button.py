from settings import *


class Btn:
    def __init__(self, game, name):
        self.game = game
        self.name = name
        self.is_active = False
        self.pos = 0, 0
        self.color = BLUE
        self.initial_settings()
        self.font = self.game.pg.font.SysFont(None, BTN_TAG_FONT_SIZE)
        self.tag = self.font.render(self.name, True, BTN_TAG_COLOR)

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

        self.game.screen.blit(self.tag, (self.pos[0] * BTN_WIDTH + BTN_NAME_TAG_OFFSET_X,
                                         self.pos[1] * BTN_HEIGHT + BTN_NAME_TAG_OFFSET_Y))

    def press(self):
        self.activate()
        self.game.guess.check(self.name)
        self.deactivate()

    def activate(self):
        self.is_active = True
        self.draw()
        if self.name == 'q':
            self.game.sound.play_q()
        elif self.name == 'w':
            self.game.sound.play_w()
        elif self.name == 'a':
            self.game.sound.play_a()
        elif self.name == 's':
            self.game.sound.play_s()

    def deactivate(self):
        self.is_active = False
