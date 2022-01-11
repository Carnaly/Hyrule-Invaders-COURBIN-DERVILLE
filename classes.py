    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Que fait ce programme : Ce programme regroupe l'ensemble des classes utilisées pour les objets crés : 
        les ennemis, le joueur, les blocs, les projectiles

Qui l'a fait : Michel COURBIN, Thomas DERVILLE

Créé le 14 décembre 2021 à 08:38

Que reste-t-il à faire ?
- classe octorok
- mouvement octo
- classe moblin
- mouvement moblin
- classe joueur
- classe projectile joueur
- image proj link
- classe projectile octorok
- image proj octo
- classe projectile moblin
- image proj moblin
- classe block
- image bloc

"""



# Partie classe des ennemis
class enemy:
    # Création de la classe des ennemis, on leur attribue un nom une vitesse de mouvement et des points de vies
    def __init__(self, name, mvt_speed, life_point, type_projectile):
        self.name = name
        self.speed = mvt_speed
        self.life = life_point
        self.projectile = type_projectile

    def printname(self): # Temporaire
        print(self.name, self.speed, self.life)

class octorok(enemy):
    def __init__(self, mvt_speed, life_point):
        enemy.__init__(self, "octorok", mvt_speed, life_point, "proj_octo")

#class moblin(enemy):
#    def __init__(self, mvt_speed, life_point):
#       enemy.__init__(self, "moblin", mvt_speed, life_point, "proj_mob")


x = octorok(10,1)
x.printname()


# Partie classe des projectiles

class projectile:
    def __init__(self, name, mvt_speed, mvt_direction):
        self.name = name
        self.speed = mvt_speed
        self.direction = mvt_direction

class proj_link(projectile):
    def __init__(self, mvt_speed, mvt_direction):
        projectile.__init__("proj_link", mvt_speed, mvt_direction)
        
class proj_octo(projectile):
    def __init__(self, mvt_speed, mvt_direction):
        projectile.__init__(self, "proj_octo", mvt_speed, mvt_direction)

#class proj_mob(projectile):
#    def __init__(self, mvt_speed, mvt_direction):
#        projectile.__init__(self, "proj_mob", mvt_speed, mvt_direction)


# Partie classe joueur

class link:
    def __init__(self, name, mvt_speed, life_point):
        self = Canevas.create_oval(PosX-10, PosY-10, PosX+10, PosY+10,width=5, outline='black', fill='red')
        self.name = name
        self.speed = mvt_speed
        self.life = life_point