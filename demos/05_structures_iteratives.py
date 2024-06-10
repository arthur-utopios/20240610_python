compteur = 0

# On utilise la boucle while quand on ne sait pas d'avance combien de fois on doit itérer
while (compteur < 10):
    print(compteur)
    compteur += 1 # compteur = compteur + 1

# /!\ Attention aux boucles infinies!
# Il faut toujours modifier un élément de la condition pour qu'elle puisse passer à faux
# while (True):
#     print("toto")

# Boucle de 0 à 9
for increment in range(10):
    print("increment:", increment)

# range permet de définir le début et la fin (non comprise)
for increment2 in range(1, 11):
    print("increment2:", increment2)

for increment3 in range(0, 101, 5):
    print("increment3:", increment3)

for increment4 in range(100, -1, -5):
    print("increment4:", increment4)

for i in range(11):
    print(f"La puissance carré de {i} est {i**2}")

# continue et break

for i in range(11):
    if(i == 5):
        continue # passe à l'itération suivante sans exécuter le code
    print(i)

    if(i == 7):
        break # quitte la boucle

print("Je suis en dehors de la boucle")

# On peut imbriquer des boucles les unes dans les autres
# La boucle inférieure s'exécute à chaque fois en entier avant de passer à l'itération suivante de la boucle extérieure
for i in range(10):
    for y in range(3):
        print(i, y)