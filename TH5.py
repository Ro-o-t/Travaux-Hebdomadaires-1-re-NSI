def dernier_indice(liste_nb, valeur):#définition d'une fonction
    """
    Entrée: une liste d'entiers et un entier
    Rôle: renvoyer le dernier indice ou l'entier apparaît dans la liste, 
    -1 sinon
    Sortie: un entier positif ou -1
    """
    renvoie = -1#initialisation de -1
    for rang in range(len(liste_nb)):#on parcourt la liste en entier
        if liste_nb[rang] == valeur:#si la valeur est trouvée
            renvoie = rang#on modifie la valeur de "renvoie"
    return renvoie#enfin on retourne "renvoie"

#Tests:
print(dernier_indice([0, 1, 2, 3, 4, 5], 2))#Test 1

print(dernier_indice([0, 5, 15, 5, 2, 3, 4, 5], 5))#Test 2

print(dernier_indice([0, 1, 2, 3, 4, 5], 8))#Test 3