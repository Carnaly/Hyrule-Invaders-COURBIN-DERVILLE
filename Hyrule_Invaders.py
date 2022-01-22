    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Que fait ce programme : Ce programme lance le jeu type Space Invaders inspiré du monde de The Legend Of Zelda.

Qui l'a fait : Michel COURBIN, Thomas DERVILLE

Créé le 11 Janvier 2022 à 09:03

Que reste-t-il à faire ?
[tout doux liste]
"""


from encodings import utf_8
from random import randrange
from tkinter import Button, Canvas, Label, PhotoImage, Tk, font, mainloop, Text
from tkinter.constants import ANCHOR, NW, CENTER, END, BOTH



################################ CRÉATION DE LA FENETRE DU JEU ################################

invade = Tk()
invade.title('Hyrule Invaders')
invade.geometry('1920x1080')


############################################ IMAGES ############################################

img_titre = PhotoImage(file="Logo.png") # Image du logo titre
img_logo = PhotoImage(file="Logopetit.png") # Image du logo
# img_fond = PhotoImage(file="Fond.png") # Image du fond de l'écran titre
# img_bg = PhotoImage(file="Background.png") # Image de l'arrière plan du jeu
img_go = PhotoImage(file="GameOver.png") # Image du Game Over


img_coeur = PhotoImage(file='FullHeart.png') # Image du coeur rempli
img_mi_coeur = PhotoImage(file='HalfHeart.png') # Image du demi coeur 
img_coeur_vide = PhotoImage(file='HollowHeart.png') # Image du coeur vide

img_joueur = PhotoImage(file='Link.png') # Image du joueur
img_attack = PhotoImage(file='LinkAttack.png') # Image lors de l'attaque
img_proj_joueur = PhotoImage(file='Projectile.png') # Image projectile du joueur

img_octo = PhotoImage(file='Octorock.png') # Image ennemis type 1
img_proj_octo = PhotoImage(file='ProjectileOcto.png') # Image projectile octorock
img_moblin = PhotoImage(file='Moblin.png') # Image ennemis type 2
img_proj_mob = PhotoImage(file='ProjectileMob.png') # Image projectile moblin
img_ganon  = PhotoImage(file='Ganon.png') # Image ennemis type spécial
img_proj_ganon  = PhotoImage(file='ProjectileGanon.png') # Image projectile ennemis type spécial

img_buis = PhotoImage(file='Buisson.png') # Image bloc



# Création des variables globales du jeu

global ennemi_speed, proj_speed, nbr_ennemi, pt_vie, Joueur, score, vague, blocs, Canevas, Fin, Start, Quitter, Infos, Titre



def start_game():
    global ennemi_speed, proj_speed, nbr_ennemi, pt_vie, Joueur, score, vague, blocs, Canevas

    # Destruction de l'écran titre
    Start.destroy()
    Quitter.destroy()
    Infos.destroy()
    Titre.destroy()

    # Réinitialisation des variables globales
    score = 0
    ennemi_speed = 200 
    proj_speed = 100 
    nbr_ennemi = 8 
    pt_vie = 2
    vague = 1
    blocs = []

    # Création du Canevas de jeu
    Canevas = Canvas(invade, width=1600, height=1080, bg='black')
    Canevas.place(x=0, y=0)

    #Menu à droite
    Menu = Canvas(invade, width=300, height=1080, bg='white')
    Menu.place(x=1600, y=0)

    #Logo Menu
    Menu.create_image(50,0, anchor=NW, image=img_logo)

    #Zone de Score
    Score= Label(invade, text='Score')

    #bouton quitter
    Quit = Button(invade, text = 'Quitter', command = invade.destroy)
    Quit.place(in_=Menu, x=100, y= 400)

    #bouton nouvelle partie
    New= Button(invade, text='Nouvelle Partie')#, command=restart_game)
    New.place(in_=Menu, x=80, y= 370)

    # Zone de points de vies

    Vie = Label(invade, text="Vies")
    Vie.config(font=('Courier',12))
    vie_x = 0
    Vie_box = []
    Vie_full = []
    Vie_box.append(Vie_full)
    Vie.place (in_=Menu, x=100, y = 700)
    for i in range(pt_vie//2):
        Vie_full.append(Menu.create_image(vie_x, 800, anchor = NW, image = img_coeur))
        vie_x +=60

    #Joueur = link()

    #score_maj()
    #init_ennemi(nbr_ennemi)
    #init_bloc()


def informations():

    Informations = Canvas(invade, width=1920, height=1080, bg='black')
    Informations.place(x=0, y=0)
    Zone_texte = Canvas(Informations)
    Zone_texte.place(x=0, y=0, width = 1920, height = 900)
    texte = Text(Zone_texte)
    texte.pack(fill=BOTH, expand=1)

    tf = open('README.txt','r',encoding='utf-8')
    data = tf.read()
    texte.insert(END,data)
    texte.configure(font=('Courier', 12), state='disabled')
    texte.tag_add("start", '1.0', 'end')
    texte.tag_config("start", background="black", foreground="green")
    tf.close()

    Quit = Button(Informations, text = 'Retour', font = (16), command = Informations.destroy)
    Quit.place(relx=0.5, rely=0.85, anchor=CENTER)

################################## CRÉATION DE L'ÉCRAN TITRE ###################################

def title():
    global Titre, Start, Quitter, Infos

    Titre = Canvas(invade, width=1920, height=1080, bg='black')
    Titre.place(x=0, y=0)

    # Image de fond

    Titre.create_image(0,0, anchor = NW, image = img_go)

    # Logo du jeu

    Titre.create_image(500,0,anchor=NW, image = img_titre)


    # Bouton début du jeu

    Start = Button(invade, text = 'Commencer',font = (16) , command = start_game)
    Start.place(relx=0.5, rely=0.7, anchor=CENTER)



    # Bouton A Propos

    Infos = Button(invade, text = 'Informations', font = (16), command = informations)
    Infos.place(relx=0.5, rely=0.75, anchor=CENTER)


    # Bouton Quitter

    Quitter = Button(invade, text = 'Quitter', font = (16), command = invade.destroy)
    Quitter.place(relx=0.5, rely=0.8, anchor=CENTER)


title()

invade.mainloop()
