def incrementer_chiffres(chiffres):
    n = len(chiffres)
    for i in range(n - 1, -1, -1):
        if chiffres[i] < 9:
            chiffres[i] += 1
            return chiffres
        chiffres[i] = 0
    return [1] + chiffres

chiffres = [int(x) for x in input("Entrez les chiffres séparés par des espaces : ").split()]
resultat = incrementer_chiffres(chiffres)
print(resultat)