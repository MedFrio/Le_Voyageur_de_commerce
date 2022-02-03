from itertools import permutations
from math import sqrt
import random
import sys
def Puissance(a):
    return a**2
def Distance(x1,y1,x2,y2):
    return sqrt(Puissance(y2-y1)+Puissance(x2-x1))
liste=[]
a=[[" "]*49 for _ in range(19)]
reponse="nothing"
while reponse!="y" :
    reponse=str(input("Générer un tableau de 8 Coordonnées aléatoires, 'y' or 'n' : "))
for i in range (8):
    x=random.randint(2,47)
    y=random.randint(2,17)
    a[y][x] = 'X'
    liste.append(x)
    liste.append(y)
print(liste)
reponse="nothing"
while reponse!="y" :
    reponse=str(input("Générer un affichage basique,en y insérant les point générés , 'y' or 'n' : "))
for n in range (49):
    a[0][n] = '-'
    a[18][n] = '-'
for m in range (19) :
    a[m][0] = '|'
    a[m][48] = '|'
for i in range (19):
    for j in range (49):
        sys.stdout.write( a[i][j])
    print('')
reponse="nothing"
while reponse!="y" :
    reponse=str(input("Calculer et Afficher les distances entre tous les points , 'y' or 'n' : "))
i=0
TabDist=[]
matrice=[]
while i<16 :
    j=0
    TabDist=[]
    while j<16 :
        x=liste[i]
        y=liste[i+1]
        X=liste[j]
        Y=liste[j+1]
        print("Calcul la distance entre A : ",(x,y)," et B : ",(X,Y)," est : "+str(Distance(x,y,X,Y)))
        j=j+2
        TabDist.append(Distance(x,y,X,Y))
    i+=2
    matrice.append(TabDist)
    
    if i<15 :
        print("")
        print("Prochain point")
        print("")
i=0
print(matrice)
reponse="nothing"
while reponse!="y" :
    reponse=str(input("Construire le tableau de tous les chemins possible , 'y' or 'n' : "))
i=0
points=[]
while i<16 :   
    points.append([liste[i],liste[i+1]])
    i=i+2
chemins = permutations(points)  
Tab=[]
for i in list(chemins):
    Tab.append(i)
print("Le tableau de tous les chemins possible a été généré.")
print("Ne pas print() tous les chemins possible, car il y'a BEAUCOUP de possibilités")
reponse="nothing"
while reponse!="y" :
    reponse=str(input("Calculer tous les possibilités de voyage et trouvez le chemin le plus court , 'y' or 'n' : "))
matricecopie=matrice
i=0
while i<=7:
    del matricecopie[i][i]
    i=i+1
shortdist=[]
for i in range(7):
    shortdist.append(min(matricecopie[i]))
print(shortdist)
