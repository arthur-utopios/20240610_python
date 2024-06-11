# Never trust user input
def fullname(prenom: str, nom: str) -> None:
    print(prenom.strip(), nom.strip())

# prenom (chaine de caractères) = input() -> chaine -> strip : supprime les espaces avant et après
prenom = input("Saisir prénom: ").strip() # "   arthur   " => "arthur"
nom = input("Saisir nom: ").strip()

fullname(prenom, nom)