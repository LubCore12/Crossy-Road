from settings import *


class Timer:
    def __init__(self, duration, func = None, repeat = False, autorun = False):
        self.duration = duration
        self.start_time = 0
        self.func = func
        self.repeat = repeat

        self.active = False

        if autorun:
            self.activate()

    def __bool__(self):
        return self.active

    def activate(self):
        self.start_time = pygame.time.get_ticks()
        self.active = True

    def deactivate(self):
        self.start_time = 0
        self.active = False

        if self.repeat:
            self.activate()

    def update(self):
        if pygame.time.get_ticks() - self.start_time > self.duration:
            if self.func:
                self.func()
            self.deactivate()
