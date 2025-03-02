class PlayerStats:
    _stats = {
        "bombs": 1,
        "speed": 1,
        "range": 1,
        "score": 0,
    }

    def __init__(self):
        pass

    # Propriétés
    @property
    def stats(self):
        return self._stats.copy()

    @property
    def bombs(self):
        return self._stats["bombs"]

    @property
    def speed(self):
        return self._stats["speed"]

    @property
    def range(self):
        return self._stats["range"]

    @property
    def score(self):
        return self._stats["score"]

    # Ajouts
    def add_bombs(self, amount):
        self._stats["bombs"] += amount
        return self

    def add_speed(self, amount):
        self._stats["speed"] += amount
        return self

    def add_range(self, amount):
        self._stats["range"] += amount
        return self

    def add_score(self, amount):
        self._stats["score"] += amount
        return self

    # Setters
    def set_bombs(self, amount):
        self._stats["bombs"] = amount
        return self

    def set_speed(self, amount):
        self._stats["speed"] = amount
        return self

    def set_range(self, amount):
        self._stats["range"] = amount
        return self

    def set_score(self, amount):
        self._stats["score"] = amount
        return self

    def reset(self):
        self._stats = {
            "bombs": 1,
            "speed": 1,
            "range": 1,
            "score": 0,
        }
        return self

    # Builtins
    def __repr__(self):
        return f"PlayerStats({str(self)})"

    def __str__(self):
        string_repr = "\n    ".join(list(map(lambda x: f"{x[0]}: {x[1]}", self._stats.items())))

        return "PlayerStats: {\n    " + string_repr + "\n}"

    def __eq__(self, other):
        for key in self._stats.keys():
            if self._stats[key] != other.player_stats[key]:
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __getitem__(self, key):
        return self._stats[key]