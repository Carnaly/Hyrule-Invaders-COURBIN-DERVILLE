#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Que fait ce programme : 

Qui l'a fait : Michel COURBIN, Thomas DERVILLE

Créé le [date] à [heure]

Que reste-t-il à faire ?
[tout doux liste]
"""



from cgitb import text
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
# img_go = PhotoImage(file="GameOver.png") # Image du Game Over


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

img_buis = PhotoImage(file='Buisson.png') # Image bloc



# Création des variables globales du jeu

global ennemi_speed, proj_speed, nbr_ennemi, pt_vie, Joueur, difficulty, score, vague, blocs, Canevas, Fin
score = 0
ennemi_speed = 600 
proj_speed = 200 
nbr_ennemi = 8 
pt_vie = 2
vague = 1
blocs = []

########################################### CLASSES ############################################


# Classe du joueur
class link:

   def __init__(self): # ptet rajouter difficulté mdr

      self.pos_x = 800
      self.pos_y = 900
      self.box = Canevas.create_rectangle(self.pos_x-36, self.pos_y, self.pos_x+38, self.pos_y+96)
      self.Link = Canevas.create_image(self.pos_x-40, self.pos_y , anchor=NW, image = img_joueur)




# Classes des ennemis
class enemy:
   # Création de la classe des ennemis, on leur attribue un nom une vitesse de mouvement et des points de vies
   def __init__(self,  pos_x, pos_y, life_point, type_projectile, points):

      self.pos_x = pos_x
      self.pos_y = pos_y
      self.life = life_point
      self.type_proj = type_projectile
      self.points = points


class octorok(enemy):

   def __init__(self, pos_x, pos_y):

      enemy.__init__(self, pos_x, pos_y, 1, proj_octo,50)

      self.box = Canevas.create_rectangle(self.pos_x-48, self.pos_y, self.pos_x+48, self.pos_y+96,fill='white')
      self.img = Canevas.create_image(self.pos_x-48, self.pos_y , anchor=NW, image = img_octo)



class moblin(enemy):

   def __init__(self, pos_x, pos_y):

      enemy.__init__(self, pos_x, pos_y, 1, proj_mob,50)

      self.box = Canevas.create_rectangle(self.pos_x-48, self.pos_y, self.pos_x+48, self.pos_y+96,fill='white')
      self.img = Canevas.create_image(self.pos_x-48, self.pos_y , anchor=NW, image = img_moblin)

class buisson(enemy):

   def __init__(self, pos_x, pos_y):

      enemy.__init__(self,pos_x, pos_y, 3, None, 0)

      self.box = Canevas.create_rectangle(self.pos_x-48, self.pos_y, self.pos_x+16, self.pos_y+64,fill='white')
      self.img = Canevas.create_image(self.pos_x-48, self.pos_y , anchor=NW, image = img_buis)


# Ennemi Spécial
class ganon(enemy):

   def __init__(self, pos_x, pos_y):

      enemy.__init__(self, pos_x, pos_y, 4, proj_ganon, 1000)

      self.box = Canevas.create_rectangle(self.pos_x-48, self.pos_y, self.pos_x+48, self.pos_y+96)
      self.img = Canevas.create_image(self.pos_x-48, self.pos_y , anchor=NW, image = img_ganon)



# Classe des projectiles

class projectile:

   def __init__(self, pos_x, pos_y, mvt_direction, life):

      self.pos_x = pos_x
      self.pos_y = pos_y
      self.direction = mvt_direction
      self.life = life


class proj_link(projectile):

   def __init__(self, pos_x, pos_y):

      projectile.__init__(self, pos_x, pos_y, 1,1)

      self.box = Canevas.create_rectangle(self.pos_x-16, self.pos_y-32, self.pos_x+16, self.pos_y+32) 
      self.proj = Canevas.create_image(self.pos_x, self.pos_y, image=img_proj_joueur)

class proj_octo(projectile):

   def __init__(self, pos_x, pos_y):

      projectile.__init__(self, pos_x, pos_y, 0,1)

      self.box = Canevas.create_rectangle(self.pos_x-16, self.pos_y-16, self.pos_x+16, self.pos_y+16)
      self.proj = Canevas.create_image(self.pos_x, self.pos_y, image=img_proj_octo)
      

class proj_mob(projectile):

   def __init__(self, pos_x, pos_y):

      projectile.__init__(self, pos_x, pos_y, 0,1)

      self.box = Canevas.create_rectangle(self.pos_x-10, self.pos_y-32, self.pos_x+10, self.pos_y+32)
      self.proj = Canevas.create_image(self.pos_x, self.pos_y, image=img_proj_mob)



class proj_ganon(projectile):

   def __init__(self, pos_x, pos_y):

      projectile.__init__(self, pos_x, pos_y, 0,1)

      self.proj = Canevas.create_image(self.pos_x, self.pos_y, image=img_proj_joueur) #image=img_proj_ganon) # à remplacer par image proj ganon
      self.box = Canevas.create_rectangle(self.pos_x-16, self.pos_y-32, self.pos_x+16, self.pos_y+32) # à remplacer par dimension proj ganon


def restart_game():

   start_game()


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
Score= Label(invade, text='Score')



#bouton quitter
Quit = Button(invade, text = 'Quitter', command = invade.destroy)
Quit.place(in_=Menu, x=100, y= 400)



#bouton nouvelle partie
New= Button(invade, text='Nouvelle Partie', command=restart_game)
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



# Création du joueur

Joueur = link()



########################################## FONCTIONS ###########################################

def start_game():
   # Initialisation des ennemis
   score = 0
   ennemi_speed = 200 
   proj_speed = 100 
   nbr_ennemi = 8 
   pt_vie = 10
   vague = 1
   blocs = []
   score_maj()
   init_ennemi(nbr_ennemi)
   init_bloc()
   Start.destroy()
   Quit.destroy()
   Infos.destroy()
   Titre.destroy()


def end_game():
   # Fonction de fin de partie


   # On détruit le canvas de jeu (fo ptet pa)

   Canevas.destroy()


   # On crée l'écran de fin

   Fin = Canvas(invade, width=1920, height=1080, bg='black')
   Fin.place(x=0, y=0)
   
   # GAME OVER

   Fin.create_image(400,400, image = img_buis)

   #Zone de Score

   Score= Label(Fin, text = 'Score : ' + str(score))
   Score.config(font=('Courier',16))
   Score.place(relx=0.5, rely=0.6, anchor=CENTER)


   # Bouton début du jeu

   Start = Button(Fin, text = 'Recommencer', command = start_game)
   Start.place(relx=0.5, rely=0.7, anchor=CENTER)

   # Bouton retour titre

   Return = Button(Fin, text = 'Écran titre' ) #, command = titre)
   Return.place(relx=0.5, rely=0.75, anchor=CENTER)

   # Bouton Quitter

   Quit = Button(Fin, text = 'Quitter', command = invade.destroy)
   Quit.place(relx=0.5, rely=0.8, anchor=CENTER)



#def void():



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
      Projectile =  proj_link(Joueur.pos_x, Joueur.pos_y-80)
      deplacement_proj(Projectile)
      # ptet rajouter du délai ptdr

   # Pause
   if touche == 'Return' or 'Escape' :
      print('Pause')



def detection_collision(Projectile):
   global pt_vie, score, blocs
   proj_co = Canevas.coords(Projectile.box)
   
   if Projectile.direction == 1 :

      n = len(ennemis)

      for i in range(n):
         if ennemis[i].life == 1 :
            en_co = Canevas.coords(ennemis[i].box)

            if en_co[1] < proj_co[1] < en_co[3] and (en_co[0] < proj_co[0] < en_co[2] or en_co[0] < proj_co[2] < en_co[2]) :
               
               Canevas.delete(ennemis[i].img)
               ennemis[i].life = 0
               score += ennemis[i].points
               score_maj()
               Projectile.life = 0
               Canevas.delete(Projectile.proj)
               Canevas.delete(Projectile.box)
               if n == 1:
                  Canevas.delete(ennemis[i].box)
                  ennemis.pop(i)
                  maj_vague()

               else :

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

   if Projectile.direction == 0 :

      j_co = Canevas.coords(Joueur.box)

      if j_co[1] < proj_co[3] < j_co[3] and (j_co[0] < proj_co[0] < j_co[2] or j_co[0] < proj_co[2] < j_co[2]) :
         pt_vie -=1
         Projectile.life = 0
         Canevas.delete(Projectile.proj)
         Canevas.delete(Projectile.box)
         if pt_vie == 0 :
            end_game()

         if pt_vie % 2 == 1:
            co = Menu.coords(Vie_full[-1])
            Vie_full.pop(-1)
            Vie_box.append(Menu.create_image(co,anchor = NW, image = img_mi_coeur))
         
         if pt_vie % 2 == 0:
            co = Menu.coords(Vie_box[-1])
            Vie_box.pop(1)
            Vie_box.append(Menu.create_image(co, anchor = NW, image = img_coeur_vide))

   m = len(blocs)
   for i in range(m):
      buiss_co = Canevas.coords(blocs[i].box)
      if (buiss_co[0] < proj_co[0] < buiss_co[2] or buiss_co[0] < proj_co[2] < buiss_co[2]) and (buiss_co[1] < proj_co[1] < buiss_co[3] or buiss_co[1] < proj_co[3] < buiss_co[3]) :
         
         if blocs[i].life == 1:
            Canevas.delete(blocs[i].img)
            blocs[i].life = 0            
            Canevas.delete(blocs[i].box)
            blocs.pop(i)

         else:
            blocs[i].life -= 1

         Projectile.life = 0
         Canevas.delete(Projectile.proj)
         Canevas.delete(Projectile.box)


   if Projectile.life == 1 :
      Canevas.after(proj_speed,deplacement_proj,Projectile)


         

def score_maj():
   Score = Label(Menu, text =('Score : ' + str(score)))
   print(score)
   Score.config(font=('Courier', 12))
   Score.place (in_=Menu, x=10, y = 250)


def maj_vague():
   # On met à jour le numéro de la vague d'ennemis
   global vague, ennemi_speed, proj_speed, nbr_ennemi
   vague += 1

   if vague == -1 :
      # Toutes les 3 vagues Ganon apparait
      print('Ganon')
   
   else :
      # On change les variables globales responsables 
      # de la vitesse des ennemis et des projectiles
      if proj_speed == 50 :
         if ennemi_speed == 60:
            init_ennemi(nbr_ennemi)
         
         else :
            ennemi_speed -= 20
            init_ennemi(nbr_ennemi)

      else :
         ennemi_speed -= 20
         proj_speed -= 10
         init_ennemi(nbr_ennemi)
      print(ennemi_speed,proj_speed)
      
      



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



def actions_ennemi(ennemi, direction):
   # On choisit la direction vers laquelle le bloc d'ennemi va se déplacer
   # 1 pour la gauche, 0 pour la droite
   n = len(ennemi)

   if direction == 1 : 
   # Déplacement vers la gauche
      
      if ennemi[0].pos_x -30 < 48 :
      # Si on atteint le bord gauche on descend l'ennemi et 
      # il change de direction vers la droite

         if n == 1 :
            ennemi[0].pos_y += 30

         else :   
            for i in range(n):
               ennemi[i].pos_y += 30
         direction = 0

      
      else : # Sinon on déplace donc l'ennemi vers la gauche 
         if n == 1 :
            ennemi[0].pos_x -= 30
         
         else :
            for i in range(n):
               ennemi[i].pos_x -= 30


   if direction == 0 :
   # Déplacement vers la droite

      if ennemi[-1].pos_x +30 > 1552 :
      # Si on atteint le bord droite on descend l'ennemi et 
      # il change de direction vers la gauche
         if n == 1 :
            ennemi[0].pos_y += 30

         else :   
            for i in range(n):
               ennemi[i].pos_y += 30
         direction = 1

      
      else : # Sinon on déplace donc l'ennemi vers la droite 
         if n == 1 :
            ennemi[0].pos_x += 30
         
         else :
            for i in range(n):
               ennemi[i].pos_x += 30

   # Tir aléatoires
   if n == 1 :

      k = randrange(40)
      if k == 1 :
         Projectile =  ennemi[0].type_proj(ennemi[0].pos_x, ennemi[0].pos_y+150)
         deplacement_proj(Projectile)
      Canevas.coords(ennemi[0].img, ennemi[0].pos_x-48, ennemi[0].pos_y+10)
      Canevas.coords(ennemi[0].box, ennemi[0].pos_x-48, ennemi[0].pos_y , ennemi[0].pos_x+48, ennemi[0].pos_y+96)


   else :
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



Titre = Canvas(invade, width=1920, height=1080, bg='black')
Titre.place(x=0, y=0)

# Image de fond

#Titre.create_image(0,0, anchor = NW, image = img_fond)

# Logo du jeu

Titre.create_image(500,0,anchor=NW, image = img_titre)


# Bouton début du jeu
Start = Button(invade, text = 'Commencer',font = (16), command = start_game)
Start.place(relx=0.5, rely=0.7, anchor=CENTER)



# Bouton A Propos

Infos = Button(invade, text = 'Informations', font = (16), command = informations)
Infos.place(relx=0.5, rely=0.75, anchor=CENTER)


# Bouton Quitter

Quit = Button(invade, text = 'Quitter', font = (16), command = invade.destroy)
Quit.place(relx=0.5, rely=0.8, anchor=CENTER)

Canevas.focus_set()
Canevas.bind('<Key>',actions_joueur)

invade.mainloop()
