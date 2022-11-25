from settings import *
from sound import Sound


class Btn:
    def __init__(self, game, name) -> None:
        self.game = game
        self.name = name
        self.is_active = False
        self.activate_time = 0
        self.font = self.game.pg.font.SysFont(None, BTN_TAG_FONT_SIZE)
        self.tag = self.font.render(self.name, True, BTN_TAG_COLOR)
        self.tag.set_alpha(BTN_TAG_COLOR_ALPHA)

        self.init_settup()
        self.color_darker = self.color + '4'

    def __str__(self) -> str:
        return self.name

    def init_settup(self):
        if self.name == 'q':
            self.position = 0, 0
            self.sound = Sound(self.game, self.name)
            self.color = BLUE
        elif self.name == 'w':
            self.position = BTN_WIDTH, 0
            self.sound = Sound(self.game, self.name)
            self.color = RED
        elif self.name == 'a':
            self.position = 0, BTN_HEIGHT
            self.sound = Sound(self.game, self.name)
            self.color = GREEN
        elif self.name == 's':
            self.position = BTN_WIDTH, BTN_HEIGHT
            self.sound = Sound(self.game, self.name)
            self.color = ORANGE

    def draw(self):
        if not self.is_active:
            self.game.pg.draw.rect(self.game.screen, self.color_darker,
                                   (self.position[0], self.position[1], BTN_WIDTH, BTN_HEIGHT))
        else:
            self.game.pg.draw.rect(self.game.screen, self.color,
                                   (self.position[0], self.position[1], BTN_WIDTH, BTN_HEIGHT))

        self.game.screen.blit(self.tag,
                              (self.position[0] + BTN_NAME_TAG_OFFSET_X,
                               self.position[1] + BTN_NAME_TAG_OFFSET_Y))

    def activate(self):
        self.is_active = True
        self.activate_time = self.game.pg.time.get_ticks()
        self.sound.play_sound()

    def deactivate(self):
        self.is_active = False
