prenom = input("Saisir un prénom: ")
nom = input("Saisir un nom: ")

# Utilisation de la fonction print pour concaténer la chaîne de caractères
print("Bonjour", prenom, nom, ".")

# Utilisation de l'opérateur + pour concaténer la chaîne
affichage = "Bonjour " + prenom + " " + nom + "."
print(affichage)

# Utilisation des f-strings pour formation la chaîne
affichage = f"Bonjour {prenom} {nom}."

print(affichage)

# On appelle la méthode title() qui met le premier caractère en majuscule
prenom = prenom.title()

# La méthode upper() met la chaîne de caractère en majuscule
nom = nom.upper()
affichage = f"Bonjour {prenom} {nom}."

print(affichage)