
"""
entrée: une liste (vide ou non)
but: rechercher le maximum de la liste
sortie: le maximum de la liste, -1 si elle est vide
"""

def recherche_maximum(liste):#création de la fonction
    if liste == []:#on vérifie si la liste est vide
       return -1#on renvoit alors -1
    maximum = liste[0]#sinon on crée maximum qui prend la valeur
    #du premier rang de la liste
    for rang in range(len(liste)):#on parcours la liste
        if liste[rang] > maximum:#si le rang actuel est plus grand que maximum
            maximum = liste[rang]#on redéfinit la valeur de maximum
    return maximum#puis on renvoit maximum



liste_1 = [0, 1, 2, 3, 4, 5]#premier test avec cette liste
print(recherche_maximum(liste_1))#on appelle la fonction

liste_2 = [0, 15, 2, 3, 4, 5]#deuxieme test avec cette liste
print(recherche_maximum(liste_2))#on appelle la fonction

liste_3 = []#test avec une liste vide
print(recherche_maximum(liste_3))#on appelle la fonctions

#temps passé: 5 min