from rectangle import aire as aire_rectangle


def aire(longueur: int, largeur: int, hauteur: int) -> int:
    return (
        (2 * aire_rectangle(longueur, largeur))
        + (2 * aire_rectangle(longueur, hauteur))
        + (2 * aire_rectangle(largeur, hauteur))
    )

print(aire(3, 6, 2))