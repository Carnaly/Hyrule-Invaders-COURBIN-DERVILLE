    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Que fait ce programme : 

Qui l'a fait : Michel COURBIN, Thomas DERVILLE

Créé le [date] à [heure]

Que reste-t-il à faire ?
[tout doux liste]
"""


from tkinter import Button, Canvas, Label, PhotoImage, Tk, mainloop
from tkinter.constants import ANCHOR, NW


#Création de la fenêtre
invade = Tk()
invade.title('Hyrule Invaders')
invade.geometry('1920x1080')

#Canevas
Canevas = Canvas(invade, width=1600, height=1080, bg='black')
Canevas.place(x=0, y=0)

#Menu à droite
Menu = Canvas(invade, width=250, height=1080, bg='white')
Menu.place(x=1600, y=0)

#Logo Menu
imgname=PhotoImage(file="Logopetit.png")
Menu.create_image(25,0, anchor=NW, image=imgname)
Menu.plop=imgname


#Zone de Score
Score= Label(invade, text="Score")
Score.config(font=('Courier',12))
Score.place (in_=Menu, x=100, y = 250)

#bouton quitter
Quit = Button(invade, text = 'Quitter', command = invade.destroy)
Quit.place(in_=Menu, x=100, y= 400)

#bouton nouvelle partie
New= Button(invade, text='Nouvelle Partie')#, command=NewGame)
New.place(in_=Menu, x=80, y= 370)

#Images 

img_joueur = []
img_joueur.append(PhotoImage(file='Link.png')) # Image du joueur
img_joueur.append(PhotoImage(file='LinkAttack.png')) # Image lors de l'attaque
num_img_joueur = 0
#
img_octo = PhotoImage(file='Octorock.png') # Image ennemis type 1
img_moblin = PhotoImage(file='Moblin.png') # Image ennemis type 2
#img_ganon  = PhotoImage(file='Ganon.png') # Image ennemis type spécial
img_proj_joueur = PhotoImage(file='Projectile.png') # Image projectile du joueur


# Partie classe des ennemis
class enemy:
    # Création de la classe des ennemis, on leur attribue un nom une vitesse de mouvement et des points de vies
    def __init__(self, name, position, life_point, type_projectile,image):
        self.name = name
        self.speed = position
        self.life = life_point
        self.projectile = type_projectile
        self.image = image


class octorok(enemy):
    def __init__(self, position, life_point):
        enemy.__init__(self, "octorok", position, life_point, "proj_octo", img_octo)


class moblin(enemy):
    def __init__(self, position, life_point):
        enemy.__init__(self, "moblin", position, life_point, "proj_mob", img_moblin)




# Partie classe des projectiles

class projectile:
    def __init__(self, name, position, mvt_direction):
        self.name = name
        self.position = position
        self.direction = mvt_direction
        self.proj = Canevas.create_image(position, image = img_proj_joueur)


class proj_link(projectile):
    def __init__(self, position, mvt_direction):
        projectile.__init__(self,"proj_link", position, mvt_direction)

class proj_octo(projectile):
    def __init__(self, position, mvt_direction):
        projectile.__init__(self, "proj_octo", position, mvt_direction)

class proj_mob(projectile):
    def __init__(self, position, mvt_direction):
        projectile.__init__(self, "proj_mob", position, mvt_direction)


# Partie classe joueur

class link:
    def __init__(self, name, position, life_point):
        Link = Canevas.create_image(position,image = img_joueur)
        self.name = name
        self.life = life_point



PosX =800
PosY =900

Pion = Canevas.create_image(PosX, PosY, image=img_joueur[num_img_joueur])


def actions_joueur(event):
    # Gestion de l'événement Appui sur une touche de clavier
    global PosX, PosY
    touche = event.keysym

    # Déplacement vers la gauche
    if touche == 'q' or touche == 'Left':
        if PosX - 30 > 0 :
            PosX -= 30
        Canevas.coords(Pion , PosX, PosY)
        Canevas.after(10,actions_joueur)
    
    # Déplacement vers la droite
    if touche == 'd' or touche == 'Right':
        if PosX + 30 < 1600 : 
            PosX += 30
        Canevas.coords(Pion, PosX, PosY)
        Canevas.after(10,actions_joueur)
    
    # Tir du joueur
    if touche == 'space' or touche == 'Up':
        print('boom')
        num_img_joueur = 1
        Projectile = Canevas.create_image(PosX, PosY-100, image=img_proj_joueur)       # proj_link((PosX, PosY-100), 1)
        deplacement_proj(Projectile)
        Canevas.after(100)
        Canevas.itemconfig(Pion,image=img_joueur[num_img_joueur])   
        Canevas.after(100)
#        num_img_joueur = 0
#        Canevas.itemconfig(Pion, image=img_joueur[num_img_joueur])

def deplacement_proj(Projectile):
    proj_x,proj_y = Canevas.coords(Projectile)
    Canevas.move(Projectile, 0, -15)
    if proj_y < 10:
        Canevas.delete(Projectile)
    Canevas.after(100,deplacement_proj,Projectile)



#Insertion des ennemis
XA=50
XB=170
XC=290
XD=410
XE=530
XF=650
XG=770
XH=890
Y=90
DX=20
EnnemiA = Canevas.create_image(XA,Y, image=img_octo)
EnnemiB = Canevas.create_image(XB,Y, image=img_moblin)
EnnemiC = Canevas.create_image(XC,Y, image=img_octo)
EnnemiD = Canevas.create_image(XD,Y, image=img_moblin)
EnnemiE = Canevas.create_image(XE,Y, image=img_octo)
EnnemiF = Canevas.create_image(XF,Y, image=img_moblin)
EnnemiG = Canevas.create_image(XG,Y, image=img_octo)
EnnemiH = Canevas.create_image(XH,Y, image=img_moblin)

def deplacementEnnemis():
    global XA, XB, XC, XD, XE, XF, XG, XH, Y, DX
    if (XA+50 > 1300) or (XB+50 > 1300) or (XC+50 > 1300) or (XD+50 > 1300) or (XE+50 > 1300) or (XF+50 > 1300) or (XG+50 > 1300) or (XH+50 > 1300):
        DX = -DX
        Y += 20 
    if XA-50 < 0 or XB-50 < 0 or XC-50 < 0 or XD-50 < 0 or XE-50 < 0 or XF-50 < 0 or XG-50 < 0 or XH-50 < 0:
        DX = -DX
        Y += 20
    XA = XA + DX 
    XB = XB + DX 
    XC = XC + DX 
    XD = XD + DX 
    XE = XE + DX 
    XF = XF + DX 
    XG = XG + DX
    XH = XH + DX
    Canevas.coords(EnnemiA, XA, Y)
    Canevas.coords(EnnemiB, XB, Y)
    Canevas.coords(EnnemiC, XC, Y)
    Canevas.coords(EnnemiD, XD, Y)
    Canevas.coords(EnnemiE, XE, Y)
    Canevas.coords(EnnemiF, XF, Y)
    Canevas.coords(EnnemiG, XG, Y)
    Canevas.coords(EnnemiH, XH, Y)
    invade.after(600, deplacementEnnemis)

deplacementEnnemis()

Canevas.after(10,actions_joueur)

Canevas.focus_set()
Canevas.bind('<Key>',actions_joueur)

invade.mainloop()

