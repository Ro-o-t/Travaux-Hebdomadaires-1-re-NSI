import csv#on importe le module csv


def enleve_doublons(fichier):#définition de la fonction
    """
    entrée: la liste composée des données du fichier csv
    rôle: renvoyer une liste mais en enlevant les éventuels doublons situés
    dans le fichier csv
    sortie: une matrice
    """
    nouvelle_liste = []#création de la liste renvoyée
    liste_album = [' Album']#on crée cette liste afin d'éliminer les doublons
    #Album est mis d'office car on ne veut pas inslure la première ligne 
    #du fichier
    for album in fichier:#on parcourt chaque liste de la matrice
        if album[2] not in liste_album:#si l'album n'a jamais été vu
            nouvelle_liste.append(album)#on ajoute les données
            liste_album.append(album[2])#et on actualise la vérification
    return nouvelle_liste#on renvoit la liste

def donne_nom(liste):#on définit une fonction
    """
    entrée: la liste sans doublons
    role: renvoyer une liste avec le nom de chaque album
    sortie: une liste de chaines de charactères
    """
    liste_nom = []#création d'une liste vide
    for rang in liste:#on parcourt la liste
        liste_nom.append(rang[2])#on ajoute à la liste vide le nom de l'album
    return liste_nom#on renvoit la liste finale

fichier = open('quelques-disques.csv', 'r', encoding='utf-8')#ouverture
#du fichier csv

tableau = list(csv.reader(fichier, delimiter=','))#lecture du fichier csv
#on trensfert les données dans un tableau

fichier.close#fermeture du fichier

liste_disques = enleve_doublons(tableau)#on enlève les doublons en appelant
#la fonction

#test 1:
print(donne_nom(liste_disques))#on affiche le résultat