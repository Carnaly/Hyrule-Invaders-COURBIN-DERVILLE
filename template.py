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
from tkinter import  Button, Canvas, Label, PhotoImage, Tk, mainloop
from tkinter.constants import ANCHOR, NW


#Création de la fenêtre
invade = Tk()
invade.title('Hyrule Invaders')
invade.geometry('1920x1080')

#Canevas
Canevas = Canvas(invade, width=1300, height=800, bg='black')
Canevas.place(x=0, y=0)

#Menu à droite
Menu = Canvas(invade, width=250, height=800, bg='white')
Menu.place(x=1300, y=0)

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

#Insertion du joueur
PosX =600
PosY =700
imgjoueur = PhotoImage(file='Link.png')
Pion = Canevas.create_image(PosX, PosY, image=imgjoueur)

#Insertion des ennemis
imgennemi1=PhotoImage(file='Octorock.png')
imgennemi2=PhotoImage(file='Moblin.png')
XA=50
XB=170
XC=290
XD=410
XE=530
XF=650
XG=770
XH=890
Y=90
EnnemiA = Canevas.create_image(XA,Y, image=imgennemi1)
EnnemiB = Canevas.create_image(XB,Y, image=imgennemi2)
EnnemiC = Canevas.create_image(XC,Y, image=imgennemi1)
EnnemiD = Canevas.create_image(XD,Y, image=imgennemi2)
EnnemiE = Canevas.create_image(XE,Y, image=imgennemi1)
EnnemiF = Canevas.create_image(XF,Y, image=imgennemi2)
EnnemiG = Canevas.create_image(XG,Y, image=imgennemi1)
EnnemiH = Canevas.create_image(XH,Y, image=imgennemi2)

def deplacementEnnemis():
    global XA, XB, XC, XD, XE, XF, XG, XH, Y
    DX= 10
    if XA+50 >= 1300 or XB+50 >= 1300 or XC+50 >= 1300 or XD+50 >= 1300 or XE+50 >= 1300 or XF+50 >= 1300 or XG+50 >= 1300 or XH+50 >= 1300 or
        DX=-DX
        Y+=20 
    if XA-50 <= 0 or XB-50 <= 0 or XC-50 <= 0 or XD-50 <= 0 or XE-50 <= 0 or XF-50 <= 0 or XG-50 <= 0 or XH-50 <= 0:
        DX = -DX
        Y+=20
    





def deplacement(event):
    # Gestion de l'événement Appui sur une touche de clavier
    global PosX, PosY
    touche = event.keysym

    # Déplacement vers la gauche
    if touche == 'q' or touche == 'Left':
        if PosX - 30 > 0 :
            PosX -= 30
        Canevas.coords(Pion, PosX-10, PosY-10)
    
    # Déplacement vers la droite
    if touche == 'd' or touche == 'Right':
        if PosX + 30 < 1300 : 
            PosX += 30
        Canevas.coords(Pion, PosX-10, PosY-10)

Canevas.after(50, deplacement)

# Tir du joueur

def tir_joueur(event):
    global PosX, PosY
    touche = event.keysym
    print(touche)

    # Tir
    if touche == 'space' or touche == 'Up':
        tir_test(PosX)
        print('boom')

def tir_test(PosX):
    y = 700
    Projectile = Canevas.create_rectangle(PosX-2, y, PosX+2, y+10 , width=5, outline='white', fill='white')
    while y > 0 :
        y -= 10
        Canevas.coords(Projectile, PosX-2, y, PosX+2, y+10)
        print(Canevas.coords(Projectile))
        Canevas.after(50)

Canevas.focus_set()
Canevas.bind('<Key>',deplacement)

invade.mainloop()