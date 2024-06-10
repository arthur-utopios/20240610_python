age = int(input("Saisir âge: "))
salaire = int(input("Saisir salaire: "))
xp = int(input("années expériences: "))

valide = True
message = ""

if age < 30:
    message = "Vous n'avez pas l'âge minimum requis\n"
    valide = False
if salaire > 40000:
    # message = message + "Vous exigez un salaire trop élevé\n"
    message += "Vous exigez un salaire trop élevé\n"
    valide = False
if xp < 5:
    message += "Vous manquez d'expérience"
    valide = False

if valide:
    message = "Félicitation vous êtes embauché!"

print(message)

if(age < 30):
    print("Trop jeune")
elif(salaire > 40000):
    print("Salaire trop élevé")
elif(xp < 5):
    print("Pas assez d'expérience")
else:
    print("Vous êtes embauché")