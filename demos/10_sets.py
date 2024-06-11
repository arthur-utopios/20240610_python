nombres = [5, 55, 55, 55, 55, 55, 55, 5, 10, 23, 48, 48, 12]
print(nombres)

nombre_set = set(nombres)
print(nombre_set)

mon_set = set()
dictionnaire = {} # dictionnaire
mon_second_set = {1}
print(type(mon_second_set))
print(type(dictionnaire))

mon_set.add(1)
mon_set.add('a')
mon_set.add(True)
print(mon_set)

# Fusion de deux sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 6, 8}

set1.update(set2)
print(set1)

# Suppression d'un élément
set1.remove(1)
print(set1)
# set.remove(1) provoque une erreur car l'élément n'existe pas

# Supprime l'élément sans lever d'exception
set1.discard(1)

set3 = {3, 4, 1, 6, 12, 23}

print('set1', set1)
print('set3', set3)
print(set1.difference(set3))

print(set1.intersection(set3))
print(set1.union(set3))

ma_liste_sans_doublon = list(set1)
print(ma_liste_sans_doublon)