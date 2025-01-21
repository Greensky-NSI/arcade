# Cahier des charges

Cahier des charges des attentes du projet

## Librairies et modules

Le projet doit être codé en [Python 3.10](https://www.python.org/downloads/release/python-3100/), avec la librairie [p5](https://pypi.org/project/p5/)

## Description

Le jeu est un **jeu d'arcade**, de type bomberman. Le joueur peut choisir un personnage qu'il incarnera avec les **flèches directionnelles** et la **barre espace**.
> Les contrôles peuvent changer si il y a plusieurs joueurs

L'arène est une grille, avec des **bords** et certains **murs** incassables ainsi que certains **obstacles**, de façon à former une sorte de labyrinthe. Le centre du labyrinthe est un carré, qui peut éventuellement avoir des propriétés (par exemple téléporter une attaque)
> Les cartes doivent être faites de façon à avoir les quatres coins libres, un centre, ainsi que des "couloirs" (grandes lignes droites, avec potentiellement des embranchements)

Le joueur se déplace **horizontalement** (⬅️➡️) et **verticalement** (⬆️⬇️), et peut placer une **bombe à sa position** avec la barre espace, explosant au bout de 4 secondes, avec un rayon de **1 case** sur chaque côté, détruisant le premier obstacle sur chaque côté, et tuant les joueurs touchés
> Une bombe qui explose et qui touche une autre bombe provoque l'explosion de cette dernière. Elles détruisent également les "stats" présents sur l'explosion.
> Les caractéristiques, telles que la **vitesse de déplacement**, le **nombre de bombes** que le joueur peut poser simultanément ainsi que la **portée** peuvent être augmentées avec des "stats" qui apparaissent dans la partie

Lorsqu'un joueur meurt, il réapparait à son **point d'origine** (un des **4 coins**), perd ses statistiques (qui sont redistribuées **sur la carte**), et recommence avec seulement une case coloriée.
> Le but du jeu est de colorier **50 cases** en **même temps** dans le temps imparti (**3 minutes**). Si aucun joueur n'a suffisament de cases au bout de ce délai, c'est le joueur avec le plus de cases qui l'emporte. Si il y a égalité, c'est le joueur avec le plus de points qui l'emporte
> Les points s'obtiennent en **détruisant des obstacles** ou en **tuant** des adversaires
> Lorsque des obstacles sont détruits, il peuvent donner des **"stats"** ou des **armes**

## Charges

| Fonctionnalité | Description | État |
|:--:|:--:|:----:|
| Écran de titre | Faire écran de titre du jeu, avec sélection du personnage | ❌ |
| Cartes | Faire une classe de carte, qui permet de créer facilement une carte de jeu | ❌ |
| Joueur | Implémenter une classe joueur | ❌ |
| Bombe | Implémenter une classe bombe | ❌ |

### Signification des signes

| Signe | Signification |
|:--:|:--:|
| ❌ | Non-implémenté |
| ✅ | Implémenté |
| 🚧 | En cours d'implémentation |
| 🚫 | Non-implémentable |
| ➖ | Fonctionnalité abandonnée |

### Organisation

Le projet doit s'organiser en modules, avec un fichier principal qui lance le jeu, et des fichiers dans des dossiers pour chaque classe.

Organisation prévue au moment de la rédaction (suceptible de changer) :

```cs
.gitignore
README.md
LICENSE
src/
  main.py
  classes/
    objects/
      bomb.py
      stat.py
    mobs/
      player.py
      projectiles.py
    complexes/
      map.py
  utils/
    toolbox.py
    constants.py
    globals.py
  types/
    typing.py
```

### Ressources

Les ressources peuvent venir de différentes sources. Aucune source n'est prescrite, du moment qu'elle est citée/utilisée correctement

#### Ressources déjà recensées

* [🍱 Ressources](#3)
* [Sites utiles](#2)
