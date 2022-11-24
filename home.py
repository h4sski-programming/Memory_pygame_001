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
                          (HOME_START_X,
                           HOME_START_Y,
                           HOME_START_WIDTH,
                           HOME_START_HEIGHT))
        self.screen.blit(self.start,
                         (HOME_START_X + HOME_PADDING,
                          HOME_START_Y + HOME_PADDING))

        self.pg.draw.rect(self.screen, RED,
                          (HOME_EXIT_X,
                           HOME_EXIT_Y,
                           HOME_EXIT_WIDTH,
                           HOME_EXIT_HEIGHT))
        self.screen.blit(self.exit_home,
                         (HOME_EXIT_X + HOME_PADDING,
                          HOME_EXIT_Y + HOME_PADDING))

    def check_events(self):
        for event in self.pg.event.get():
            if event.type == self.pg.QUIT or (event.type == self.pg.KEYDOWN and event.key == self.pg.K_ESCAPE):
                self.is_running = False

            lmb = self.pg.mouse.get_pressed()[0]
            if lmb:
                mouse_x, mouse_y = self.pg.mouse.get_pos()
                if HOME_START_X < mouse_x < (HOME_START_X + HOME_START_WIDTH) and HOME_START_Y < mouse_y < (HOME_START_Y + HOME_START_HEIGHT):
                    self.start_game = True
                elif HOME_EXIT_X < mouse_x < (HOME_EXIT_X + HOME_EXIT_WIDTH) and HOME_EXIT_Y < mouse_y < (HOME_EXIT_Y + HOME_EXIT_HEIGHT):
                    self.is_running = False

    def run(self):
        while self.is_running:
            self.check_events()
            self.draw()
            self.update()
            if self.start_game:
                break
