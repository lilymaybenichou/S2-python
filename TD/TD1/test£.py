#! /usr/bin/env python
# -*- coding:Utf8 -*-

                ###########################################
                #                                         #
                #                 Sudoku                  #
                #                   de                    #
                #               Guillaume D               #
                #                                         #
                #                                         #
                #                                         #
                ###########################################

from Tkinter import *
import tkFileDialog
import tkMessageBox
import tkSimpleDialog

# -------------- Declaration de variables global ------------------------

c=70
nb=9
x0,y0=70,70
c1=210
nb1=3
nombreEntre=10
couleur='black'
typeJeu=0

listeGrille=['ligne1','ligne2','ligne3','ligne4','ligne5','ligne6','ligne7',
       'ligne8','ligne9','colone1','colone2','colone3','colone4',
       'colone5','colone6','colone7','colone8','colone9','carre1',
       'carre2','carre3','carre4','carre5','carre6','carre7','carre8','carre9']

grilleSudo=[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

bloqueSudo=[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

grilleFacile=[[0, 1, 9, 0, 3, 0, 2, 6, 0], [2, 0, 0, 6, 1, 7, 0, 0, 9], [6, 0, 0, 8, 0, 2, 0, 0, 3],
              [0, 4, 8, 3, 7, 6, 1, 2, 0], [7, 6, 0, 1, 2, 4, 0, 9, 8], [0, 2, 3, 5, 8, 9, 7, 4, 0],
              [4, 0, 0, 9, 0, 3, 0, 0, 2], [3, 0, 0, 7, 5, 1, 0, 0, 4], [0, 7, 6, 0, 4, 0, 9, 3, 0]]

grilleMoyen=[[0, 9, 0, 2, 0, 0, 0, 6, 0], [0, 2, 0, 0, 0, 0, 8, 0, 0], [1, 0, 7, 8, 0, 0, 5, 9, 0],
             [5, 0, 6, 0, 0, 0, 1, 2, 0], [7, 1, 0, 6, 5, 0, 0, 3, 0], [0, 0, 0, 4, 0, 0, 0, 0, 0],
             [0, 5, 0, 1, 0, 4, 0, 0, 8], [2, 8, 9, 0, 0, 0, 0, 0, 4], [0, 0, 0, 0, 8, 0, 0, 0, 0]]

grilleDifficile=[[0, 7, 0, 0, 1, 0, 0, 9, 0], [9, 0, 0, 8, 0, 0, 0, 0, 7], [0, 0, 3, 0, 0, 0, 0, 0, 6],
                [0, 4, 0, 0, 0, 1, 5, 0, 0], [0, 3, 0, 0, 0, 0, 0, 1, 0], [0, 0, 2, 7, 0, 0, 0, 6, 0],
                [5, 0, 0, 0, 0, 0, 6, 0, 0], [6, 0, 0, 0, 0, 5, 0, 0, 2], [0, 8, 0, 0, 2, 0, 0, 7, 0]]

grilleDiabolique=[[0, 9, 0, 0, 2, 6, 0, 0, 8], [0, 3, 0, 0, 0, 0, 0, 0, 0], [0, 7, 0, 0, 0, 0, 2, 1, 4],
                  [0, 1, 0, 0, 7, 8, 0, 0, 0], [0, 0, 0, 6, 0, 3, 0, 0, 0], [0, 0, 0, 4, 5, 0, 0, 3, 0],
                  [5, 6, 7, 0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0, 0, 9, 0], [8, 0, 0, 3, 1, 0, 0, 5, 0]]

#----------------------------------- Fonction du Programme ----------------------------

# ============================== Fonction du jeu ===========================

# modifi les valeurs des variable globale correspondant
# aux ligne ,colonne et carré

def modifi():
    global ligne1,ligne2,ligne3,ligne4,ligne5,ligne6,ligne7,ligne8,ligne9
    global colone1,colone2,colone3,colone4,colone5,colone6,colone7,colone8,colone9
    global carre1,carre2,carre3,carre4,carre5,carre6,carre7,carre8,carre9
    ligne1=grilleSudo[0]
    ligne2=grilleSudo[1]
    ligne3=grilleSudo[2]
    ligne4=grilleSudo[3]
    ligne5=grilleSudo[4]
    ligne6=grilleSudo[5]
    ligne7=grilleSudo[6]
    ligne8=grilleSudo[7]
    ligne9=grilleSudo[8]
    colone1=[grilleSudo[0][0],grilleSudo[1][0],grilleSudo[2][0],
             grilleSudo[3][0],grilleSudo[4][0],grilleSudo[5][0],
             grilleSudo[6][0],grilleSudo[7][0],grilleSudo[8][0]]
    colone2=[grilleSudo[0][1],grilleSudo[1][1],grilleSudo[2][1],
             grilleSudo[3][1],grilleSudo[4][1],grilleSudo[5][1],
             grilleSudo[6][1],grilleSudo[7][1],grilleSudo[8][1]]
    colone3=[grilleSudo[0][2],grilleSudo[1][2],grilleSudo[2][2],
             grilleSudo[3][2],grilleSudo[4][2],grilleSudo[5][2],
             grilleSudo[6][2],grilleSudo[7][2],grilleSudo[8][2]]
    colone4=[grilleSudo[0][3],grilleSudo[1][3],grilleSudo[2][3],
             grilleSudo[3][3],grilleSudo[4][3],grilleSudo[5][3],
             grilleSudo[6][3],grilleSudo[7][3],grilleSudo[8][3]]
    colone5=[grilleSudo[0][4],grilleSudo[1][4],grilleSudo[2][4],
             grilleSudo[3][4],grilleSudo[4][4],grilleSudo[5][4],
             grilleSudo[6][4],grilleSudo[7][4],grilleSudo[8][4]]
    colone6=[grilleSudo[0][5],grilleSudo[1][5],grilleSudo[2][5],
             grilleSudo[3][5],grilleSudo[4][5],grilleSudo[5][5],
             grilleSudo[6][5],grilleSudo[7][5],grilleSudo[8][5]]
    colone7=[grilleSudo[0][6],grilleSudo[1][6],grilleSudo[2][6],
             grilleSudo[3][6],grilleSudo[4][6],grilleSudo[5][6],
             grilleSudo[6][6],grilleSudo[7][6],grilleSudo[8][6]]
    colone8=[grilleSudo[0][7],grilleSudo[1][7],grilleSudo[2][7],
             grilleSudo[3][7],grilleSudo[4][7],grilleSudo[5][7],
             grilleSudo[6][7],grilleSudo[7][7],grilleSudo[8][7]]
    colone9=[grilleSudo[0][8],grilleSudo[1][8],grilleSudo[2][8],
             grilleSudo[3][8],grilleSudo[4][8],grilleSudo[5][8],
             grilleSudo[6][8],grilleSudo[7][8],grilleSudo[8][8]]
    carre1=[grilleSudo[0][0],grilleSudo[0][1],grilleSudo[0][2],
             grilleSudo[1][0],grilleSudo[1][1],grilleSudo[1][2],
             grilleSudo[2][0],grilleSudo[2][1],grilleSudo[2][2]]
    carre2=[grilleSudo[0][3],grilleSudo[0][4],grilleSudo[0][5],
             grilleSudo[1][3],grilleSudo[1][4],grilleSudo[1][5],
             grilleSudo[2][3],grilleSudo[2][4],grilleSudo[2][5]]
    carre3=[grilleSudo[0][6],grilleSudo[0][7],grilleSudo[0][8],
             grilleSudo[1][6],grilleSudo[1][7],grilleSudo[1][8],
             grilleSudo[2][6],grilleSudo[2][7],grilleSudo[2][8]]
    carre4=[grilleSudo[3][0],grilleSudo[3][1],grilleSudo[3][2],
             grilleSudo[4][0],grilleSudo[4][1],grilleSudo[4][2],
             grilleSudo[5][0],grilleSudo[5][1],grilleSudo[5][2]]
    carre5=[grilleSudo[3][3],grilleSudo[3][4],grilleSudo[3][5],
             grilleSudo[4][3],grilleSudo[4][4],grilleSudo[4][5],
             grilleSudo[5][3],grilleSudo[5][4],grilleSudo[5][5]]
    carre6=[grilleSudo[3][6],grilleSudo[3][7],grilleSudo[3][8],
             grilleSudo[4][6],grilleSudo[4][7],grilleSudo[4][8],
             grilleSudo[5][6],grilleSudo[5][7],grilleSudo[5][8]]
    carre7=[grilleSudo[6][0],grilleSudo[6][1],grilleSudo[6][2],
             grilleSudo[7][0],grilleSudo[7][1],grilleSudo[7][2],
             grilleSudo[8][0],grilleSudo[8][1],grilleSudo[8][2]]
    carre8=[grilleSudo[6][3],grilleSudo[6][4],grilleSudo[6][5],
             grilleSudo[7][3],grilleSudo[7][4],grilleSudo[7][5],
             grilleSudo[8][3],grilleSudo[8][4],grilleSudo[8][5]]
    carre9=[grilleSudo[6][6],grilleSudo[6][7],grilleSudo[6][8],
             grilleSudo[7][6],grilleSudo[7][7],grilleSudo[7][8],
             grilleSudo[8][6],grilleSudo[8][7],grilleSudo[8][8]]

# testGagne verifie que la somme de chaque ligne , chaque colonne et chaque carré
# renvoie bien 45 en utilisant la fonction sommeListe()
# pour savoir si la grille est gagnante  

def testGagne():
    for k in listeGrille:        
        if not sommeListe(eval(k)):
            return False
    return True

def sommeListe(liste):
    return sum(liste)==45
         
        
# testGrille utilise la fonction plusTest pour compter le nombre
# de fois ou un chiffre apparait dans une liste de colonne de ligne ou de carré
# et retourne vrai si il n'y a pas plus de 1 chiffre par ligne, colonne ou carré
# sinon retourne faux

def testGrille():
    global listeGrille
    for k in listeGrille:        
        if not plusTest(eval(k)):
            return False
    return True

# la fonction plusTest pour compter le nombre
# de fois ou un chiffre apparait dans une liste de colonne de ligne ou de carré    

def plusTest(liste):
    for i in range(1,10):
        if liste.count(i)>1:
            return False
    return True

# ============================== Fonction de l'interface graphique =====================================

# grille affiche la grille et
# affiche que si le chiffre est différent de 0

def grille():
    can.delete(ALL)
    for k in range(nb1+1):
        can.create_line(x0+c1*k, y0,x0+c1*k,y0 + nb1*c1, width=3)
        can.create_line(x0, y0+c1*k,x0+nb1*c1 ,y0+c1*k, width=3)
    for i in range(nb+1):
        can.create_line(x0+c*i, y0,x0+c*i,y0 + nb*c)
        can.create_line(x0, y0+c*i,x0+nb*c ,y0+c*i)
        for i in range(nb):
            for j in range(nb):
                if grilleSudo[i][j]>0 and grilleSudo[i][j]<10:
                    if typeJeu==1:
                        if testPos(i,j):
                            can.create_text (y0 +c*(j+.5),x0+c*(i+.5),text=str(grilleSudo[i][j]),font=("helvetica",15),fill=couleur)
                        else :
                            can.create_text (y0 +c*(j+.5),x0+c*(i+.5),text=str(grilleSudo[i][j]),font=("helvetica",15),fill='blue')
                    else:
                        can.create_text (y0 +c*(j+.5),x0+c*(i+.5),text=str(grilleSudo[i][j]),font=("helvetica",15),fill=couleur)
        
# correspond renvoi les coordonnées i et j pour ecrire

def correspond(x,y):
    return [(y-y0)/c,(x-x0)/c]

# ecrire récupère les coordonnées du clique
# du bouton gauche de la souris et retourne i ligne et j colonne dans saisir

def ecrire(event):
    (i,j)=correspond(event.x,event.y)
    if i in range(nb) and j in range (nb):
        saisir(i,j)

# la fonction saisir, saisie le chiffre dans la bonne case et verifie si modif est vrai ou faux, 
# donc si le chiffre existe déja sur une ligne, une colonne ou un carré
# le cas échéant il demande de cliquer sur une case ou affiche que le chiffre existe déja,
# enfin la fonction vérifie aussi si la grille est gagnante a l'aide de la fonction testGagne
# qui renvoi vrai ou faux et affiche le cas échéant "GRILLE GAGNANTE".
# en mode résolution les chiffres bloqués aparaisse en bleu et ne sont pas modifiable,
# on utilise la fonction testPos pour savoir si la position dans la grille est bloquée ou non.

def saisir(i,j):
    global couleur
    t.delete("0.0",END)
    if typeJeu==1:
        if not testPos(i,j):
            return
    if not modif(i,j,nombreEntre):
        t.delete("0.0",END)
        if modeJeu==1:
            t.configure(fg="red")
            t.insert(END,"Le chiffre entré    existe déja sur une ligne une colonne ouun carré")
            couleur='red'
        else:
            t.configure(fg="black")
            t.insert(END,"")
            couleur='black'            
    else:
        couleur='black'
        if testGagne():
            t.delete("0.0",END)
            t.configure(fg="blue")
            t.insert(END,"\n   GRILLE GAGNANTE")
            bnew.configure(state=NORMAL)
    can.delete(ALL)
    grille()

def testPos(i,j):
    if bloqueSudo[i][j]!=10:
        return True
    

# modif sert a modifier les valeurs
# de la liste grilleSudo pour i ligne
# j colonne et retourne testGrille()
# qui retourne vrai ou faux

def modif(i,j,nombreEntre):
    global grilleSudo
    grilleSudo[i][j]=nombreEntre
    modifi()
    return testGrille()
    
# les fonction de button de chiffre permettent de modifier
# la variable globale nombreEntre pour entré un chiffre dans une case
# sachant que le chiffre 0 éfface la case

def bun():
    global nombreEntre
    nombreEntre=1
    t.delete("0.0",END)
    t.configure(fg="blue")
    t.insert(END,"cliquer sur une case")

def bdeux():
    global nombreEntre
    nombreEntre=2
    t.delete("0.0",END)
    t.configure(fg="blue")
    t.insert(END,"cliquer sur une case")

def btrois():
    global nombreEntre
    nombreEntre=3
    t.delete("0.0",END)
    t.configure(fg="blue")
    t.insert(END,"cliquer sur une case")

def bquatre():
    global nombreEntre
    nombreEntre=4
    t.delete("0.0",END)
    t.configure(fg="blue")
    t.insert(END,"cliquer sur une case")

def bcinq():
    global nombreEntre
    nombreEntre=5
    t.delete("0.0",END)
    t.configure(fg="blue")
    t.insert(END,"cliquer sur une case")

def bsix():
    global nombreEntre
    nombreEntre=6
    t.delete("0.0",END)
    t.configure(fg="blue")
    t.insert(END,"cliquer sur une case")

def bsept():
    global nombreEntre
    nombreEntre=7
    t.delete("0.0",END)
    t.configure(fg="blue")
    t.insert(END,"cliquer sur une case")

def bhuit():
    global nombreEntre
    nombreEntre=8
    t.delete("0.0",END)
    t.configure(fg="blue")
    t.insert(END,"cliquer sur une case") 

def bneuf():
    global nombreEntre
    nombreEntre=9
    t.delete("0.0",END)
    t.insert(END,"cliquer sur une case")

def bdel():
    global nombreEntre
    nombreEntre=0
    t.delete("0.0",END)
    t.configure(fg="blue")
    t.insert(END,"cliquer sur une case")

# new lance le programme et affiche la grille

def new():
    global typeJeu,nombreEntre,modeJeu
    nombreEntre=0
    typeJeu=0
    modeJeu=1
    t.delete("0.0",END)
    can.delete(ALL)
    grille()
    bactive.configure(state=DISABLED)
    bdesactive.configure(state=ACTIVE)
    
# New réinitialise une grille vide

def New():
    global grilleSudo
    grilleSudo=[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    new()
    
# sauve est dans le menu fichier et permet de sauvegarder une grille

def sauve():
      myFormats =[('Fichier Texte','*.txt')]
      fileName = tkFileDialog.asksaveasfilename(parent=fen,filetypes=myFormats,title='Enregistrer sous...')
      if fileName !='':
            f=open(fileName, 'w')
            f.write(str(grilleSudo))
            tkMessageBox.showinfo('Fichier sauvegardé','Fichier sauvegardé')
            f.close
      else:
            tkMessageBox.showinfo('Fichier non sauvegardé','Fichier non sauvegardé')

# ouvrir est dans le menu Édition et permet d'ouvrir une grille

def ouvrir():
    global grilleSudo,modeJeu
    modeJeu=1
    bactive.configure(state=DISABLED)
    bdesactive.configure(state=ACTIVE)
    myFormats =[('Fichier Texte','*.txt')]
    fileOpen = tkFileDialog.askopenfilename(parent=fen,filetypes=myFormats,title='Choisir fichier')
    if fileOpen !='':
        f=open(fileOpen, 'r')
        grilleSudo=eval(f.read())
        f.close
        new()
        
# ouvrirResolution est dans le menu Resolution et permet d'ouvrir une grille en mode résolution

def ouvrirResolution():
    global grilleSudo,modeJeu,typeJeu
    modeJeu=1
    bactive.configure(state=DISABLED)
    bdesactive.configure(state=ACTIVE)
    myFormats =[('Fichier Texte','*.txt')]
    fileOpen = tkFileDialog.askopenfilename(parent=fen,filetypes=myFormats,title='Choisir fichier')
    if fileOpen !='':
        f=open(fileOpen, 'r')
        grilleSudo=eval(f.read())
        f.close
        new()
    typeJeu=1
    bdesactive.configure(state=DISABLED)
    bactive.configure(state=ACTIVE)
    genere()
    

def facile():
    global grilleSudo,typeJeu,modeJeu
    t.delete("0.0",END)
    can.delete(ALL)
    grilleSudo=grilleFacile
    typeJeu=1
    modeJeu=0
    bdesactive.configure(state=DISABLED)
    bactive.configure(state=ACTIVE)
    genere()

def moyen():
    global grilleSudo,typeJeu,modeJeu
    t.delete("0.0",END)
    can.delete(ALL)
    grilleSudo=grilleMoyen
    typeJeu=1
    modeJeu=0
    bdesactive.configure(state=DISABLED)
    bactive.configure(state=ACTIVE)
    genere()

def difficile():
    global grilleSudo,typeJeu,modeJeu
    t.delete("0.0",END)
    can.delete(ALL)
    grilleSudo=grilleDifficile
    typeJeu=1
    modeJeu=0
    bdesactive.configure(state=DISABLED)
    bactive.configure(state=ACTIVE)
    genere()

def diabolique():
    global grilleSudo,typeJeu,modeJeu
    t.delete("0.0",END)
    can.delete(ALL)
    grilleSudo=grilleDiabolique
    typeJeu=1
    modeJeu=0
    bdesactive.configure(state=DISABLED)
    bactive.configure(state=ACTIVE)
    genere()

def genere():
    global grilleSudo,typeJeu,bloqueSudo
    bloqueSudo=[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    t.delete("0.0",END)
    can.delete(ALL)
    for i in range(nb):
            for j in range(nb):
                if bloqueSudo[i][j]!=grilleSudo[i][j]:
                    bloqueSudo[i][j]+=10
    typeJeu=1
    grille()

def bactive():
    global modeJeu
    bactive.configure(state=DISABLED)
    bdesactive.configure(state=ACTIVE)
    modeJeu=1

def bdesactive():
    global modeJeu
    bdesactive.configure(state=DISABLED)
    bactive.configure(state=ACTIVE)
    modeJeu=0

# MenuAPropos est dans le menu '?' et permet d'afficher
# des informations le programme et son concepteur

def menuAPropos():                                                                        
    tkMessageBox.showinfo("À propos de Sudoku","     Sudoku version 2.1\n\n           conçu par\n\n     Guillaume D\n")

# stop_quit permet de fermer et détruire la fenetre

def stop_quit():
    if tkMessageBox.askokcancel("Quitter", "Voulez vous vraiment quitter ?"):
        fen.quit()
        fen.destroy()

# la fenêtre principale

fen=Tk()

barreDeMenus=Menu(fen)                                                             
fen.config(menu=barreDeMenus)

menuFichier=Menu(barreDeMenus)

barreDeMenus.add_cascade(label="Édition", menu=menuFichier)
menuFichier.add_command(label="Ouvrir...", command=ouvrir)                          
menuFichier.add_command(label="Enregistrer sous...", command=sauve)
menuFichier.add_separator()                                                                  
menuFichier.add_command(label="Quitter", command=stop_quit)

menuResolution=Menu(barreDeMenus)                                                             
barreDeMenus.add_cascade(label="Résolution", menu=menuResolution)
menuResolution.add_command(label="Grille Facile", command=facile)
menuResolution.add_command(label="Grille Moyen", command=moyen)
menuResolution.add_command(label="Grille Difficile", command=difficile)
menuResolution.add_command(label="Grille Diabolique", command=diabolique)
menuResolution.add_separator()                                                                  
menuResolution.add_command(label="Ouvrir une grille en mode résolution", command=ouvrirResolution)

menuInfo = Menu(barreDeMenus) 
barreDeMenus.add_cascade(label="À Propos", command=menuAPropos)# menu=menuInfo
#menuInfo.add_command(label="À  Propos")

# le canvas

can=Canvas(fen,width=800,height=800,bg="white")
can.bind("<Button-1>",ecrire)
can.pack(side=LEFT)

# les boutons

bnew=Button(fen,text='Édition',font=("courier",10,"bold"), command=New)
bnew.pack(side=TOP)

bframe=Frame(fen,width=200)

bun=Button(bframe, text="1",font=("courier",10,"bold"),command=bun)
bdeux=Button(bframe, text="2",font=("courier",10,"bold"),command=bdeux)
btrois=Button(bframe, text="3",font=("courier",10,"bold"),command=btrois)
bquatre=Button(bframe, text="4",font=("courier",10,"bold"),command=bquatre)
bcinq=Button(bframe, text="5",font=("courier",10,"bold"),command=bcinq)
bsix=Button(bframe, text="6",font=("courier",10,"bold"),command=bsix)
bsept=Button(bframe, text="7",font=("courier",10,"bold"),command=bsept)
bhuit=Button(bframe, text="8",font=("courier",10,"bold"),command=bhuit)
bneuf=Button(bframe, text="9",font=("courier",10,"bold"),command=bneuf)
bdel=Button(bframe, text="Effacer",font=("courier",10,"bold"),command=bdel)

bframe.pack()
bun.pack(side=TOP)
bdeux.pack()
btrois.pack()
bquatre.pack()
bcinq.pack()
bsix.pack()
bsept.pack()
bhuit.pack()
bneuf.pack()
bdel.pack(side=BOTTOM)

t=Text(fen ,height=4 ,width=20 ,bg="light grey" ,font=("courier",15,"bold"))
t.pack()

Label(fen,text="AIDE",font=("courier",15,"bold"),fg="black").pack()

bframe1=Frame(fen,width=200)
bframe1.pack()

bactive=Button(bframe1 ,text="Activer", font=("courier",10,"bold"), command=bactive)
bactive.pack(side=LEFT)

bdesactive=Button(bframe1 ,text="Désactiver", font=("courier",10,"bold"), command=bdesactive)
bdesactive.pack(side=RIGHT)

can.bind("<Button-1>",ecrire)

bquit = Button(fen,text='Quitter',font=("courier",10,"bold"), command=stop_quit)
bquit.pack(side=BOTTOM)

# le lancement de l'application

fen.mainloop()