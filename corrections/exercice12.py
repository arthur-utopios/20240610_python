def compter_lettre_a(chaine: str) -> int:
    compteur = 0
    for lettre in chaine:
        if(lettre == 'a'):
            compteur += 1
    return compteur

print(compter_lettre_a('abba'))
print(compter_lettre_a('mixer'))

def compter_lettre_a_bis(chaine: str) -> int:
    return chaine.count('a')

print(compter_lettre_a_bis('abba'))
print(compter_lettre_a_bis('mixer'))