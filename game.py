from settings import *
from button import Btn
from guess import Guess


class Game:
    def __init__(self, main):
        self.m = main
        self.pg = main.pg
        self.screen = main.screen
        self.clock = main.clock
        self.is_running = True
        self.score = 0

        self.buttons = {
            'q': Btn(self, name='q'),
            'w': Btn(self, name='w'),
            'a': Btn(self, name='a'),
            's': Btn(self, name='s'),
        }
        self.guess = Guess(self)

        self.new_game()

    def update(self):
        self.pg.display.flip()
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
                    if not self.guess.check_player_correct(self.buttons['q']):
                        self.is_running = False
                elif keys[self.pg.K_w]:
                    if not self.guess.check_player_correct(self.buttons['w']):
                        self.is_running = False
                elif keys[self.pg.K_a]:
                    if not self.guess.check_player_correct(self.buttons['a']):
                        self.is_running = False
                elif keys[self.pg.K_s]:
                    if not self.guess.check_player_correct(self.buttons['s']):
                        self.is_running = False

        if not self.is_running:
            self.score = len(self.guess.correct) - 1

    def play_correct(self):
        tmp = []
        i = 0
        play_next_time = self.pg.time.get_ticks() + DELAY_TIME
        while True:
            if self.pg.time.get_ticks() > play_next_time:
                self.guess.correct[i].activate()
                tmp.append(self.guess.correct[i].name)
                play_next_time = self.pg.time.get_ticks() + DELAY_TIME
                i += 1

            # I think that this way is better then move this conndition to while loop.
            # This way I'm not constantly requesting for value "len(self.guess.correct)".
            if i >= len(self.guess.correct):
                break
            self.check_events()
            self.draw()
            self.update()
        print(tmp)

    def new_game(self):
        self.clock.tick(FPS)
        self.play_correct()

    def run(self):
        while self.is_running:
            self.check_events()
            self.draw()
            self.update()
