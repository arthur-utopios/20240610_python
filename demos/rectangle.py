def aire(longueur: int, largeur: int) -> int:
    return longueur * largeur


def perimetre(longueur: int, largeur: int) -> int:
    return 2 * longueur + 2 * largeur


# Cette condition permet de vérifier si le fichier est exécute comme fichier principal
# Si il est importé comme module, il portera le nom du fichier
# __name__ est une variable spéciale gérée par Python
if __name__ == "__main__":
    print(__name__)  # __main__
    print(perimetre(2, 3))
    print(aire(4, 2))
else:
    print(__name__)  # rectangle
