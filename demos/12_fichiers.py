# file = open("fichier.txt", mode='r', encoding='utf8')

# print(file) # io.TextIOWrapper

# print(file.read())

# lignes = file.readlines()
# print(lignes)

# for line in file:
#     print(line, end='\r')

# ferme la "connection" avec le fichier
# file.close()

# Context manager
# Permet d'omettre la fermeture du fichier en fin de traitement
# La fermeture se fait automatiquement à la fin du bloc d'instruction
with open('fichier.txt', encoding='utf8') as file:
    print(file.readline(), end='')

# le fichier est fermé (sans préciser file.close())!