def premier_indice_min(liste):#déclaration d'une fonction
    """
    Entrée: une liste de nombres
    Rôle: définir l'indice le plus bas du nombre le plus petit de la liste
    Sortie: un entier (l'induce recherché)
    """
    indice = 0#intialisation de l'indice à 0
    minimum = 0#déclaration de l'indice "minimum"
    valeur = liste[0]#intialisation de la valeur de départ
    while indice < len(liste):#on parcourt la liste avec une boucle while
        if liste[indice] < valeur:#si la valeur actuelle est STRICTEMENT
            #inférieure à l'ancienne
            valeur = liste[indice]#réactualisation de la valeur minimale
            minimum = indice#réactualisation de l'indice minimal
        indice += 1#on incrémente l'indice
    return minimum#on renvoit l'indice recherché

#Tests:

print(premier_indice_min([0, 1, 0, 1, 1, 1]))#test 1

print(premier_indice_min([10.2, 5.1, 15, 5.7, 2.3, 3.4, 4, 5.7]))#test 2