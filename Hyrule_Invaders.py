    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Que fait ce programme : Ce programme lance le jeu type Space Invaders inspiré du monde de The Legend Of Zelda.

Qui l'a fait : Michel COURBIN, Thomas DERVILLE

Créé le 11 Janvier 2022 à 09:03

Que reste-t-il à faire ?
[tout doux liste]
"""


from tkinter import Button, Canvas, Label, PhotoImage, Tk, mainloop
from tkinter.constants import ANCHOR, NW


#Création de la fenêtre
invade = Tk()
invade.title('Hyrule Invaders')
invade.geometry('1920x1080')


Titre = Canvas(invade, width=1920, height=1080, bg='black')
Titre.place(x=0,y=0)
img_logo=PhotoImage(file="Logo.png")
Titre.create_image(500,0,anchor=NW, image=img_logo)

img_fac = PhotoImage(file="Buisson.png")
img_diff = PhotoImage(file="Buisson.png")

Titre.create_image(500,700,anchor=NW, image=img_fac)
Titre.create_image(1400,700,anchor=NW, image=img_diff)

def callback(event):
    Titre["bg"] = 'white' 
        


Titre.tag_bind(img_fac, 'Button-1', callback)
Titre.tag_bind(img_diff, 'Button-1', callback)



invade.mainloop()
