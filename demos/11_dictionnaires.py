mon_dico = {}
mon_second_dico = dict()

mon_dico = {"clé": "valeur", 1: 312, "toto": False, "toto": "chips"}

print(mon_dico)
print(mon_dico["clé"])

# Ajouter un element à un dictionnaire
mon_dico["password"] = "azerty"
print(mon_dico)

mon_dico["password"] = "qwerty"
print(mon_dico)

# Parcours des clés
print(mon_dico.keys())
for key in mon_dico.keys():
    print(key)

# Parcours des valeurs
for value in mon_dico.values():
    print(value)

# Parcours des clés et des valeurs
for key, value in mon_dico.items():
    print(key, value)

# Suppression d'une clé d'un dictionnaire
del mon_dico['clé']
print(mon_dico)

mon_dico.update({'id': 1, 'name': 'toto'})
print(mon_dico)