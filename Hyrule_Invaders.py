    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Que fait ce programme : Ce programme lance le jeu type Space Invaders inspiré du monde de The Legend Of Zelda.

Qui l'a fait : Michel COURBIN, Thomas DERVILLE

Créé le 11 Janvier 2022 à 09:03

Que reste-t-il à faire ?
- Écran pause
"""

# Importation des fonctions nécessaires

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
img_fond = PhotoImage(file="Fond.png") # Image du fond de l'écran titre
img_bg = PhotoImage(file="Background.png") # Image de l'arrière plan du jeu
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

global ecran, Start, Quitter, Autre, Canevas, Menu, Joueur, ennemi_speed, proj_speed, tir_speed, nbr_ennemi, pt_vie, vie_box, vie_full, score, ennemis,vague, blocs, Fin

########################################### CLASSES ############################################

# Pour toutes les classes on crée une image et une hit box associée.

# Classe du joueur
class link:

    def __init__(self):

        self.pos_x = 810
        self.pos_y = 860
        self.box = Canevas.create_rectangle(self.pos_x-36, self.pos_y, self.pos_x+38, self.pos_y+96, width=0)
        self.Link = Canevas.create_image(self.pos_x-40, self.pos_y , anchor=NW, image = img_joueur)



# Classes des ennemis
class enemy:
    # Création de la classe des ennemis, on leur attribue une position, des points de vies, 
    # un type de projectile et les points de score qu'ils donnent lors de l'élimination
    def __init__(self,  pos_x, pos_y, life_point, type_projectile, points):

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.life = life_point
        self.type_proj = type_projectile
        self.points = points


class octorok(enemy):

    def __init__(self, pos_x, pos_y):

        enemy.__init__(self, pos_x, pos_y, 1, proj_octo,50)

        self.box = Canevas.create_rectangle(self.pos_x-48, self.pos_y, self.pos_x+48, self.pos_y+96,width=0)
        self.img = Canevas.create_image(self.pos_x-48, self.pos_y , anchor=NW, image = img_octo)


class moblin(enemy):

    def __init__(self, pos_x, pos_y):

        enemy.__init__(self, pos_x, pos_y, 1, proj_mob,50)

        self.box = Canevas.create_rectangle(self.pos_x-48, self.pos_y, self.pos_x+48, self.pos_y+96,width=0)
        self.img = Canevas.create_image(self.pos_x-48, self.pos_y , anchor=NW, image = img_moblin)


# Ennemi Spécial
class ganon(enemy):

    def __init__(self, pos_x, pos_y):

        enemy.__init__(self, pos_x, pos_y, 4, proj_ganon, 1000)

        self.box = Canevas.create_rectangle(self.pos_x-48, self.pos_y, self.pos_x+48, self.pos_y+96,width=0)
        self.img = Canevas.create_image(self.pos_x-48, self.pos_y , anchor=NW, image = img_ganon)



# Classe des projectiles
class projectile:
    # On leur attribue une position, une direction, une image, une hit box et des points de vie.

    def __init__(self, pos_x, pos_y, mvt_direction, life):

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direction = mvt_direction
        self.life = life


class proj_link(projectile):

    def __init__(self, pos_x, pos_y):

        projectile.__init__(self, pos_x, pos_y, 1,1)
        self.proj = Canevas.create_image(self.pos_x, self.pos_y, image=img_proj_joueur)
        self.box = Canevas.create_rectangle(self.pos_x-16, self.pos_y-32, self.pos_x+16, self.pos_y+32,width=0)


class proj_octo(projectile):

    def __init__(self, pos_x, pos_y):

        projectile.__init__(self, pos_x, pos_y, 0,1)

        self.box = Canevas.create_rectangle(self.pos_x-16, self.pos_y-16, self.pos_x+16, self.pos_y+16,width=0)
        self.proj = Canevas.create_image(self.pos_x, self.pos_y, image=img_proj_octo)
      

class proj_mob(projectile):

    def __init__(self, pos_x, pos_y):

        projectile.__init__(self, pos_x, pos_y, 0,1)

        self.box = Canevas.create_rectangle(self.pos_x-10, self.pos_y-32, self.pos_x+10, self.pos_y+32, width=0)
        self.proj = Canevas.create_image(self.pos_x, self.pos_y, image=img_proj_mob)


class proj_ganon(projectile):

    def __init__(self, pos_x, pos_y):

        projectile.__init__(self, pos_x, pos_y, 0,1)

        self.proj = Canevas.create_image(self.pos_x, self.pos_y, image=img_proj_ganon)
        self.box = Canevas.create_rectangle(self.pos_x-32, self.pos_y-32, self.pos_x+32, self.pos_y+32, width=0)


# Classe des blocs
class buisson(enemy):

    def __init__(self, pos_x, pos_y):

        enemy.__init__(self,pos_x, pos_y, 3, None, 0)

        self.box = Canevas.create_rectangle(self.pos_x-48, self.pos_y, self.pos_x+16, self.pos_y+64, width=0)
        self.img = Canevas.create_image(self.pos_x-48, self.pos_y , anchor=NW, image = img_buis)


########################################## FONCTIONS ###########################################

# Fonction de début du jeu, utilisable à partir de l'écran titre et de l'écran de fin

def start_game():

    void()
    init_game()


# Fonction de réinitialisation du jeu utilisable dans le jeu

def restart_game():

    Canevas.destroy()
    Menu.destroy()
    init_game()


# Fonction d'initialisation du jeu

def init_game():
    global Canevas, Menu, zone_de_score, Joueur, Start, Quitter, ennemi_speed, proj_speed, tir_speed, nbr_ennemi, ennemis, pt_vie, vie_full, vie_box, score, vague, blocs

    # Réinitialisation des variables globales
    score = 0
    ennemi_speed = 600 
    proj_speed = 200 
    tir_speed = 50
    nbr_ennemi = 8 
    pt_vie = 10
    vague = 1
    blocs = []
    ennemis = []

    # Création du Canevas de jeu
    Canevas = Canvas(invade, width=1600, height=1080, bg='black')
    Canevas.create_image(0, 0, anchor=NW, image=img_bg)
    Canevas.place(x=0, y=0)

    #Menu à droite
    Menu = Canvas(invade, width=300, height=1080, bg='white')
    Menu.place(x=1600, y=0)

    #Logo Menu
    Menu.create_image(50,0, anchor=NW, image=img_logo)

    # Zone de Score
    zone_de_score= Label(invade, text='Score')

    # Bouton quitter
    Quitter = Button(invade, text = 'Quitter', command = invade.destroy)
    Quitter.place(in_=Menu, x=100, y= 400)

    # Bouton nouvelle partie
    Start = Button(invade, text='Nouvelle Partie', command=restart_game)
    Start.place(in_=Menu, x=80, y= 370)

    # Zone de points de vies
    vie = Label(invade, text="Vies")
    vie.config(font=('Courier',12))
    vie_x = 0
    vie_box = []
    vie_full = []
    vie_box.append(vie_full)
    vie.place (in_=Menu, x=100, y = 700)
    for i in range(pt_vie//2):
        vie_full.append(Menu.create_image(vie_x, 800, anchor = NW, image = img_coeur))
        vie_x +=60

    # Création du joueur
    Joueur = link()

    # Initialisation du score, des blocs et des ennemis
    score_maj()
    init_ennemi(nbr_ennemi)
    init_bloc()

    # Détection des touches des joueurs sur le Canevas de jeu
    Canevas.focus_set()
    Canevas.bind('<Key>',actions_joueur)



# Destruction de l'écran précédent (Titre ou Fin)

def void():

    Start.destroy()
    Quitter.destroy()
    Autre.destroy()
    ecran.destroy()


# Fonction de mise à jour du score dans la zone de score

def score_maj():

    zone_de_score = Label(Menu, text =('Score : ' + str(score)))
    zone_de_score.config(font=('Courier', 12))
    zone_de_score.place (in_=Menu, x=10, y = 250)


# Fonction d'initialisation des blocs de protection

def init_bloc():

    global blocs

    cases_vides = [[0,1,6,7,8,9,10,11,12,13,18,19],[0,7,8,9,10,11,12,19]]
    position = [600,664]
    for j in range(2):
        pos_x = 190
        vide = cases_vides[j]
        pos_y = position[j]
        for i in range(20):
            if i not in vide:
                blocs.append(buisson(pos_x, pos_y))
            pos_x+=64


# Fonction d'initialisation d'une vague d'ennemis normaux

def init_ennemi(n):

    # On crée les n ennemis sur différents emplacements en haut de l'écran
    pos_x = 120

    for i in range(n):
    # On altère entre octorock et moblin, pair octorock, impair moblin

        if i % 2 == 0:
            ennemis.append(octorok(pos_x, 0))
            pos_x+=120


        if i % 2 == 1:
            ennemis.append(moblin(pos_x, 0))
            pos_x+=120
    
    actions_ennemi(ennemis, 0)


# Fonction d'initialisation d'une vague avec un ennemi spécial

def init_ganon():
    global ennemis
    pos_x = 120
    ennemis.append(ganon(pos_x,0))
    actions_ennemi(ennemis, 0)


# Fonction qui commande les actions des ennemis

def actions_ennemi(ennemis, direction):
    # On choisit la direction vers laquelle le bloc d'ennemi va se déplacer
    # 1 pour la gauche, 0 pour la droite
    n = len(ennemis)

    if direction == 1 : 
    # Déplacement vers la gauche
        
        if ennemis[0].pos_x -30 < 90 :
        # Si on atteint le bord gauche on descend l'ennemi et 
        # il change de direction vers la droite

            if n == 1 :
                # Si l'ennemi est seul
                ennemis[0].pos_y += 30

            else :   
                for i in range(n):
                    ennemis[i].pos_y += 30
            direction = 0


        
        else : # Sinon on déplace donc l'ennemi vers la gauche 
            if n == 1 :
                # Si l'ennemi est seul
                ennemis[0].pos_x -= 30
            
            else :
                for i in range(n):
                    ennemis[i].pos_x -= 30


    if direction == 0 :
    # Déplacement vers la droite

        if ennemis[-1].pos_x +30 > 1520 :
        # Si on atteint le bord droite on descend l'ennemi et 
        # il change de direction vers la gauche
            if n == 1 :
                # Si l'ennemi est seul
                ennemis[0].pos_y += 30

            else :   
                for i in range(n):
                    ennemis[i].pos_y += 30
            direction = 1
        

        
        else : # Sinon on déplace donc l'ennemi vers la droite 
            if n == 1 :
                # Si l'ennemi est seul
                ennemis[0].pos_x += 30
            
            else :
                for i in range(n):
                    ennemis[i].pos_x += 30

    # Tir aléatoires
    if n == 1 : # Si l'ennemi est seul
        k = randrange(tir_speed) 
        # On choisit un nombre entier aléatoire entre 0 et la valeur de tir_speed
        # Tir_speed diminue au cours des vagues donc la probabilité que l'ennemi tire à chaque déplacement augmente
        if k == 1 : # Si ce nombre vaut 1 alors l'ennemi tire 
            Projectile =  ennemis[0].type_proj(ennemis[0].pos_x, ennemis[0].pos_y+150)
            deplacement_proj(Projectile)
        
        # On déplace l'image et la hitbox de l'ennemi à ses nouvelles coordonnées
        Canevas.coords(ennemis[0].img, ennemis[0].pos_x-48, ennemis[0].pos_y+10)
        Canevas.coords(ennemis[0].box, ennemis[0].pos_x-48, ennemis[0].pos_y , ennemis[0].pos_x+48, ennemis[0].pos_y+96)


    else :
        for i in range(n):
            if ennemis[i].life == 1 :
                k = randrange(tir_speed)
                # On choisit un nombre entier aléatoire entre 0 et la valeur de tir_speed
                # Tir_speed diminue au cours des vagues donc la probabilité que l'ennemi tire à chaque déplacement augmente
                if k == 1 : # Si ce nombre vaut 1 alors l'ennemi tire 
                    Projectile =  ennemis[i].type_proj(ennemis[i].pos_x, ennemis[i].pos_y+150)
                    deplacement_proj(Projectile)

        for i in range(n):
            # On déplace l'image et la hitbox de chaque ennemi à ses nouvelles coordonnées
            Canevas.coords(ennemis[i].img, ennemis[i].pos_x-48, ennemis[i].pos_y+10)
            Canevas.coords(ennemis[i].box, ennemis[i].pos_x-48, ennemis[i].pos_y , ennemis[i].pos_x+48, ennemis[i].pos_y+96)
    

    if ennemis[0].pos_y > 500:
        # A partir de cette limite, on commence à vérifier si les ennemis arrivent au niveau des blocs

        m = len(blocs)
        tab = []
        for i in range(m):
            buiss_co = Canevas.coords(blocs[i].box)

            if buiss_co[1] < ennemis[0].pos_y + 100 :
                # Si les prochains déplacements de l'ennemi arrivent au niveau des blocs
                # on prend les indices des blocs concernés dans un tableau donc une ligne
                tab.append(i)

        while len(tab) != 0:
            # On détruit tout les blocs qui restent sur la ligne 
            Canevas.delete(blocs[0].img)
            blocs[0].life = 0            
            Canevas.delete(blocs[0].box)
            blocs.pop(0)
            tab.pop(0)

    if ennemis[0].pos_y > 700:
        # Si les ennemis passent sous cette limite le joueur a perdu

        end_game()
    Canevas.after(ennemi_speed, actions_ennemi, ennemis, direction)


# Fonction qui gère les actions possibles du joueur

def actions_joueur(event):
    touche = event.keysym # On récupère les touches pressées par le joueur

    # Déplacement vers la gauche si on appuie sur Q ou la flèche de gauche
    if touche == 'q' or touche == 'Left':
        if Joueur.pos_x - 30 > 60 :  
            Joueur.pos_x -= 30
    
    # Déplacement vers la droite si on appuie sur D ou la flèche de droite
    if touche == 'd' or touche == 'Right':
        if Joueur.pos_x +30 < 1520 : 
            Joueur.pos_x += 30

    # On déplace l'image et la hitbox du joueur
    Canevas.coords(Joueur.Link, Joueur.pos_x-40, Joueur.pos_y)
    Canevas.coords(Joueur.box, Joueur.pos_x-36, Joueur.pos_y,Joueur.pos_x+38, Joueur.pos_y+96)

    
    # Tir du joueur si on appuie sur Espace ou la flèche du haut
    if touche == 'space' or touche == 'Up':
        # On crée un projectile
        Projectile =  proj_link(Joueur.pos_x, Joueur.pos_y-80)

        # On le déplace
        deplacement_proj(Projectile)



# Fonction qui gère les déplacements des projectiles

def deplacement_proj(Projectile):
    # On vérifie la direction du projectile

    if Projectile.direction == 1 : # Si elle vaut 1 alors le projectile monte  

        proj_x,proj_y = Canevas.coords(Projectile.proj)

        if proj_y < 10: # Au delà de cette limite le projectile disparait
            Projectile.life = 0
            Canevas.delete(Projectile.proj)
            Canevas.delete(Projectile.box)
        proj_y = proj_y-15


    if Projectile.direction == 0 : # Si elle vaut 0 alors le projectile descend

        proj_x,proj_y = Canevas.coords(Projectile.proj)
        if proj_y > 1000: # Au delà de cette limite le projectile disparait
            Projectile.life = 0
            Canevas.delete(Projectile.proj)
            Canevas.delete(Projectile.box)
        proj_y = proj_y+15   
    
    # On déplace le projectile à ses nouvelles coordonnées

    Canevas.coords(Projectile.proj, proj_x, proj_y)
    Canevas.coords(Projectile.box, proj_x-16, proj_y-32, proj_x+16, proj_y+32)
    
    if Projectile.life == 1 : # Si le projectile n'est pas "mort" on détecte ses collisions
        detection_collision(Projectile)


# Fonction qui gère les collisions des projectiles

def detection_collision(Projectile):
    global pt_vie, score, blocs, Canevas, vie_box, vie_full, ennemis
    proj_co = Canevas.coords(Projectile.box) # On récupère les coordonnées du projectile

    if Projectile.direction == 1 : # Si le projectile monte alors on détecte les collisions avec les ennemis
        n = len(ennemis)
        for i in range(n):
            if ennemis[i].life != 0 :
                en_co = Canevas.coords(ennemis[i].box)

                if en_co[1] < proj_co[1] < en_co[3] and (en_co[0] < proj_co[0] < en_co[2] or en_co[0] < proj_co[2] < en_co[2]) :
                    # Si il y a collision on fait perdre un point de vie à l'ennemi 

                    ennemis[i].life -= 1

                    if ennemis[i].life == 0: 
                        # Si les points de vie de l'ennemi tombent à 0 
                        Canevas.delete(ennemis[i].img) # On détruit son image
                        score += ennemis[i].points # On augmente le score avec les points attribués à l'ennemi 
                        score_maj() # On met à jour le score

                    Projectile.life = 0 # On "tue" le projectile pour ne pas qu'il se déplace à nouveau
                    Canevas.delete(Projectile.proj) # On détruit son image
                    Canevas.delete(Projectile.box) # On détruit sa hit box

                    if n == 1: # si l'ennemi était seul
                        if ennemis[i].life == 0:
                            Canevas.delete(ennemis[i].box)
                            ennemis.pop(i) # On le retire de la liste des ennemis 
                            maj_vague() # On met à jour la vague d'ennemi

                    else : # Si on elimine un ennemi sur un bord 
                        if i == 0:
                            Canevas.delete(ennemis[i].box)
                            ennemis.pop(i)
                            while ennemis[i].life == 0 : 
                                # On retire toutes les hitbox des ennemis morts qui servaient à garder la structure du bloc ennemi
                                Canevas.delete(ennemis[i].box)
                                ennemis.pop(i)

                        if i == n-1 :
                            Canevas.delete(ennemis[i].box)
                            ennemis.pop(i)
                            i -= 1
                            while ennemis[i].life == 0 :
                                # On retire toutes les hitbox des ennemis morts qui servaient à garder la structure du bloc ennemi
                                Canevas.delete(ennemis[i].box)
                                ennemis.pop(i)
                                i-=1


    if Projectile.direction == 0 : # Si le projectile descend alors on détecte les collisions avec le joueur

        j_co = Canevas.coords(Joueur.box)

        if j_co[1] < proj_co[3] < j_co[3] and (j_co[0] < proj_co[0] < j_co[2] or j_co[0] < proj_co[2] < j_co[2]) :
            # Si il y a collision on retire un point de vie et on détruit le projectile
            pt_vie -=1
            Projectile.life = 0
            Canevas.delete(Projectile.proj)
            Canevas.delete(Projectile.box)

            if pt_vie == 0 : # Si le joueur tombe à 0 point de vie, c'est la fin du jeu
                end_game()

            if pt_vie % 2 == 1: # Si le joueur a un nombre impair de points de vie alors il a un demi coeur
                co = Menu.coords(vie_full[-1])
                vie_full.pop(-1)
                vie_box.append(Menu.create_image(co,anchor = NW, image = img_mi_coeur))
            
            if pt_vie % 2 == 0: # Si le joueur a un nombre pair alors on remplace le demi coeur par un coeur vide
                co = Menu.coords(vie_box[-1])
                vie_box.pop(1)
                vie_box.append(Menu.create_image(co, anchor = NW, image = img_coeur_vide))


    # Pour les deux directions on vérifie les collisions avec les blocs de protection

    m = len(blocs)
    for i in range(m):
        buiss_co = Canevas.coords(blocs[i].box)
        if (buiss_co[0] < proj_co[0] < buiss_co[2] or buiss_co[0] < proj_co[2] < buiss_co[2]) and (buiss_co[1] < proj_co[1] < buiss_co[3] or buiss_co[1] < proj_co[3] < buiss_co[3]) :
            # Si il y a collision on retire un point de vie au bloc

            if blocs[i].life == 1: # Si le bloc perd son dernier point de vie alors il est détruit
                Canevas.delete(blocs[i].img)
                blocs[i].life = 0            
                Canevas.delete(blocs[i].box)
                blocs.pop(i)

            else:
                blocs[i].life -= 1

            # On détruit le projectile
            Projectile.life = 0
            Canevas.delete(Projectile.proj)
            Canevas.delete(Projectile.box)

    if Projectile.life == 1 : # On continue les déplacements des projectiles uniquement s'ils sont "vivants"
        Canevas.after(proj_speed,deplacement_proj,Projectile)



# Fonction qui met à jour les vagues d'ennemis

def maj_vague():
    # On met à jour le numéro de la vague d'ennemis
    global vague, ennemi_speed, proj_speed, tir_speed, nbr_ennemi
    vague += 1

    if vague % 4 == 0:
        # Toutes les 3 vagues Ganon apparait
        init_ganon()
    
    else :
        # On change les variables globales responsables de la vitesse des ennemis et des projectiles pour augmenter la difficulté
        if proj_speed == 50 : # On définit tout de même des limites aux vitesses
            if ennemi_speed == 60:
                init_ennemi(nbr_ennemi)
            
            else :
                ennemi_speed -= 20
                init_ennemi(nbr_ennemi)

        else :
            ennemi_speed -= 20
            proj_speed -= 10
            tir_speed -= 2
            init_ennemi(nbr_ennemi)


# Fonction de fin de partie

def end_game():
    # On détruit le canvas du jeu

    Canevas.destroy()
    Menu.destroy()

    # Création de l'écran de fin

    Fin = Canvas(invade, width=1920, height=1080)
    Fin.place(x=0,y=0)
    Fin.create_image( 0, 0, anchor = NW, image = img_go) 

    # Zone de score

    zone_de_score = Label(Fin, text =('Score : ' + str(score)))
    zone_de_score.config(font=('Courier', 12))
    zone_de_score.place (relx = 0.5, rely = 0.65, anchor= CENTER)

    # Bouton début du jeu

    Start = Button(Fin, text = 'Commencer',font = (16), command = start_game)
    Start.place(relx=0.5, rely=0.7, anchor=CENTER)

    # Bouton Retour à l'écran titre

    Infos = Button(Fin, text = 'Écran Titre', font = (16), command = title)
    Infos.place(relx=0.5, rely=0.75, anchor=CENTER)


    # Bouton Quitter

    Quit = Button(Fin, text = 'Quitter', font = (16), command = invade.destroy)
    Quit.place(relx=0.5, rely=0.8, anchor=CENTER)


# Fonction qui affiche les informations du A Propos

def informations():

    Informations = Canvas(invade, width=1920, height=1080, bg='black')
    Informations.place(x=0, y=0)
    Zone_texte = Canvas(Informations)
    Zone_texte.place(x=0, y=0, width = 1920, height = 900)
    texte = Text(Zone_texte)
    texte.pack(fill=BOTH, expand=1)

    # On lit les données du fichier texte README

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
    global ecran, Start, Quitter, Autre

    ecran = Canvas(invade, width=1920, height=1080, bg='black')
    ecran.place(x=0, y=0)

    # Image de fond

    ecran.create_image(0,0, anchor = NW, image = img_fond)

    # Logo du jeu

    ecran.create_image(500,0,anchor=NW, image = img_titre)


    # Bouton début du jeu

    Start = Button(invade, text = 'Commencer',font = (16) , command = start_game)
    Start.place(relx=0.5, rely=0.7, anchor=CENTER)



    # Bouton A Propos

    Autre = Button(invade, text = 'Informations', font = (16), command = informations)
    Autre.place(relx=0.5, rely=0.75, anchor=CENTER)


    # Bouton Quitter

    Quitter = Button(invade, text = 'Quitter', font = (16), command = invade.destroy)
    Quitter.place(relx=0.5, rely=0.8, anchor=CENTER)


title() # On commence le jeu par un écran titre

invade.mainloop()
