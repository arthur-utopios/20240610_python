# bool : False, True
# str : 'toto' '124abc'
# int : 1, 4, 123
# float : 1.1, 135.2


def verification_adn(adn: str) -> bool:
    for lettre in adn:
        if lettre not in "atcg":
            return False
    return True


# print(verification_adn('atcgggtca'))
# print(verification_adn('atcgggtcax'))


def saisie_adn(question: str) -> str:
    # lower permet de récupérer la chaîne en minuscule
    # AtCgefe -> atcgefe
    chaine = input(question).lower()

    # Tant que l'adn saisi est invalide, on ne sort pas de la boucle
    while not verification_adn(chaine):
        print("Erreur de saisie!")
        chaine = input(question).lower()

    return chaine


def calculer_proportion(sequence: str, chaine: str) -> float:
    # 'atagcatgc'.count('at') => 2
    ocurrence = chaine.count(sequence)
    return (ocurrence * len(sequence) / len(chaine)) * 100


def main() -> None:
    sequence = saisie_adn("Saisir sequence: ")
    chaine = saisie_adn("Saisir chaine: ")

    proportion  = calculer_proportion(sequence, chaine)

    print(f"Dans la chaine '{chaine}' il y a {proportion:0.2f}% de la séquence '{sequence}'")

main()

