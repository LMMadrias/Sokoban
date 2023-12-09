from tkinter import *

# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('Sokoban')

#variables globales
numero_niveau=0
fini=False

# Création du plateau
#plateau vide au départ
plateau = []
for i in range(12):
    plateau.append([])
    for j in range(16):
        plateau[i].append([])
        for k in range(4):
            (plateau[i][j]).append(0)

#niveau 1
#murs
for i in range(12):
    plateau[i][0][0]=1
    plateau[i][1][0]=1
    plateau[i][14][0]=1
    plateau[i][15][0]=1

for j in range(16):
    plateau[0][j][0]=1
    plateau[1][j][0]=1
    plateau[10][j][0]=1
    plateau[11][j][0]=1

#joueur
plateau[3][3][1]=1
#caisses
plateau[5][4][2]=1
plateau[5][6][2]=1
#interrupteurs
plateau[3][8][3]=1
plateau[5][5][3]=1

#Fonctions, appelées au bon moment, pour les niveaux suivants
def genere_niveau_2():
    #on efface le plateau
    for i in range(2,10):
        for j in range(2,14):
            plateau[i][j][0]=0
            plateau[i][j][1]=0
            plateau[i][j][2]=0
            plateau[i][j][3]=0
    #on crée un nouveau plateau
    #murs
    plateau[8][8][0]=1
    plateau[7][3][0]=1
    #joueur
    plateau[9][9][1]=1
    #caisses
    plateau[5][4][2]=1
    plateau[5][6][2]=1
    #interrupteurs
    plateau[3][8][3]=1
    plateau[5][5][3]=1

def genere_niveau_3():
    for i in range(2,10):
        for j in range(2,14):
            plateau[i][j][0]=0
            plateau[i][j][1]=0
            plateau[i][j][2]=0
            plateau[i][j][3]=0

#Fonction testant si un niveau est fini
def test_victoire():
    for i in range(12):
        for j in range(16):
            if plateau[i][j][3]==1 and plateau[i][j][2]==0:
                return False
                #s'il y a au moins un interrupteur sans caisse on n'a pas fini
    return True

# Création d'un widget Canvas (zone graphique)
Largeur = 800
Hauteur = 600
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='grey')
#Titre
Canevas.create_text(400,100,fill="darkblue",font="Times 60 italic bold",
                        text="SOKOBAN")

Canevas.create_text(400,250,fill="darkblue",font="Times 20",
                        text="Poussez les caisses sur les interrupteurs")

Canevas.create_text(400,300,fill="darkblue",font="Times 20",
                        text="Appuyez sur une touche pour commencer")

def affiche_plateau_canvas():
    for i in range(12):
        Canevas.create_line(0,50*i,800,50*i,width=0.5)
    for j in range(16):
        Canevas.create_line(50*j,0,50*j,600,width=0.5)
    for i in range(12):
        print()
        for j in range(16):
            if (plateau[i][j][0]==1):
                #affichage mur
                Canevas.create_rectangle(50*j,50*i,50*j+50,50*i+50,fill='blue')

            elif (plateau[i][j][1]==1):
                 #affichage joueur
                Canevas.create_oval(50*j,50*i,50*j+50,50*i+50,fill='yellow')
            elif (plateau[i][j][2]==1):
                #affichage caisse
                Canevas.create_rectangle(50*j,50*i,50*j+50,50*i+50,fill='red')
            elif (plateau[i][j][3]==1):
                #affichage interrupteur
                Canevas.create_oval(50*j+10,50*i+10,50*j+40,50*i+40,fill='red')

def Clavier(event):
    global numero_niveau
    global fini
    """ Gestion de l'événement Appui sur une touche du clavier """
    if fini==False: #quand le jeu est fini on ne peut plus se déplacer
        #on efface le canevas
        Canevas.delete("all")
        mvt_poss=True
        touche = event.keysym
        for i in range(12):
            for j in range(16):
                if (plateau[i][j][1]==1 and mvt_poss ==True ):
                    # déplacement vers le haut
                    #possible si pas de mur dans la case destination ni de caisse suivie d'une caisse ou d'un mur
                    if touche == 'Up' and plateau[i-1][j][0]!=1 and not(plateau [i-1][j][2]==1 and (plateau[i-2][j][2]==1 or plateau[i-2][j][0]==1)):
                        if plateau[i-1][j][2]==1:
                            plateau[i-2][j][2]=1
                            plateau[i-1][j][2]=0
                        plateau[i][j][1]=0
                        plateau[i-1][j][1]=1
                    elif touche == 'Left' and plateau[i][j-1][0]!=1 and not(plateau [i][j-1][2]==1 and (plateau[i][j-2][2]==1 or plateau[i][j-2][0]==1)):
                        if plateau[i][j-1][2]==1:
                            plateau[i][j-2][2]=1
                            plateau[i][j-1][2]=0
                        plateau[i][j][1]=0
                        plateau[i][j-1][1]=1
                    elif touche == 'Right' and plateau[i][j+1][0]!=1 and not(plateau [i][j+1][2]==1 and (plateau[i][j+2][2]==1 or plateau[i][j+2][0]==1)):
                        if plateau[i][j+1][2]==1:
                            plateau[i][j+2][2]=1
                            plateau[i][j+1][2]=0
                        plateau[i][j][1]=0
                        plateau[i][j+1][1]=1
                    elif touche == 'Down' and plateau[i+1][j][0]!=1 and not(plateau [i+1][j][2]==1 and (plateau[i+2][j][2]==1 or plateau[i+2][j][0]==1)):
                        if plateau[i+1][j][2]==1:
                            plateau[i+2][j][2]=1
                            plateau[i+1][j][2]=0
                        plateau[i][j][1]=0
                        plateau[i+1][j][1]=1
                    mvt_poss=False #pour ne pas se déplacer de plusieurs cases à la fois
        #le cas échéant on change de niveau :
        if (test_victoire()==True):
            numero_niveau=numero_niveau+1
            if numero_niveau==1:
                genere_niveau_2()
            if numero_niveau==2:
                genere_niveau_3()
                Canevas.create_text(400,300,fill="darkblue",font="Times 60 italic bold",text="BRAVO !!!")
                fini=True #bloque les commandes
        #on raffiche le canevas
        affiche_plateau_canvas()

Canevas.focus_set()
Canevas.bind('<Key>',Clavier)
Canevas.grid(row=0,column=0)

# Création d'un widget Button (bouton Quitter)
BoutonQuitter=Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy)
BoutonQuitter.grid(row=1,column=0)

#boucle principale
Mafenetre.mainloop()