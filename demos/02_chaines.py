# Concaténation de chaînes
str1 = "chaine 1"
str2 = "chaine 2"
str3 = "str1: " + str1 + " - str2: " + str2

print(str1)
print(str2)
print(str3)
print(str1 + str2) # chaine 1chaine 2

# Ces deux syntaxes sont équivalentes
print(str1, str2)
print(str1 + " " + str2)

# Concaténation de deux types
age = 28 
mon_texte = "Voici mon âge: "
# print(mon_texte + age) # TypeError: can only concatenate str (not "int") to str
print(mon_texte + str(age))

# Formatage de chaînes
prenom = "Arthur"
# Les valeurs dans la chaîne corresponde à la position des arguments de la fonction format
# 0: premier paramètre
# 1: second paramètre
chaine_formatee = "Je m'appelle {0} et j'ai {1} ans".format(prenom, age)
print(chaine_formatee)

# f-string
# On passe directement le nom de la variable dans les accolades
chaine_formatee_deux = f"Je m'appelle {prenom} et j'ai {age}"

# Les chaînes sont des "tableaux de caractères"
# Les caractères d'une chaîne sont indexés
#            01234567
ma_chaine = "abcdefgh"

print(ma_chaine[0]) # a
print(ma_chaine[3]) # d

# Mécanisme de slices (tranches)
# Permet de découper une chaînes
# [2;5[
print(ma_chaine[2:5]) # cde

# du début à 5 non compris
print(ma_chaine[:5]) # abcde

# de 3 à la fin
print(ma_chaine[3:]) # defgh

# chaine[<début>:<fin>:<pas>]

# Caractères spéciaux
# Retour la ligne \n
print("Hello\nworld\n!")

# tabulation \t
print("Hello\tworld\t!")

# Pour échapper le caractère " on ajoute un backslash
print("Salut, je m'appelle Arthur, j'adore aller au \"bowling\"!")