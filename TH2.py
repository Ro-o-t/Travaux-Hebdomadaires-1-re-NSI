
def recherche(liste, nombre):#définition d'une fonction recherche
    """
    Rôle: determiner si un nombre est dans une liste ou non
    entrée: une liste et un entier à chercher
    sortie: si entier dans la liste: True
    sinon: False
    """
    if liste == []:#si la liste est vide
        return False#renvoyer false
    else:#sinon
        for rang in range(len(liste)):#on parcous la liste
            if liste[rang] == nombre:#si le nombre se trouve dans la liste
                return True#renvoyer true
        
        return False#si le nombre n'y est pas renvoyer false

print(recherche([0, 1, 2, 3, 4, 5], 2))#test 1 affiché

print(recherche([0, 1, 2, 3, 4, 5], 5))#test 2 affiché

print(recherche([0, 1, 2, 3, 4, 5], 0))#test 3 affiché

print(recherche([0, 1, 2, 3, 4, 5], 12))#test 4 affiché

#temps passé: 5 min