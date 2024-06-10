iteration = 0

epaisseur_feuille = 0.0001
epaisseur_max = 400

while epaisseur_feuille < epaisseur_max:
    iteration += 1
    epaisseur_feuille *= 2

print(f"Pour dépasser les 400m d'épaisseur, il faut plier la feuille {iteration} fois")

iteration = 0
epaisseur_feuille = 0.0001

while epaisseur_max >= epaisseur_feuille:
    iteration += 1
    epaisseur_max /= 2

print(f"Pour arriver à 1mm d'épaisseur, il faut déplier la feuille {iteration} fois")
