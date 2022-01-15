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


from random import randrange
from tkinter import Button, Canvas, Label, PhotoImage, Tk, mainloop
from tkinter.constants import ANCHOR, NW


################################ CRÉATION DE LA FENETRE DU JEU ################################

invade = Tk()
invade.title('Hyrule Invaders')
invade.geometry('1920x1080')


############################################ IMAGES ############################################

img_titre = PhotoImage(file="Logo.png") # Image du logo titre
img_logo = PhotoImage(file="Logopetit.png") # Image du logo

img_coeur = PhotoImage(file='FullHeart.png') # Image du coeur rempli
img_mi_coeur = PhotoImage(file='HalfHeart.png') # Image du demi coeur 
img_coeur_vide = PhotoImage(file='HollowHeart.png') # Image du coeur vide

img_joueur = PhotoImage(file='Link.png') # Image du joueur
img_attack = PhotoImage(file='LinkAttack.png') # Image lors de l'attaque
img_proj_joueur = PhotoImage(file='Projectile.png') # Image projectile du joueur

img_octo = PhotoImage(file='Octorock.png') # Image ennemis type 1
#img_proj_octo = PhotoImage(file='ProjectileOcto.png') # Image projectile octorock
img_moblin = PhotoImage(file='Moblin.png') # Image ennemis type 2
#img_proj_mob = PhotoImage(file='ProjectileMob.png') # Image projectile moblin
img_ganon  = PhotoImage(file='Ganon.png') # Image ennemis type spécial

img_buis = PhotoImage(file='Buisson.png') # Image bloc



################################## CRÉATION DE L'ÉCRAN TITRE ###################################

# Image de fond






# Création des variables globales du jeu

global ennemi_speed, proj_speed, nbr_ennemi, pt_vie, Joueur


# Bouton sélection de la difficulté du jeu


ennemi_speed = 200 # choix de la vitesse des ennemis : facile = 600, difficile = 200 ?
proj_speed = 100 # choix de la vitesse des projectiles : facile = 100, difficile = 300 
nbr_ennemi = 8 # choix du nombre d'ennemis par ligne : facile = 6, difficile = 8 ?
pt_vie = 10 # choix du nombre de vie pour le joueur : facile = 10, difficile = 6 


# Bouton A Propos


# Bouton Quitter




###################################### CRÉATION DU CANVAS ######################################

#Canevas
Canevas = Canvas(invade, width=1600, height=1080, bg='black')
Canevas.place(x=0, y=0)

#Menu à droite
Menu = Canvas(invade, width=300, height=1080, bg='white')
Menu.place(x=1600, y=0)

#Logo Menu
Menu.create_image(50,0, anchor=NW, image=img_logo)

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


########################################### CLASSES ############################################



class link:

   def __init__(self): # ptet rajouter difficulté mdr

      self.pos_x = 800
      self.pos_y = 800
      self.Link = Canevas.create_image(self.pos_x-40, self.pos_y , anchor=NW, image = img_joueur)
      self.box = Canevas.create_rectangle(self.pos_x-48, self.pos_y, self.pos_x+48, self.pos_y+96)



class enemy:
    # Création de la classe des ennemis, on leur attribue un nom une vitesse de mouvement et des points de vies
   def __init__(self,  pos_x, pos_y, life_point, type_projectile):

      self.pos_x = pos_x
      self.pos_y = pos_y
      self.life = life_point
      self.type_proj = type_projectile


class octorok(enemy):

   def __init__(self, pos_x, pos_y):

      enemy.__init__(self, pos_x, pos_y, 1, proj_octo)

      self.img = Canevas.create_image(self.pos_x-48, self.pos_y , anchor=NW, image = img_octo)
      self.box = Canevas.create_rectangle(self.pos_x-48, self.pos_y, self.pos_x+48, self.pos_y+96)


