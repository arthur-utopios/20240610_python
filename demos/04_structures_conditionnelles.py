age = int(input("Saisir âge: "))

# tab pour créer une indentation
# shift + tab pour supprimer l'indentation
# Il faut respecter l'indentation, autrement le code ne s'exécutera pas
if(age >= 21):
    print("Majeur aux USA")
elif(age >=18):
    print("Majeur en Europe")
else:
    print("Vous êtes mineur")

is_admin = True

# Ici le message s'affichera à chaque fois, car is_admin est toujours à Vrai
if(age > 18 or is_admin):
    print("Vous avez tous les droits")