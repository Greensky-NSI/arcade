class Timer:
    _current_tick = 0
    _cycle = 0

    def __init__(self, cycle, starting = 0):
        """
        Classe Timer pour gérer les cycles et les ticks.

        Attributs:
            _current_tick (int): Le tick actuel dans le cycle.
            _cycle (int): La durée totale du cycle.

        Méthodes:
            tick(self): Incrémente le tick actuel et retourne si le cycle est terminé.
            update_max_cycle(self, cycle): Met à jour la durée du cycle et ajuste le tick actuel.
            current_tick(self): Retourne le tick actuel.
            cycle(self): Retourne la durée du cycle.
            ticked(self): Retourne True si le cycle est terminé, sinon False.
        """
        self._cycle = cycle
        self._current_tick = starting % cycle

    def tick(self):
        """
        Incrémente le tick actuel et retourne si le cycle est terminé.

        :return:
        """
        self._current_tick = (self._current_tick + 1) % self._cycle

        return self.ticked

    def update_max_cycle(self, cycle):
        """
        Met à jour la durée du cycle et ajuste le tick actuel.

        :param cycle:
        :return:
        """
        self._cycle = cycle
        self._current_tick = self._current_tick % self._cycle

    @property
    def current_tick(self):
        """
        Retourne le tick actuel.

        :return:
        """
        return self._current_tick

    @property
    def cycle(self):
        """
        Retourne la durée du cycle.

        :return:
        """
        return self._cycle

    @property
    def ticked(self):
        """
        Retourne True si le cycle est terminé, sinon False.

        :return:
        """
        return self._current_tick == 0