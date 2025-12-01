def plus_long_palindrome(s):
    n = len(s)
    max_palindrome = ""
    for i in range(n):
        for j in range(i, n):
            sous_chaine = s[i:j+1]
            if sous_chaine == sous_chaine[::-1] and len(sous_chaine) > len(max_palindrome): max_palindrome = sous_chaine
    return max_palindrome

s = input("Entrez une chaîne : ")
print("Le plus long palindrome est :", plus_long_palindrome(s))