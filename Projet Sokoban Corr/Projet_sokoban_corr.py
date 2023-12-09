from tkinter import *
def sokoban():
    # Création de la fenêtre principale
    Mafenetre = Tk()
    Mafenetre.title('Sokoban')
    Mafenetre.resizable(width=False,height=False)
    Mafenetre.geometry("+0+0")

    #variables globales
    numero_niveau = 1
    fini = False
    nbCoups = 0
    nbCoupsMax = 17
    nbCoupsRecord = 12
    difficulte = 0
    commencerPartie = True

    def setDifficulty(x):
        nonlocal affichageNiveau
        nonlocal difficulte
        difficulte = x
        Canevas.delete(affichageNiveau)
        if x==1:
            affichageNiveau = Canevas.create_text(500,350,fill="darkblue",font="Times 20",text="Difficulté : difficile")
        else:
            affichageNiveau = Canevas.create_text(500,350,fill="darkblue",font="Times 20",text="Difficulté : normale")

    # Création du plateau
    #plateau vide au départ
    def creerPlateau():
        plateau = []
        for i in range(12):
            plateau.append([])
            for j in range(20):
                plateau[i].append([])
                for k in range(9): #vaut 1 à l'indice : 0 pour les murs, 1 pour joueur, 2 pour caisses R, 3 pour les interrupteurs R,
                    # 4 caisses V, 5 interr R, 6 echelle up, 7 echelle down, 8 trou
                    plateau[i][j].append(0)

        #genere les murs pour tous les niveaux
        for i in range(12):
            plateau[i][0][0]=1
            plateau[i][19][0]=1

        for j in range(20):
            plateau[0][j][0]=1
            plateau[11][j][0]=1
        return plateau

    plateauEtage1 = creerPlateau()
    plateauEtage2 = creerPlateau()
    plateauEtage3 = creerPlateau()
    plateauActuel = plateauEtage1

    def init_plateau_vierge(plateau):
        for i in range(1,11):
            for j in range(1,19):
                for k in range(9):
                    plateau[i][j][k]=0

    def genere_niveau_1():
        nonlocal nbCoupsMax, nbCoupsRecord
        nbCoupsMax = 17
        nbCoupsRecord = 12
        #joueur
        plateauActuel[3][3][1]=1
        #caisses
        plateauActuel[5][4][2]=1
        plateauActuel[5][6][2]=1
        #interrupteurs
        plateauActuel[3][8][3]=1
        plateauActuel[5][5][3]=1

    def genere_niveau_2():
        genere_niveau_1()

        nonlocal nbCoupsMax, nbCoupsRecord
        nbCoupsRecord = 18
        nbCoupsMax = 25
        #murs
        plateauActuel[8][8][0]=1
        plateauActuel[7][3][0]=1

        #joueur
        plateauActuel[3][3][1]=0
        plateauActuel[9][9][1]=1

    def genere_niveau_3():
        nonlocal nbCoupsMax, nbCoupsRecord
        nbCoupsMax = 60
        nbCoupsRecord = 43
        #murs
        plateauActuel[7][3][0]=1
        plateauActuel[7][4][0]=1
        plateauActuel[8][5][0]=1
        #joueur
        plateauActuel[9][9][1]=1
        #caisses
        plateauActuel[6][4][2]=1
        plateauActuel[6][5][2]=1
        plateauActuel[5][5][2]=1
        #interrupteurs
        plateauActuel[4][9][3]=1
        plateauActuel[6][9][3]=1
        plateauActuel[7][9][3]=1

    def genere_niveau_4():
        genere_niveau_3()
        nonlocal nbCoupsMax, nbCoupsRecord
        nbCoupsMax = 110
        nbCoupsRecord = 92
        #murs
        plateauActuel[6][2][0]=1
        plateauActuel[5][9][0]=1
        plateauActuel[6][10][0]=1
        plateauActuel[3][14][0]=1
        plateauActuel[3][15][0]=1
        plateauActuel[3][16][0]=1
        plateauActuel[4][13][0]=1
        plateauActuel[4][17][0]=1
        plateauActuel[5][17][0]=1
        plateauActuel[6][16][0]=1
        plateauActuel[7][16][0]=1
        plateauActuel[7][15][0]=1
        plateauActuel[8][14][0]=1
        plateauActuel[7][13][0]=1
        plateauActuel[6][13][0]=1
        #caisses
        plateauActuel[5][3][2]=1
        #interrupteur
        plateauActuel[7][14][3]=1

    def genere_niveau_5():
        genere_niveau_4()
        nonlocal nbCoupsMax, nbCoupsRecord
        nbCoupsMax = 170
        nbCoupsRecord = 154
        #murs
        plateauActuel[7][7][0]=1
        plateauActuel[8][7][0]=1
        plateauActuel[9][8][0]=1
        plateauActuel[5][8][0]=1
        #joueur
        plateauActuel[9][9][1]=0
        plateauActuel[1][1][1]=1
        #caisses
        plateauActuel[7][8][2]=1
        #interrupteurs
        plateauActuel[4][16][3]=1
        plateauActuel[6][15][3]=1
        plateauActuel[7][9][3]=0

    def genere_niveau_6():
        genere_niveau_5()
        nonlocal nbCoupsMax, nbCoupsRecord
        nbCoupsMax = 300
        nbCoupsRecord = 282
        #murs
        plateauActuel[1][7][0]=1
        plateauActuel[2][8][0]=1
        plateauActuel[2][9][0]=1
        plateauActuel[3][11][0]=1
        plateauActuel[4][7][0]=1
        #caisses2
        plateauActuel[2][12][4]=1
        #interrupteurs2
        plateauActuel[2][4][5]=1

    def genere_niveau_7():
        nonlocal nbCoupsMax, nbCoupsRecord
        nbCoupsMax = 250
        nbCoupsRecord = 79
        #joueur
        plateauEtage1[1][1][1]=1
        #interrupteur
        plateauEtage1[3][3][3]=1
        #echelle montante
        plateauEtage1[1][18][6]=1

        #echelle descendante
        plateauEtage2[1][18][7]=1
        #echelle montante
        plateauEtage2[1][17][6]=1
        #trou
        plateauEtage2[5][5][8]=1
        plateauEtage2[9][10][8]=1
        #caisses
        plateauEtage2[7][7][2]=1 #rouge
        plateauEtage2[8][8][4]=1 #verte

        #trou
        plateauEtage3[9][10][8]=1
        #caisses
        plateauEtage3[2][2][2]=1 #R
        plateauEtage3[2][5][4]=1 #V
        #echelle descendante
        plateauEtage3[1][17][7]=1

    def genere_niveau_8():
        nonlocal nbCoupsMax, nbCoupsRecord
        nbCoupsMax = 200
        nbCoupsRecord = 74
        #joueur
        plateauEtage1[3][2][1]=1
        #echelle montante
        plateauEtage1[1][1][6]=1
        plateauEtage1[1][17][6]=1
        #murs
        for i in range(1,11):
            plateauEtage1[i][10][0]=1
        #caisse
        plateauEtage1[5][3][2]=1
        #interrupteur
        plateauEtage1[5][13][3]=1

        #murs
        for i in range(1,11):
            plateauEtage2[i][6][0]=1
        #trou
        plateauEtage2[5][10][8]=1
        #caisse
        plateauEtage2[5][12][4]=1
        #echelle descendante
        plateauEtage2[1][1][7]=1
        plateauEtage2[1][17][7]=1
        #echelle montante
        plateauEtage2[1][2][6]=1
        plateauEtage2[1][18][6]=1

        #echelle descendante
        plateauEtage3[1][2][7]=1
        plateauEtage3[1][18][7]=1

    def genere_niveau_9():
        nonlocal nbCoupsMax, nbCoupsRecord
        nbCoupsMax = 500
        nbCoupsRecord = 500
        #joueur
        plateauEtage1[3][2][1]=1
        #escalier montant
        plateauEtage1[1][1][6]=1
        plateauEtage1[1][18][6]=1
        #interrupteur
        plateauEtage1[8][5][3]=1
        plateauEtage1[3][7][3]=1
        plateauEtage1[3][3][3]=1
        plateauEtage1[5][13][3]=1
        plateauEtage1[7][14][3]=1
        plateauEtage1[9][15][5]=1
        plateauEtage1[1][7][5]=1
        plateauEtage1[7][2][5]=1
        #murs
        plateauEtage1[10][5][0]=1
        plateauEtage1[9][5][0]=1
        plateauEtage1[8][6][0]=1
        plateauEtage1[7][7][0]=1
        plateauEtage1[6][7][0]=1
        plateauEtage1[5][7][0]=1
        plateauEtage1[4][7][0]=1
        plateauEtage1[3][8][0]=1
        plateauEtage1[2][8][0]=1
        plateauEtage1[1][9][0]=1
        plateauEtage1[4][13][0]=1
        plateauEtage1[5][14][0]=1
        plateauEtage1[5][15][0]=1
        plateauEtage1[6][16][0]=1
        plateauEtage1[6][17][0]=1
        plateauEtage1[9][10][0]=1
        plateauEtage1[8][11][0]=1
        plateauEtage1[7][12][0]=1
        plateauEtage1[8][15][0]=1
        plateauEtage1[8][16][0]=1


        #escalier descendant
        plateauEtage2[1][1][7]=1
        plateauEtage2[1][18][7]=1
        #escalier montant
        plateauEtage2[10][1][6]=1
        plateauEtage2[1][4][6]=1
        plateauEtage2[10][12][6]=1
        plateauEtage2[10][18][6]=1
        #murs
        for i in range(4):
            plateauEtage2[1+i][3+i][0]=1
        for i in range(5):
            plateauEtage2[5+i][7][0]=1
            plateauEtage2[i+1][13-i][0]=1
            plateauEtage2[i+6][9+i][0]=1
        plateauEtage2[10][8][0]=1
        #trou
        plateauEtage2[8][14][8]=1
        plateauEtage2[2][7][8]=1
        plateauEtage2[3][6][8]=1
        plateauEtage2[3][4][8]=1
        plateauEtage2[8][5][8]=1
        plateauEtage2[5][13][8]=1
        #caisses
        plateauEtage2[4][15][2]=1
        plateauEtage2[2][10][2]=1
        plateauEtage2[6][8][4]=1


        #escalier descendant
        plateauEtage3[10][1][7]=1
        plateauEtage3[1][4][7]=1
        plateauEtage3[10][12][7]=1
        plateauEtage3[10][18][7]=1
        #murs
        plateauEtage3[10][8][0]=1
        plateauEtage3[9][9][0]=1
        plateauEtage3[8][10][0]=1
        plateauEtage3[7][11][0]=1
        for i in range(4):
            plateauEtage3[7][12+i][0]=1
        plateauEtage3[6][16][0]=1
        plateauEtage3[6][17][0]=1
        plateauEtage3[5][18][0]=1
        #trou
        plateauEtage3[9][10][8]=1
        plateauEtage3[10][9][8]=1
        plateauEtage3[7][16][8]=1
        plateauEtage3[8][14][8]=1
        plateauEtage3[2][7][8]=1
        plateauEtage3[6][10][8]=1
        plateauEtage3[3][12][8]=1
        plateauEtage3[6][8][8]=1
        plateauEtage3[3][4][8]=1
        plateauEtage3[8][5][8]=1
        plateauEtage3[5][13][8]=1
        plateauEtage3[2][16][8]=1
        #caisses
        plateauEtage3[3][10][2]=1
        plateauEtage3[6][5][4]=1
        plateauEtage3[5][3][2]=1
        plateauEtage3[9][4][4]=1
        plateauEtage3[2][4][2]=1


    def genere_niveau_10():
        pass


    #Fonction testant si un niveau est fini
    def test_victoire(plateau):
        for i in range(12):
            for j in range(20):
                if plateau[i][j][3]==1 and plateau[i][j][2]==0:
                    return False
                if plateau[i][j][5]==1 and plateau[i][j][4]==0:
                    return False    #s'il y a au moins un interrupteur sans caisse on n'a pas fini
        return True

    def restartLevel():
        nonlocal plateauActuel, nbCoups
        init_plateau_vierge(plateauEtage1)
        init_plateau_vierge(plateauEtage2)
        init_plateau_vierge(plateauEtage3)
        Canevas.delete("all")
        nbCoups = 0
        if numero_niveau == 1:
            genere_niveau_1()
        elif numero_niveau == 2:
            genere_niveau_2()
        elif numero_niveau == 3:
            genere_niveau_3()
        elif numero_niveau == 4:
            genere_niveau_4()
        elif numero_niveau == 5:
            genere_niveau_5()
        elif numero_niveau == 6:
            genere_niveau_6()
        elif numero_niveau ==7:
            genere_niveau_7()
        elif numero_niveau ==8:
            genere_niveau_8()
        elif numero_niveau ==9:
            genere_niveau_9()
        elif numero_niveau ==10:
            genere_niveau_10()
        elif numero_niveau ==11:
            genere_niveau_11()
        elif numero_niveau ==12:
            genere_niveau_12()
        plateauActuel=plateauEtage1
        affiche_plateau_canvas(plateauEtage1)



    # Création d'un widget Canvas (zone graphique)
    Canevas = Canvas(Mafenetre, width = 1000, height = 600, bg ='grey')
    #Titre
    Canevas.create_text(500,100,fill="darkblue",font="Times 60 italic bold", text="SOKOBAN")

    Canevas.create_text(500,250,fill="darkblue",font="Times 20", text="Poussez les caisses sur les interrupteurs")

    Canevas.create_text(500,300,fill="darkblue",font="Times 20", text="Réglez la difficulté puis appuyez sur une touche pour commencer")

    affichageNiveau = Canevas.create_text(500,350,fill="darkblue",font="Times 20", text="Difficulté : normale")



    def affiche_plateau_canvas(plateau):
        setDifficulty0.destroy()
        setDifficulty1.destroy()
        for i in range(12):
            Canevas.create_line(0,50*i,1000,50*i,width=0.5)
        for j in range(20):
            Canevas.create_line(50*j,0,50*j,600,width=0.5)
        for i in range(12):
            for j in range(20):
                if (plateau[i][j][0]==1):
                    #affichage mur
                    Canevas.create_rectangle(50*j,50*i,50*j+50,50*i+50,fill='blue')
                elif (plateau[i][j][1]==1):
                     #affichage joueur
                    Canevas.create_oval(50*j,50*i,50*j+50,50*i+50,fill='yellow')
                elif (plateau[i][j][2]==1):
                    #affichage caisse
                    Canevas.create_rectangle(50*j,50*i,50*j+50,50*i+50,fill='red')
                elif plateau[i][j][4]==1:
                    #affichage caisse verte
                    Canevas.create_rectangle(50*j,50*i,50*j+50,50*i+50,fill='green')
                elif (plateau[i][j][3]==1):
                    #affichage interrupteur
                    Canevas.create_oval(50*j+10,50*i+10,50*j+40,50*i+40,fill='red')
                elif(plateau[i][j][5]==1):
                    #affichage interrupteur vert
                    Canevas.create_oval(50*j+10,50*i+10,50*j+40,50*i+40,fill='green')
                elif(plateau[i][j][6]==1):
                    #affichage fleche haut
                    Canevas.create_polygon(50*j+25,50*i+5,50*j+40,50*i+20,50*j+30,50*i+20,50*j+30,50*i+45,50*j+20,50*i+45,50*j+20,50*i+20,50*j+10,50*i+20,50*j+25,50*i+5,fill='black')
                elif plateau[i][j][7]==1:
                    #affichage fleche bas
                    Canevas.create_polygon(50*j+20,50*i+5,50*j+30,50*i+5,50*j+30,50*i+30,50*j+40,50*i+30,50*j+25,50*i+45,50*j+10,50*i+30,50*j+20,50*i+30,50*j+20,50*i+5,fill='black')
                elif plateau[i][j][8]==1:
                    Canevas.create_oval(50*j+5,50*i+5,50*j+45,50*i+45,fill='black')

        if numero_niveau >= 7:
            numeroEtage=''
            if plateauActuel==plateauEtage1:
                numeroEtage = '1er Etage'
            elif plateauActuel==plateauEtage2:
                numeroEtage = '2eme Etage'
            elif plateauActuel==plateauEtage3:
                numeroEtage = '3eme Etage'
            Canevas.create_text(500,30,fill="white",font="Times 20",text=numeroEtage)

        if difficulte == 1:
            Canevas.create_text(700,575,fill="white",font="Times 20",text="Nombre de coups pour réussir : "+str(nbCoupsMax))
            Canevas.create_text(830,30,fill="white",font="Times 20",text="Record de coups : "+str(nbCoupsRecord))
            if nbCoups < nbCoupsMax:
                Canevas.create_text(200,575,fill="white",font="Times 20",text="Coups joués : "+str(nbCoups))
            else:
                Canevas.create_text(200,575,fill="red",font="Times 20",text="Coups joués : "+str(nbCoups))

        Canevas.create_text(100,30,fill="white",font="Times 20",text="Niveau "+str(numero_niveau))

        restartButton = Button(master=footer,text="recommencer",command=restartLevel)
        restartButton.grid(row=0,column=1)


    def Clavier(event):
        """ Gestion de l'événement Appui sur une touche du clavier """
        nonlocal numero_niveau, fini, plateauActuel, nbCoups, commencerPartie
        if fini==False: #quand le jeu est fini on ne peut plus se déplacer
            Canevas.delete("all")   #on efface le canevas
            if not commencerPartie:
                if difficulte == 1:
                    nbCoups+=1
                mvt_poss=True
                touche = event.keysym
                for i in range(12):
                    for j in range(20):
                        if (plateauActuel[i][j][1]==1 and mvt_poss ==True ):
                            # déplacement vers le haut
                            #possible si pas de mur dans la case destination ni de caisse suivie d'une caisse, d'un mur ou d'une echelle
                            if touche == 'Up' and plateauActuel[i-1][j][0]==0 and not((plateauActuel [i-1][j][2]==1 or plateauActuel[i-1][j][4]==1) and (plateauActuel[i-2][j][6]==1 or plateauActuel[i-2][j][7]==1 or plateauActuel[i-2][j][2]==1 or plateauActuel[i-2][j][0]==1 or plateauActuel[i-2][j][4]==1)):
                                if plateauActuel[i-1][j][2]==1:
                                    if plateauActuel[i-2][j][8]==1:
                                        if plateauActuel==plateauEtage2:
                                            plateauEtage1[i-2][j][2]=1
                                            plateauEtage1[i-2][j][4]=0
                                            plateauEtage1[i-2][j][0]=0 #On casse ce sur quoi la boite tombe (la boite ou le mur)
                                        elif plateauActuel==plateauEtage3:
                                            if plateauEtage2[i-2][j][8]==1:
                                                plateauEtage1[i-2][j][2]=1
                                                plateauEtage1[i-2][j][0]=0
                                                plateauEtage1[i-2][j][4]=0
                                            else:
                                                plateauEtage2[i-2][j][2]=1
                                                plateauEtage2[i-2][j][0]=0
                                                plateauEtage2[i-2][j][4]=0
                                    else:
                                        plateauActuel[i-2][j][2]=1
                                    plateauActuel[i-1][j][2]=0
                                elif plateauActuel[i-1][j][4]==1:
                                    if plateauActuel[i-2][j][8]==1:
                                        if plateauActuel==plateauEtage2:
                                            plateauEtage1[i-2][j][4]=1
                                            plateauEtage1[i-2][j][0]=0
                                            plateauEtage1[i-2][j][2]=0
                                        elif plateauActuel==plateauEtage3:
                                            if plateauEtage2[i-2][j][8]==1:
                                                plateauEtage1[i-2][j][2]=0
                                                plateauEtage1[i-2][j][0]=0
                                                plateauEtage1[i-2][j][4]=1
                                            else:
                                                plateauEtage2[i-2][j][2]=0
                                                plateauEtage2[i-2][j][0]=0
                                                plateauEtage2[i-2][j][4]=1
                                    else:
                                        plateauActuel[i-2][j][4]=1
                                    plateauActuel[i-1][j][4]=0
                                elif plateauActuel[i-1][j][6]==1:
                                    if plateauActuel==plateauEtage1:
                                        Canevas.delete("all")
                                        plateauActuel[i][j][1]=0
                                        plateauActuel=plateauEtage2
                                    elif plateauActuel==plateauEtage2:
                                        Canevas.delete("all")
                                        plateauActuel[i][j][1]=0
                                        plateauActuel=plateauEtage3
                                elif plateauActuel[i-1][j][7]==1:
                                    if plateauActuel==plateauEtage2:
                                        Canevas.delete("all")
                                        plateauActuel[i][j][1]=0
                                        plateauActuel=plateauEtage1
                                    elif plateauActuel==plateauEtage3:
                                        Canevas.delete("all")
                                        plateauActuel[i][j][1]=0
                                        plateauActuel=plateauEtage2
                                plateauActuel[i][j][1]=0
                                plateauActuel[i-1][j][1]=1
                            elif touche == 'Left' and plateauActuel[i][j-1][0]==0 and not((plateauActuel [i][j-1][2]==1 or plateauActuel[i][j-1][4]==1) and (plateauActuel[i][j-2][7]==1 or plateauActuel[i][j-2][6]==1 or plateauActuel[i][j-2][2]==1 or plateauActuel[i][j-2][0]==1 or plateauActuel[i][j-2][4]==1)):
                                if plateauActuel[i][j-1][2]==1:
                                    if plateauActuel[i][j-2][8]==1:
                                        if plateauActuel==plateauEtage2:
                                            plateauEtage1[i][j-2][2]=1
                                            plateauEtage1[i][j-2][0]=0
                                            plateauEtage1[i][j-2][4]=0
                                        elif plateauActuel==plateauEtage3:
                                            if plateauEtage2[i][j-2][8]==1:
                                                plateauEtage1[i][j-2][2]=1
                                                plateauEtage1[i][j-2][0]=0
                                                plateauEtage1[i][j-2][4]=0
                                            else:
                                                plateauEtage2[i][j-2][2]=1
                                                plateauEtage2[i][j-2][0]=0
                                                plateauEtage2[i][j-2][4]=0
                                    else:
                                        plateauActuel[i][j-2][2]=1
                                    plateauActuel[i][j-1][2]=0
                                elif plateauActuel[i][j-1][4]==1:
                                    if plateauActuel[i][j-2][8]==1:
                                        if plateauActuel==plateauEtage2:
                                            plateauEtage1[i][j-2][4]=1
                                            plateauEtage1[i][j-2][0]=0
                                            plateauEtage1[i][j-2][2]=0
                                        elif plateauActuel==plateauEtage3:
                                            if plateauEtage2[i][j-2][8]==1:
                                                plateauEtage1[i][j-2][2]=0
                                                plateauEtage1[i][j-2][0]=0
                                                plateauEtage1[i][j-2][4]=1
                                            else:
                                                plateauEtage2[i][j-2][2]=0
                                                plateauEtage2[i][j-2][0]=0
                                                plateauEtage2[i][j-2][4]=1
                                    else:
                                        plateauActuel[i][j-2][4]=1
                                    plateauActuel[i][j-1][4]=0
                                elif plateauActuel[i][j-1][6]==1:
                                    if plateauActuel==plateauEtage1:
                                        Canevas.delete("all")
                                        plateauActuel[i][j][1]=0
                                        plateauActuel=plateauEtage2
                                    elif plateauActuel==plateauEtage2:
                                        Canevas.delete("all")
                                        plateauActuel[i][j][1]=0
                                        plateauActuel=plateauEtage3
                                elif plateauActuel[i][j-1][7]==1:
                                    if plateauActuel==plateauEtage2:
                                        Canevas.delete("all")
                                        plateauActuel[i][j][1]=0
                                        plateauActuel=plateauEtage1
                                    elif plateauActuel==plateauEtage3:
                                        Canevas.delete("all")
                                        plateauActuel[i][j][1]=0
                                        plateauActuel=plateauEtage2
                                plateauActuel[i][j][1]=0
                                plateauActuel[i][j-1][1]=1
                            elif touche == 'Right' and plateauActuel[i][j+1][0]==0 and not((plateauActuel [i][j+1][2]==1 or plateauActuel[i][j+1][4]==1) and (plateauActuel[i][j+2][6]==1 or plateauActuel[i][j+2][7]==1 or plateauActuel[i][j+2][2]==1 or plateauActuel[i][j+2][0]==1 or plateauActuel[i][j+2][4]==1)):
                                if plateauActuel[i][j+1][2]==1:
                                    if plateauActuel[i][j+2][8]==1:
                                        if plateauActuel==plateauEtage2:
                                            plateauEtage1[i][j+2][2]=1
                                            plateauEtage1[i][j+2][0]=0
                                            plateauEtage1[i][j+2][4]=0
                                        elif plateauActuel==plateauEtage3:
                                            if plateauEtage2[i][j+2][8]==1:
                                                plateauEtage1[i][j+2][2]=1
                                                plateauEtage1[i][j+2][0]=0
                                                plateauEtage1[i][j+2][4]=0
                                            else:
                                                plateauEtage2[i][j+2][2]=1
                                                plateauEtage2[i][j+2][0]=0
                                                plateauEtage2[i][j+2][4]=0
                                    else:
                                        plateauActuel[i][j+2][2]=1
                                    plateauActuel[i][j+1][2]=0
                                elif plateauActuel[i][j+1][4]==1:
                                    if plateauActuel[i][j+2][8]==1:
                                        if plateauActuel==plateauEtage2:
                                            plateauEtage1[i][j+2][4]=1
                                            plateauEtage1[i][j+2][0]=0
                                            plateauEtage1[i][j+2][2]=0
                                        elif plateauActuel==plateauEtage3:
                                            if plateauEtage2[i][j+2][8]==1:
                                                plateauEtage1[i][j+2][2]=0
                                                plateauEtage1[i][j+2][0]=0
                                                plateauEtage1[i][j+2][4]=1
                                            else:
                                                plateauEtage2[i][j+2][2]=0
                                                plateauEtage2[i][j+2][0]=0
                                                plateauEtage2[i][j+2][4]=1
                                    else:
                                        plateauActuel[i][j+2][4]=1
                                    plateauActuel[i][j+1][4]=0
                                elif plateauActuel[i][j+1][6]==1:
                                    if plateauActuel==plateauEtage1:
                                        Canevas.delete("all")
                                        plateauActuel[i][j][1]=0
                                        plateauActuel=plateauEtage2
                                    elif plateauActuel==plateauEtage2:
                                        Canevas.delete("all")
                                        plateauActuel[i][j][1]=0
                                        plateauActuel=plateauEtage3
                                elif plateauActuel[i][j+1][7]==1:
                                    if plateauActuel==plateauEtage2:
                                        Canevas.delete("all")
                                        plateauActuel[i][j][1]=0
                                        plateauActuel=plateauEtage1
                                    elif plateauActuel==plateauEtage3:
                                        Canevas.delete("all")
                                        plateauActuel[i][j][1]=0
                                        plateauActuel=plateauEtage2
                                plateauActuel[i][j][1]=0
                                plateauActuel[i][j+1][1]=1
                            elif touche == 'Down' and plateauActuel[i+1][j][0]==0 and not((plateauActuel [i+1][j][2]==1 or plateauActuel[i+1][j][4]==1) and (plateauActuel[i+2][j][6]==1 or plateauActuel[i+2][j][7]==1 or plateauActuel[i+2][j][2]==1 or plateauActuel[i+2][j][0]==1 or plateauActuel[i+2][j][4]==1)):
                                if plateauActuel[i+1][j][2]==1:
                                    if plateauActuel[i+2][j][8]==1:
                                        if plateauActuel==plateauEtage2:
                                            plateauEtage1[i+2][j][2]=1
                                            plateauEtage1[i+2][j][0]=0
                                            plateauEtage1[i+2][j][4]=0
                                        elif plateauActuel==plateauEtage3:
                                            if plateauEtage2[i+2][j][8]==1:
                                                plateauEtage1[i+2][j][2]=1
                                                plateauEtage1[i+2][j][0]=0
                                                plateauEtage1[i+2][j][4]=0
                                            else:
                                                plateauEtage2[i+2][j][2]=1
                                                plateauEtage2[i+2][j][0]=0
                                                plateauEtage2[i+2][j][4]=0
                                    else:
                                        plateauActuel[i+2][j][2]=1
                                    plateauActuel[i+1][j][2]=0
                                elif plateauActuel[i+1][j][4]==1:
                                    if plateauActuel[i+2][j][8]==1:
                                        if plateauActuel==plateauEtage2:
                                            plateauEtage1[i+2][j][4]=1
                                            plateauEtage1[i+2][j][0]=0
                                            plateauEtage1[i+2][j][2]=0
                                        elif plateauActuel==plateauEtage3:
                                            if plateauEtage2[i+2][j][8]==1:
                                                plateauEtage1[i+2][j][2]=0
                                                plateauEtage1[i+2][j][0]=0
                                                plateauEtage1[i+2][j][4]=1
                                            else:
                                                plateauEtage2[i+2][j][2]=0
                                                plateauEtage2[i+2][j][0]=0
                                                plateauEtage2[i+2][j][4]=1
                                    else:
                                        plateauActuel[i+2][j][4]=1
                                    plateauActuel[i+1][j][4]=0
                                elif plateauActuel[i+1][j][6]==1:
                                    if plateauActuel==plateauEtage1:
                                        Canevas.delete("all")
                                        plateauActuel[i][j][1]=0
                                        plateauActuel=plateauEtage2
                                    elif plateauActuel==plateauEtage2:
                                        Canevas.delete("all")
                                        plateauActuel[i][j][1]=0
                                        plateauActuel=plateauEtage3
                                elif plateauActuel[i+1][j][7]==1:
                                    if plateauActuel==plateauEtage2:
                                        Canevas.delete("all")
                                        plateauActuel[i][j][1]=0
                                        plateauActuel=plateauEtage1
                                    elif plateauActuel==plateauEtage3:
                                        Canevas.delete("all")
                                        plateauActuel[i][j][1]=0
                                        plateauActuel=plateauEtage2
                                plateauActuel[i][j][1]=0
                                plateauActuel[i+1][j][1]=1
                            mvt_poss=False #pour ne pas se déplacer de plusieurs cases à la fois
                #le cas échéant on change de niveau :
                if (test_victoire(plateauEtage1) and test_victoire(plateauEtage2) and test_victoire(plateauEtage3)):
                    if nbCoups<=nbCoupsMax:
                        numero_niveau=numero_niveau+1
                    nbCoups=0
                    if numero_niveau==1:
                        init_plateau_vierge(plateauEtage1)
                        init_plateau_vierge(plateauEtage2)
                        init_plateau_vierge(plateauEtage3)
                        genere_niveau_1()
                    if numero_niveau==2:
                        init_plateau_vierge(plateauEtage1)
                        init_plateau_vierge(plateauEtage2)
                        init_plateau_vierge(plateauEtage3)
                        genere_niveau_2()
                    if numero_niveau==3:
                        init_plateau_vierge(plateauEtage1)
                        init_plateau_vierge(plateauEtage2)
                        init_plateau_vierge(plateauEtage3)
                        genere_niveau_3()
                    if numero_niveau == 4:
                        init_plateau_vierge(plateauEtage1)
                        init_plateau_vierge(plateauEtage2)
                        init_plateau_vierge(plateauEtage3)
                        genere_niveau_4()
                    if numero_niveau == 5:
                        init_plateau_vierge(plateauEtage1)
                        init_plateau_vierge(plateauEtage2)
                        init_plateau_vierge(plateauEtage3)
                        genere_niveau_5()
                    if numero_niveau == 6:
                        init_plateau_vierge(plateauEtage1)
                        init_plateau_vierge(plateauEtage2)
                        init_plateau_vierge(plateauEtage3)
                        genere_niveau_6()
                    if numero_niveau == 7:
                        init_plateau_vierge(plateauEtage1)
                        init_plateau_vierge(plateauEtage2)
                        init_plateau_vierge(plateauEtage3)
                        genere_niveau_7()
                    if numero_niveau == 8:
                        init_plateau_vierge(plateauEtage1)
                        init_plateau_vierge(plateauEtage2)
                        init_plateau_vierge(plateauEtage3)
                        genere_niveau_8()
                    if numero_niveau == 9:
                        init_plateau_vierge(plateauEtage1)
                        init_plateau_vierge(plateauEtage2)
                        init_plateau_vierge(plateauEtage3)
                        genere_niveau_9()
                    if numero_niveau == 10:
                        init_plateau_vierge(plateauEtage1)
                        init_plateau_vierge(plateauEtage2)
                        init_plateau_vierge(plateauEtage3)
                        genere_niveau_10()
                        Canevas.create_text(500,300,fill="darkblue",font="Times 60 italic bold",text="BRAVO !!!")
                        fini=True #bloque les commandes
            #on raffiche le canevas
            commencerPartie = False
            affiche_plateau_canvas(plateauActuel)



    genere_niveau_1()

    Canevas.focus_set()
    Canevas.bind('<Key>',Clavier)
    Canevas.grid(row=0,column=0)

    footer = Frame(master=Mafenetre)
    footer.grid(row=1,column=0)

    setDifficulty0 = Button(master=footer, text="Mode normal",command=lambda:setDifficulty(0))
    setDifficulty1 = Button(master=footer, text="Mode difficile",command=lambda:setDifficulty(1))
    setDifficulty0.grid(row=0,column=1)
    setDifficulty1.grid(row=0,column=2)
    # Création d'un widget Button (bouton Quitter)
    BoutonQuitter=Button(footer, text ='Quitter', command = Mafenetre.destroy)
    BoutonQuitter.grid(row=0,column=0)

    #boucle principale
    Mafenetre.mainloop()
sokoban()