class moblin(enemy):

   def __init__(self, pos_x, pos_y):

      enemy.__init__(self, pos_x, pos_y, 1, proj_mob)

      self.img = Canevas.create_image(self.pos_x-48, self.pos_y , anchor=NW, image = img_moblin)
      self.box = Canevas.create_rectangle(self.pos_x-48, self.pos_y, self.pos_x+48, self.pos_y+96)



class projectile:

   def __init__(self, pos_x, pos_y, mvt_direction):

      self.pos_x = pos_x
      self.pos_y = pos_y
      self.direction = mvt_direction


class proj_link(projectile):

   def __init__(self, pos_x, pos_y):

      projectile.__init__(self, pos_x, pos_y, 1)

      self.proj = Canevas.create_image(self.pos_x, self.pos_y, image=img_proj_joueur)
      self.box = Canevas.create_rectangle(self.pos_x-16, self.pos_y-32, self.pos_x+16, self.pos_y+32) 


class proj_octo(projectile):

    def __init__(self, pos_x, pos_y):

      projectile.__init__(self, pos_x, pos_y, 0)

      self.proj = Canevas.create_image(self.pos_x, self.pos_y, image=img_proj_joueur) #image=img_proj_octo) # à remplacer par image proj octo
      self.box = Canevas.create_rectangle(self.pos_x-16, self.pos_y-32, self.pos_x+16, self.pos_y+32) # à remplacer par dimension proj octo

class proj_mob(projectile):

    def __init__(self, pos_x, pos_y):

      projectile.__init__(self, pos_x, pos_y, 0)

      self.proj = Canevas.create_image(self.pos_x, self.pos_y, image=img_proj_joueur) #image=img_proj_mob) # à remplacer par image proj moblin
      self.box = Canevas.create_rectangle(self.pos_x-16, self.pos_y-32, self.pos_x+16, self.pos_y+32) # à remplacer par dimension proj moblin


Joueur = link()




########################################## FONCTIONS ###########################################

    
def actions_joueur(event):
   # On gère ici toutes les actions possible par le joueur
   touche = event.keysym
   print(touche)
   # Déplacement vers la gauche
   if touche == 'q' or touche == 'Left':
      if Joueur.pos_x - 30 > 40 :  
         Joueur.pos_x -= 30
   

   # Déplacement vers la droite
   if touche == 'd' or touche == 'Right':
      if Joueur.pos_x +30 < 1560 : 
         Joueur.pos_x += 30

   Canevas.coords(Joueur.Link, Joueur.pos_x-40, Joueur.pos_y)
   Canevas.coords(Joueur.box, Joueur.pos_x-48, Joueur.pos_y,Joueur.pos_x+48, Joueur.pos_y+96)

   # Tir du joueur
   if touche == 'space' or touche == 'Up':
      Projectile =  proj_link(Joueur.pos_x, Joueur.pos_y-100)
      deplacement_proj(Projectile)

   # Pause
   if touche == 'Return' or 'Escape' :
      print('Pause')



def detection_collision(Projectile):
   global pt_vie
   proj_co = Canevas.coords(Projectile.box)
   
   if Projectile.direction == 1 :

      n = len(ennemis)

      for i in range(n):
         
         en_co = Canevas.coords(ennemis[i].box)

         if en_co[1] < proj_co[1] < en_co[3] and (en_co[0] < proj_co[0] < en_co[2] or en_co[0] < proj_co[2] < en_co[2]) :
            
            Canevas.delete(ennemis[i].img)

            if i == 0:
               Canevas.delete(ennemis[i].box)
               ennemis.pop(i)
               while ennemis[i].life == 0 :
                  Canevas.delete(ennemis[i].box)
                  ennemis.pop(i)

            if i == n-1 :
               Canevas.delete(ennemis[i].box)
               ennemis.pop(i)
               i -= 1
               while ennemis[i].life == 0 :
                  Canevas.delete(ennemis[i].box)
                  ennemis.pop(i)
                  i-=1

            Canevas.delete(Projectile.proj)
            Canevas.delete(Projectile.box)
            ennemis[i].life = 0

   if Projectile.direction == 0 :

      j_co = Canevas.coords(Joueur.box)

      if j_co[1] < proj_co[3] < j_co[3] and (j_co[0] < proj_co[0] < j_co[2] or j_co[0] < proj_co[2] < j_co[2]) :
         pt_vie -=1
         Canevas.delete(Projectile.proj)
         Canevas.delete(Projectile.box)
