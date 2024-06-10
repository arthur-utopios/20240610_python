import math

# Opérateur arithmétiques 
print(10 / 2)
print(5 - 3)
print(3 + 7)
print(3 * 5)

# Division entière
print(5 // 3)

# Modulo : le reste de la division
print(5 % 3) # 2
print(6 % 3) # 0

# Mettre à la puissance
print(2 ** 3) # 3

# round permet d'arrondir un résultat
print(round(1.4)) # 1
print(round(1.5)) # 2

# round prend en second paramètre le nombre de chiffres après la virgule
print(round(1.2748, 2))

# la fonction ceil permet d'arrondir à l'entier supérieur
print(math.ceil(1.2)) # 2

# la fonction floor permet d'arrondir à l'entier inférieur
print(math.floor(1.9)) # 1

print(math.pi) # 3.141592653589793

# Opérateurs de comparaisons
print("4 < 5", 4 < 5)  # inférieur <
print("4 > 5", 4 > 5) # supérieur >
print("4 >= 5", 4 >= 5) # supérieur ou égal
print("4 <= 5", 4 <= 5) # inférieur ou égal
print("5 == 5", 5 == 5) # égalité
print("6 != 5", 6 != 5) # différent de

# Opérateurs logiques

# Opérateur ET (les deux expressions doivent être vraies)
print((25 > 5) and (120 != 30)) # True
print((25 > 5) & (120 != 30)) # True

#Opérateur OU (l'une, l'autre ou les deux doivent être vraies)
print((25 > 50) or (120 != 30)) # True
print((25 > 50) | (120 != 30)) # True

# Opérateur OU exclusion (l'un, l'autre mais pas les deux)
print((25 > 50) ^ (120 != 30)) 

# opérateur d'inversion 
print(not True) # False
print(not (25 > 50)) # True