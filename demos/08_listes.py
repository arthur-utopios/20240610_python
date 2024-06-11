# syntaxe à privilégier
ma_liste = []

print(type(ma_liste))

# utilisation du constructeur
ma_seconde_liste = list()

print(type(ma_seconde_liste))

# Les listes peuvent avoir des types dynamiques
ma_liste = [1, 'arthur', True, 12.3, [1, 2, 3]]

print(ma_liste)
# Les éléments de la liste sont indexés de 0 à taille - 1
print(ma_liste[0], ma_liste[1], ma_liste[-1])
# Accéder à un élément d'une liste dans une liste
print(ma_liste[4][0])

print("taille 'ma_liste':", len(ma_liste))

# Ajouter un élément à la fin de la liste
ma_liste.append('hello')
print(ma_liste[-1])

# Trier une liste
mes_entiers = [10, 11, 45, 3, 200, 1]
mes_entiers.sort()
print(mes_entiers)
mes_entiers.sort(reverse=True)
print(mes_entiers)

# Ajout un élément à un index précis
mes_entiers.insert(1, 88)
print(mes_entiers)

# Ajouter une liste en fin de liste
mes_entiers.extend([131, 42])
print(mes_entiers)

# Supprimer par rapport à l'index
print(mes_entiers.pop(1)) # 88
print(mes_entiers)

# Supprime le premier élément qui correspond
mes_entiers.remove(1)
print(mes_entiers)

for nombre in mes_entiers:
    print(nombre)

# enumerate renvoie un tuple avec l'index et la valeur
# Ici on utilise la destructuration pour récupérer l'index et la valeur
for (index, value) in enumerate(mes_entiers):
    print('index:', index, 'value:', value)

print('max:', max(mes_entiers))

# List comprehension
# https://www.pythoncheatsheet.org/cheatsheet/comprehensions
liste_nombre = [x for x in range(1, 11)]
print(liste_nombre)

liste_carre = [x**2 for x in liste_nombre]
print(liste_carre)

liste_pair = [x for x in liste_carre if x % 2 == 0]
print(liste_pair)