import sys
from settings import *


class Home:
    def __init__(self, main) -> None:
        self.pg = main.pg
        self.clock = main.clock
        self.screen = main.screen
        self.title = 'Home screen'
        self.is_running = True
        self.start_game = False
        self.font = self.pg.font.SysFont(None, HOME_FONT_SIZE)
        self.start = self.font.render('Start', True, WHITE)
        self.exit_home = self.font.render('Exit', True, WHITE)

    def update(self):
        self.pg.display.flip()
        self.clock.tick(FPS)
        self.pg.display.set_caption(f'{self.title}')

    def draw(self):
        self.screen.fill(BLACK)
        self.pg.draw.rect(self.screen, GREEN,
                          (50, 200, WINDOW_WIDTH/2 - 100, HOME_FONT_SIZE + HOME_TEXT_OFFSET))
        self.screen.blit(self.start,
                         (70, 220))
        self.pg.draw.rect(self.screen, RED,
                          (WINDOW_WIDTH/2 + 50, 200, WINDOW_WIDTH/2 - 100, HOME_FONT_SIZE + HOME_TEXT_OFFSET))
        self.screen.blit(self.exit_home,
                         (WINDOW_WIDTH/2 + 70, 220))

    def check_events(self):
        for event in self.pg.event.get():
            if event.type == self.pg.QUIT or (event.type == self.pg.KEYDOWN and event.key == self.pg.K_ESCAPE):
                self.is_running = False
                # self.pg.quit()
                # sys.exit()

            keys = self.pg.key.get_pressed()
            if keys[self.pg.K_p]:
                self.start_game = True

    def run(self):
        while self.is_running:
            self.check_events()
            self.update()
            self.draw()
            if self.start_game:
                break
