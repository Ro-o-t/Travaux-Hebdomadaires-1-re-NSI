def premier_indice(liste_nb, valeur):  # Définition d'une fonction
    """
    Entrée: une liste d'entiers et une valeur
    Rôle: chercher la valeur dans la liste et récupérer son premier indice 
    où elle apparaît
    Sortie: un entier (-1 si la valeur n'est pas trouvée) 
    """

    indice = None  # Initialisation de la variable indice
    rang = 0  # Initialisation de la variable rang

    while rang < len(liste_nb) and indice == None:  # On parcourt 
        #la liste tant que la valeur n'est pas trouvée
        if liste_nb[rang] == valeur:  # Si la valeur est trouvée
            indice = rang  # indice prend la valeur de rang
        rang += 1  # Incrémentation de rang (1)

    if indice is None:  # Si la valeur n'a pas été trouvée
        indice = -1  # indice prend la valeur -1

    return indice  # On renvoie indice


# tests:
print(premier_indice([0, 1, 2, 3, 4, 5], 2))  # test 1

print(premier_indice([0, 5, 15, 5, 2, 3, 4, 5], 5))  # test 2

print(premier_indice([0, 1, 2, 3, 4, 5], 8))  # test 3
