class PlayerStats:
    """
    Classe représentant les statistiques d'un joueur.
    """

    _stats = {
        "bombs": 1,
        "speed": 1,
        "range": 1,
        "score": 0,
    }

    def __init__(self):
        """
        Initialise les statistiques du joueur avec les valeurs par défaut.
        """
        pass

    # Propriétés
    @property
    def stats(self):
        """
        Retourne une copie des statistiques du joueur.

        :return: Dictionnaire des statistiques.
        """
        return self._stats.copy()

    @property
    def bombs(self):
        """
        Retourne le nombre de bombes du joueur.

        :return: Nombre de bombes.
        """
        return self._stats["bombs"]

    @property
    def speed(self):
        """
        Retourne la vitesse du joueur.

        :return: Vitesse.
        """
        return self._stats["speed"]

    @property
    def range(self):
        """
        Retourne la portée du joueur.

        :return: Portée.
        """
        return self._stats["range"]

    @property
    def score(self):
        """
        Retourne le score du joueur.

        :return: Score.
        """
        return self._stats["score"]

    # Ajouts
    def add_bombs(self, amount):
        """
        Ajoute un certain nombre de bombes aux statistiques du joueur.

        :param amount: Nombre de bombes à ajouter.
        :return: L'objet PlayerStats.
        """
        self._stats["bombs"] += amount
        return self

    def add_speed(self, amount):
        """
        Augmente la vitesse du joueur.

        :param amount: Quantité de vitesse à ajouter.
        :return: L'objet PlayerStats.
        """
        self._stats["speed"] += amount
        return self

    def add_range(self, amount):
        """
        Augmente la portée du joueur.

        :param amount: Quantité de portée à ajouter.
        :return: L'objet PlayerStats.
        """
        self._stats["range"] += amount
        return self

    def add_score(self, amount):
        """
        Augmente le score du joueur.

        :param amount: Quantité de score à ajouter.
        :return: L'objet PlayerStats.
        """
        self._stats["score"] += amount
        return self

    # Setters
    def set_bombs(self, amount):
        """
        Définit le nombre de bombes du joueur.

        :param amount: Nombre de bombes.
        :return: L'objet PlayerStats.
        """
        self._stats["bombs"] = amount
        return self

    def set_speed(self, amount):
        """
        Définit la vitesse du joueur.

        :param amount: Vitesse.
        :return: L'objet PlayerStats.
        """
        self._stats["speed"] = amount
        return self

    def set_range(self, amount):
        """
        Définit la portée du joueur.

        :param amount: Portée.
        :return: L'objet PlayerStats.
        """
        self._stats["range"] = amount
        return self

    def set_score(self, amount):
        """
        Définit le score du joueur.

        :param amount: Score.
        :return: L'objet PlayerStats.
        """
        self._stats["score"] = amount
        return self

    def reset(self):
        """
        Réinitialise les statistiques du joueur aux valeurs par défaut.

        :return: L'objet PlayerStats.
        """
        self._stats = {
            "bombs": 1,
            "speed": 1,
            "range": 1,
            "score": 0,
        }
        return self

    # Builtins
    def __repr__(self):
        """
        Retourne une représentation officielle de l'objet PlayerStats.

        :return: Représentation officielle de l'objet.
        """
        return f"PlayerStats({str(self)})"

    def __str__(self):
        """
        Retourne une chaîne de caractères lisible représentant l'objet PlayerStats.

        :return: Chaîne de caractères représentant l'objet.
        """
        string_repr = "\n    ".join(list(map(lambda x: f"{x[0]}: {x[1]}", self._stats.items())))

        return "PlayerStats: {\n    " + string_repr + "\n}"

    def __eq__(self, other):
        """
        Compare l'objet PlayerStats avec un autre objet pour l'égalité.

        :param other: L'autre objet à comparer.
        :return: True si les objets sont égaux, sinon False.
        """
        for key in self._stats.keys():
            if self._stats[key] != other.player_stats[key]:
                return False
        return True

    def __ne__(self, other):
        """
        Compare l'objet PlayerStats avec un autre objet pour l'inégalité.

        :param other: L'autre objet à comparer.
        :return: True si les objets ne sont pas égaux, sinon False.
        """
        return not self.__eq__(other)

    def __getitem__(self, key):
        """
        Retourne la valeur de la statistique associée à la clé donnée.

        :param key: La clé de la statistique.
        :return: La valeur de la statistique.
        """
        return self._stats[key]