def recherche_rang(liste_nb, nombre):  # Définition d'une fonction
    """
    Rôle : chercher les index d'un nombre dans une liste
    Entrée : liste (vide ou d'entiers) et un nombre entier
    Sortie : liste des indices où se trouve le nombre dans la liste,
    ou "None" s'il n'y est pas / si la liste est vide
    """
    liste_finale = []  # Création de la liste retournée
    if liste_nb == []:  # Si la liste est vide
        return None  # Retourner None
    else:  # Sinon
        for rang in range(len(liste_nb)):  # On parcourt la liste
            if liste_nb[rang] == nombre:  # Si le nombre y est
                liste_finale.append(rang)  # Ajouter l'index à la liste finale

        if liste_finale == []:  # Si la liste est quand même vide
            return None  # Retourner None
        
        return liste_finale  # Si la liste n'est pas vide : la retourner
    

print(recherche_rang([0, 1, 2, 3, 4, 5], 2))  # Test 1

print(recherche_rang([0, 1, 2, 2, 4, 2], 2))  # Test 2

print(recherche_rang([0, 1, 3, 3, 4, 5], 2))  # Test 3

print(recherche_rang([], 2))  # Test 4
