from math import floor

# On prend la valeur absolue saisie par l'utilisateur pour éviter les erreurs
population_actuelle = abs(int(input("Saisir la population actuelle: ")))
taux_accroissement = abs(float(input("Saisir taux accroissement (%): ")))
population_visee = abs(int(input("Saisir une population visée: ")))

while(population_visee < population_actuelle):
    print("Erreur! La population visée doit être supérieure à la population actuelle")
    population_visee = abs(int(input("Saisir une population visée: ")))

annee = 0

while population_actuelle < population_visee:
    population_actuelle *= 1 + (taux_accroissement / 100)
    annee += 1

print(f"La population visée sera de {floor(population_actuelle)} habitants en {annee} ans")