def score(s):
    score=0
    set_s = set(s)
    for i in range (len(set_s)-1):
        score = abs (ord(s[i]) - ord(s[i+1])) + abs (ord(s[i+1]) - ord(s[i]))
    return score
    

    
s= input("Entrez une chaîne de caractères : ")
print("Le score de la chaîne est :", score(s))