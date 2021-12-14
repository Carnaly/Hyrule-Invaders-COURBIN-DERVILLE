#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Que fait ce programme : 

Qui l'a fait : Michel COURBIN, Thomas DERVILLE

Créé le 14/12/2021 à 8:50

Que reste-t-il à faire ?
    -Canevas (zone principale du jeu)
    -Zone indiquant le score
    -Bouton "New game"
    -Bouton "Rage quit"
"""
from tkinter import Button, Canvas, Label, Tk, mainloop


#Création de la fenêtre
invade = Tk()
invade.title('Hyrule Invaders')
invade.geometry('1920x1080')

#Canevas
Canevas = Canvas(invade, width=1300, height=800, bg='black')
Canevas.place(x=0, y=0)

#Zone de Score
Score= Label(invade, text="Score")
Score.config(font=('Courier',12))
Score.place (x=1400, y = 100)

#bouton quitter
Quit = Button(invade, text = 'Quitter', command = invade.destroy)
Quit.place(x=1400, y= 400)

#bouton nouvelle partie
New= Button(invade, text='Nouvelle Partie')#, command=NewGame)
New.place(x=1400, y= 200)


invade.mainloop()