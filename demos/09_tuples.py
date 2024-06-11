# Une tuple est dit immuables
# C'est à dire qu'une fois défini il ne peut pas être modifié
# Son avantage est d'être beaucoup plus performant que les listes

mon_tuple = ()
mon_second_tuple = tuple()

mon_troisieme_tuple = (1, 2)
mon_quatrieme_tuple = 1, 2


# unpacking
a, b = mon_troisieme_tuple
print(a, b)

nombres = (1, 5, 10, 23)
x, _, _, z = nombres
print(x, z)