#         if pt_vie == 0 :
#  FIN DU JEU
         if pt_vie % 2 == 1:
            co = Menu.coords(Vie_full[-1])
            Vie_full.pop(-1)
            Vie_box.append(Menu.create_image(co,anchor = NW, image = img_mi_coeur))
         
         if pt_vie % 2 == 0:
            co = Menu.coords(Vie_box[-1])
            Vie_box.pop(1)
            Vie_box.append(Menu.create_image(co, anchor = NW, image = img_coeur_vide))





         


def deplacement_proj(Projectile):
   if Projectile.direction == 1 :
      proj_x,proj_y = Canevas.coords(Projectile.proj)
      if proj_y < 10:
         Canevas.delete(Projectile)
      Canevas.move(Projectile.proj, 0, -15)
      Canevas.move(Projectile.box, 0, -15)

   if Projectile.direction == 0 :
      proj_x,proj_y = Canevas.coords(Projectile.proj)
      if proj_y > 1000:
         Canevas.delete(Projectile)      
      Canevas.move(Projectile.proj, 0, +15)
      Canevas.move(Projectile.box, 0, +15)
   detection_collision(Projectile)
   Canevas.after(proj_speed,deplacement_proj,Projectile)



def actions_ennemi(ennemi, direction):
   # On choisit la direction vers laquelle le bloc d'ennemi va se déplacer
   # 1 pour la gauche, 0 pour la droite
   n = len(ennemi)

   if direction == 1 : 
   # Déplacement vers la gauche

      if ennemi[0].pos_x -30 < 48 :
      # Si on atteint le bord gauche on descend l'ennemi et 
      # il change de direction vers la droite
         for i in range(n):
            ennemi[i].pos_y += 30
         direction = 0
      
      else : # Sinon on déplace donc l'ennemi vers la gauche 
         for i in range(n):
            ennemi[i].pos_x -= 30


   if direction == 0 :
   # Déplacement vers la droite

      if ennemi[-1].pos_x +30 > 1552 :
      # Si on atteint le bord droite on descend l'ennemi et 
      # il change de direction vers la gauche
         for i in range(n):
            ennemi[i].pos_y += 30
         direction = 1

      else : # Sinon on déplace donc l'ennemi vers la droite
         for i in range(n):
            ennemi[i].pos_x +=30

   # Tir aléatoires
   for i in range(n):
      if ennemis[i].life == 1 :
         k = randrange(50)
         if k == 1 :
            Projectile =  ennemi[i].type_proj(ennemi[i].pos_x, ennemi[i].pos_y+150)
            deplacement_proj(Projectile)

   for i in range(n):
      Canevas.coords(ennemi[i].img, ennemi[i].pos_x-48, ennemi[i].pos_y+10)
      Canevas.coords(ennemi[i].box, ennemi[i].pos_x-48, ennemi[i].pos_y , ennemi[i].pos_x+48, ennemi[i].pos_y+96)
   Canevas.after(ennemi_speed, actions_ennemi, ennemi, direction)



def init_ennemi(n):
   # On crée les n ennemis sur différents emplacements en haut de l'écran
   pos_x = 50
   global ennemis
   ennemis = []
   for i in range(n):
   # On altère entre octorock et moblin, pair octorock, impair moblin

      if i % 2 == 0:
         ennemis.append(octorok(pos_x, 0))
         pos_x+=120


      if i % 2 == 1:
         ennemis.append(moblin(pos_x, 0))
         pos_x+=120
      
   actions_ennemi(ennemis, 0)
         


init_ennemi(nbr_ennemi)





Canevas.focus_set()
Canevas.bind('<Key>',actions_joueur)


invade.mainloop()
