    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Que fait ce programme : 

Qui l'a fait : Michel COURBIN, Thomas DERVILLE

Créé le [date] à [heure]

Que reste-t-il à faire ?
[tout doux liste]
"""

"""
Que fait ce programme : 

Qui l'a fait : Michel COURBIN, Thomas DERVILLE

Créé le [date] à [heure]

Que reste-t-il à faire ?
[tout doux liste]
"""

from email.mime import image
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






############################################ IMAGES ############################################


img_joueur = PhotoImage(file='Link.png') # Image du joueur
img_attack = PhotoImage(file='LinkAttack.png') # Image lors de l'attaque
img_proj_joueur = PhotoImage(file='Projectile.png') # Image projectile du joueur

img_octo = PhotoImage(file='Octorock.png') # Image ennemis type 1
img_moblin = PhotoImage(file='Moblin.png') # Image ennemis type 2
img_ganon  = PhotoImage(file='Ganon.png') # Image ennemis type spécial

img_buis = PhotoImage(file='Buisson.png') # Image bloc


################################################################################################

########################################### CLASSES ############################################


class link:

    def __init__(self): # ptet rajouter difficulté mdr

        self.life_pt = 6
        self.pos_x = 800
        self.pos_y = 800
        self.Link = Canevas.create_image(self.pos_x-40, self.pos_y , anchor=NW, image = img_joueur)




    


Pion = link()
Canevas.create_image(0, 0, anchor=NW, image=img_buis )
################################################################################################

########################################## FONCTIONS ###########################################


def actions_joueur(event):
    touche = event.keysym

    # Déplacement vers la gauche
    if touche == 'q' or touche == 'Left':
        if Pion.pos_x - 30 > 40 :    
            Pion.pos_x -= 30
        Canevas.coords(Pion.Link, Pion.pos_x-40, Pion.pos_y)

    # Déplacement vers la droite
    if touche == 'd' or touche == 'Right':
        if Pion.pos_x +30 < 1560 : 
            Pion.pos_x += 30
        Canevas.coords(Pion.Link, Pion.pos_x-40, Pion.pos_y)


    # Tir du joueur
    if touche == 'space' or touche == 'Up':
        print('boom')
        Projectile = Canevas.create_image(Pion.pos_x, Pion.pos_y-100, image=img_proj_joueur)       # proj_link((PosX, PosY-100), 1)
        #deplacement_proj(Projectile)




Canevas.after(10,actions_joueur)

Canevas.focus_set()
Canevas.bind('<Key>',actions_joueur)

################################################################################################

invade.mainloop()
