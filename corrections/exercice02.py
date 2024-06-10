from math import pi
# import math : importe TOUT le module
# from math import pi : importe une partie du module

hauteur = float(input("Saisir la hauteur du cône: "))
rayon = float(input("Saisir le rayon du cône: "))
volume = ((pi * rayon**2) * hauteur) / 3

print(f"Le volume du cône est de {round(volume, 3)}")

# Ici le 0 correspond au nombre de caractères total à afficher
# Ici le 3 correspond au nombre de chiffres après la virgule
# f indique que la variable est de type float
print(f"Le volume du cône est de {volume:0.3f}")
