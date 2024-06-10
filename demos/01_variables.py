# print : écrire dans le terminal
print("Hello world!")
print('Hello world!')

# Pour échapper le caractère ' on utilise un backslash: \
print('J\'arrive')

# Chaîne sur plusieurs lignes
print("""Hello
    world
        !""")

# On peut passer une infinité de paramètres à la fonction print
# Par défaut, elle va afficher les éléments séparés par un espace
print(1, "chaîne", 12.3)

# Déclaration de variable
# Le caractère = est un opérateur d'affectation
# J'affecte la valeur 8 à la variable ma_valeur
# Les déclarations dans python se font en snake_case
ma_variable = 8

# Les numériques
var = 23 # int
# Afficher le type de la variable
print(type(var))

var = 23.0 # float
print(type(var))

var = 23. # float
print(type(var))

# Chaîne de caractères
var = "23.0" # str => string
print(type(var))

# Les booléens
mon_bool = True # bool
print(mon_bool)
print(type(mon_bool))

mon_bool = False
print(mon_bool)

print("4 < 5", 4 < 5)  # inférieur <
print("4 > 5", 4 > 5) # supérieur >
print("4 >= 5", 4 >= 5) # supérieur ou égal
print("4 <= 5", 4 <= 5) # inférieur ou égal
print("5 == 5", 5 == 5) # égalité
print("6 != 5", 6 != 5) # différent de

print("Saisir votre age: ")
# input permet de lire des entrées depuis le terminal
age = input()
print("Votre âge est de:", age, "ans")
print("age:", type(age)) # str

# Cast : convertir un type vers un autre
age_int = int(age)
print("age_int:", type(age_int))
age_float = float(age_int)
print("age_float:", type(age_float))

# On peut saisir l'intitulé de ce qu'on veut afficher directement dans la fonction input
prenom = input("Saisir votre prénom: ")
print(prenom)