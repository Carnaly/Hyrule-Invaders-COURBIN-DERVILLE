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


PosX =230
PosY =750

Pion = Canevas.create_oval(PosX-10, PosY-10, PosX+10, PosY+10,width=5, outline='black', fill='red')

def deplacement(event):
    # Gestion de l'événement Appui sur une touche de clavier
    global PosX, PosY
    touche = event.keysym
    print(touche)

    # Déplacement vers la gauche
    if touche == 'q' or touche == 'Left':
        PosX -= 30
    Canevas.coords(Pion, PosX-10, PosY-10, PosX+10, PosY+10)
    
    # Déplacement vers la droite
    if touche == 'd' or touche == 'Right':
        PosX += 30
    Canevas.coords(Pion, PosX-10, PosY-10, PosX+10, PosY+10)

Canevas.after(100000000000000, deplacement)

# Tir du joueur

def tir_joueur(event):
    global PosX, PosY
    touche = event.keysym
    print(touche)

    # Tir
    if touche == 'space' or touche == '<Up>':
        print('boom')


Canevas.focus_set()
Canevas.bind('<Key>',deplacement,)

invade.mainloop()