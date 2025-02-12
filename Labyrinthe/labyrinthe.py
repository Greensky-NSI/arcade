from p5 import *

class Labyrinthe:
    def __init__(self,largeur,hauteur,taille_case):
        self.largeur=largeur
        self.hauteur=hauteur
        self.taille_case=taille_case
        self.nb_lignes=hauteur//taille_case
        self.nb_colonnes=largeur//taille_case
        self.grille=[["vide" for i in range(self.nb_colonnes)] for i in range(self.nb_lignes)]
        self.obstacles=[]

    def obstacle(self,obstacles):
        self.obstacles=obstacles
        for x,y in obstacles:
            self.grille[y][x]="obstacle"

    def muraille(self,x,y):
        fill(80)
        rect((x*self.taille_case,y*self.taille_case),self.taille_case,self.taille_case)

        fill(100)
        no_stroke()
        circle((x*self.taille_case+self.taille_case*0.3,y*self.taille_case+self.taille_case*0.3),self.taille_case*0.2)
        circle((x*self.taille_case+self.taille_case*0.7,y*self.taille_case+self.taille_case*0.7),self.taille_case*0.2)
        circle((x*self.taille_case+self.taille_case*0.5,y*self.taille_case+self.taille_case*0.5),self.taille_case*0.15)

        stroke(60)
        stroke_weight(3)
        line((x*self.taille_case,y*self.taille_case),(x*self.taille_case+self.taille_case,y*self.taille_case))
        line((x*self.taille_case,y*self.taille_case+self.taille_case),(x*self.taille_case+self.taille_case,y*self.taille_case+self.taille_case))
        line((x*self.taille_case,y*self.taille_case),(x*self.taille_case,y*self.taille_case+self.taille_case))
        line((x*self.taille_case+self.taille_case,y*self.taille_case),(x*self.taille_case+self.taille_case,y*self.taille_case+self.taille_case))

    def afficher_laby(self):
        for y in range(self.nb_lignes):
            for x in range(self.nb_colonnes):
                if self.grille[y][x]=="vide":
                    fill(240,240,255)
                    stroke(200,200,255)
                    rect((x*self.taille_case,y*self.taille_case),self.taille_case,self.taille_case)
                elif self.grille[y][x]=="obstacle":
                    self.muraille(x,y)

largeur=800
hauteur=600
taille_case=40

labyrinthe=Labyrinthe(largeur,hauteur,taille_case)

obstacles=[
    (0,1),(0,13),
    (1,1),(1,10),(1,11),(1,12),(1,13),
    (2,1),(2,2),(2,3),(2,4),(2,5),(2,6),
    (3,1),
    (4,1),(4,11),(4,12),(4,13),
    (5,1),(5,5),(5,6),(5,7),(5,13),
    (6,7),(6,13),
    (7,7),(7,10),(7,11),(7,12),(7,13),(7,14),
    (8,0),(8,1),(8,2),(8,3),(8,7),
    (9,7),
    (10,10),(10,11),(10,12),
    (11,11),
    (12,11),
    (13,3),(13,11),
    (14,3),(14,10),(14,11),
    (15,3),
    (16,1),(16,2),(16,3),
    (17,6),(17,7),(17,10),(17,11),(17,12),(17,13),(17,14),
    (18,6),
    (19,6),
]
labyrinthe.obstacle(obstacles)

def setup():
    size(largeur,hauteur)

def draw():
    background(30,30,50)
    labyrinthe.afficher_laby()

run()