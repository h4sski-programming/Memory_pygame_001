from settings import *
from sound import Sound2


class Btn:
    def __init__(self, game, name) -> None:
        self.game = game
        self.name = name
        self.is_active = False
        self.font = self.game.pg.font.SysFont(None, BTN_TAG_FONT_SIZE)
        self.tag = self.font.render(self.name, True, BTN_TAG_COLOR)
        self.tag.set_alpha(BTN_TAG_COLOR_ALPHA)

        self.init_settup()
        self.color_darker = self.color + '4'

    def init_settup(self):
        if self.name == 'q':
            self.position = 0, 0
            self.sound = Sound2(self.game, self.name)
            self.color = BLUE
        elif self.name == 'w':
            self.position = BTN_WIDTH, 0
            self.sound = Sound2(self.game, self.name)
            self.color = RED
        elif self.name == 'a':
            self.position = 0, BTN_HEIGHT
            self.sound = Sound2(self.game, self.name)
            self.color = GREEN
        elif self.name == 's':
            self.position = BTN_WIDTH, BTN_HEIGHT
            self.sound = Sound2(self.game, self.name)
            self.color = ORANGE

    def draw(self):
        if not self.is_active:
            self.game.pg.draw.rect(self.game.screen, self.color_darker,
                                   (self.position[0], self.position[1], BTN_WIDTH, BTN_HEIGHT))
        else:
            self.game.pg.draw.rect(self.game.screen, self.color,
                                   (self.position[0], self.position[1], BTN_WIDTH, BTN_HEIGHT))

        self.game.screen.blit(self.tag, (self.position[0] + BTN_NAME_TAG_OFFSET_X,
                                         self.position[1] + BTN_NAME_TAG_OFFSET_Y))

    def activate(self):
        self.is_active = True
        self.sound.play_sound()

    def deactivate(self):
        self.is_active = False
    '''
    def __init__(self, game, name):
        self.game = game
        self.name = name
        self.is_active = False
        self.pos = 0, 0
        self.color = BLUE
        self.initial_settings()
        self.draw_color = self.color + '4'

        self.font = self.game.pg.font.SysFont(None, BTN_TAG_FONT_SIZE)
        self.tag = self.font.render(self.name, True, BTN_TAG_COLOR)

    def initial_settings(self):
        if self.name == 'w':
            self.pos = BTN_WIDTH, 0
            self.color = RED
        elif self.name == 'a':
            self.pos = 0, BTN_HEIGHT
            self.color = GREEN
        elif self.name == 's':
            self.pos = BTN_WIDTH, BTN_HEIGHT
            self.color = ORANGE

    def draw(self):
        self.game.pg.draw.rect(self.game.screen, self.draw_color,
                               (self.pos[0], self.pos[1], BTN_WIDTH, BTN_HEIGHT))

        self.game.screen.blit(self.tag, (self.pos[0] + BTN_NAME_TAG_OFFSET_X,
                                         self.pos[1] + BTN_NAME_TAG_OFFSET_Y))

    def press(self):        # to be removed when cleared from Game.py
        self.activate()
        self.game.guess.check(self.name)
        self.deactivate()

    def activate(self):
        self.is_active = True
        self.draw_color = self.color
        self.draw()
        if self.name == 'q':
            self.game.sound.play_q()
        elif self.name == 'w':
            self.game.sound.play_w()
        elif self.name == 'a':
            self.game.sound.play_a()
        elif self.name == 's':
            self.game.sound.play_s()

        self.game.pg.time.delay(DELAY_TIME)
        self.deactivate()

    def deactivate(self):
        self.is_active = False
        self.draw_color = self.color + '4'
'''
