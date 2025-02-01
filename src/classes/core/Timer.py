class Timer:
    _current_tick = 0
    _cycle = 0

    def __init__(self, cycle, starting = 0):
        self._cycle = cycle
        self._current_tick = starting % cycle

    def tick(self):
        self._current_tick = (self._current_tick + 1) % self._cycle

        return self.ticked

    def update_max_cycle(self, cycle):
        self._cycle = cycle
        self._current_tick = self._current_tick % self._cycle

    @property
    def current_tick(self):
        return self._current_tick

    @property
    def cycle(self):
        return self._cycle

    @property
    def ticked(self):
        return self._current_tick == 0