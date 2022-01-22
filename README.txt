HYRULE INVADERS par Michel COURBIN et Thomas DERVILLE


Bienvenue dans le Royaume de Hyrule.

De nombreux monstres sont apparus et sème le désespoir dans ce monde depuis l'avènement du Roi des Voleurs Ganon.
Mais heureusement le jeune élu de la déesse Hylia, Link, est là pour se battre et protéger le Royaume de Hyrule de toutes ces menaces.


Les règles du jeu : 

Vous incarnez le héros Link et vous devez survivre le plus longtemps possible à l'assaut incessant des monstres.
Vous pouvez vous déplacer à droite, à gauche et tirer avec votre épée pour éliminer vos ennemis.
Les monstres arrivent par vagues et sont de plus en plus rapides et agressifs.
Toutes les 3 vagues Ganon viendra vous affronter.
Les monstres peuvent tirer des projectiles et s'ils vous touchent vous perdrez 1 point de vie.

Vous disposez de buissons pour vous protéger, cependant ils disparaitront si les montres s'en approchent trop ou
s'ils reçoivent trop de projectiles de la part des ennemis ou de la vôtre.

Si vos points de vie tombent à 0, vous avez perdu.
Si les monstres arrivent en bas de l'écran, vous avez perdu.

ATTENTION : Vous ne disposez que de 5 coeurs (10 points de vie).



Commandes :

Aller à droite : Flèche de droite ou D

Aller à gauche : Flèche de gauche ou Q

Tirer : Flèche du haut ou Espace



Implémentations des structures demandées : 

Pile : Une pile est utilisée dans la barre de coeurs entiers. On dépile un coeur entier tout les deux points de vie perdus (un point de vie = un demi coeur).
(voir vie_full dans init_game où la pile est créée ligne 251 et dans detection_collision où on dépile tout les deux coeurs ligne 588)

Liste : La liste est utilisée pour le bloc des ennemis et ainsi avoir une entité qui regroupe chacun des ennemis.
(voir ennemis dans init_ennemi lignes 316 et 321 et dans init_ganon ligne 332) 


Lien du GitHub utilisé : https://github.com/Carnaly/Hyrule-Invaders-COURBIN-DERVILLE


