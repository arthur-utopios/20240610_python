# Définition de fonction
# def nom_fonction(<paramètres>) -> <type retour>:
def hello_world() -> None:
    print("Hello world!")


# Appel de fonction
hello_world()  # Hello world!
retour_fonction = hello_world()  # None
print(retour_fonction)


# Paramètres fonction
def bonjour_nom(nom: str) -> None:
    print("Bonjour", nom)


bonjour_nom("Arthur")
bonjour_nom(12)
# bonjour_nom() # Type error


# Valeur par défaut
# ALT + SHIFT + F pour formater le code
# Installation de black formatter dans les extensions


# def <nom fonction> (arg: type = valeurDéfaut) -> <type retour>:
def bonjour_toto_defaut(nom: str = "toto") -> None:
    print("Bonjour", nom)


bonjour_toto_defaut()  # Bonjour toto

# print utilise des paramètres par défaut de base
print("Bonjour", "Je", "M'appelle", "Arthur", sep="-")


def addition(a: int, b: int) -> int:
    return a + b


print(addition(1, 6))
resultat = addition(12, 17)
print(resultat)


# Mettre les 3 guillemets en début de fonction permet d'ajouter de la documentation
def documentation() -> None:
    """
    documentation()
    permet d'afficher des choses
    """
    pass


nombre = 12


# /!\ Mauvais pratique !
def out_of_scope():
    return nombre * 12


# Bonne pratique
def in_the_scope(nombre: int):
    return nombre * 12


def scope_variable(rayon: int) -> float:
    pi = 3.14  # pi n'existe qu'à l'intérieur de cette fonction
    return pi * rayon**2


# Pour définir une infinité d'arguments on peut le caractère * devant la variable
def parametres_infini(*args):
    print(type(args))
    for arg in args:
        print(arg)


parametres_infini("toto", "titi", "tata")

# Tout élément itérable peut être parcouru avec la boucle for
for lettre in "Arthur":
    print(lettre)

# arguments, key arguments
def args_kwargs(*args, **kwargs):
    print(type(args), type(kwargs))
    print(args)
    print(kwargs)

args_kwargs(12, 14, key="clé", chien="rex", chat="garfield")

kayak = 'kayak'

# L'opérateur in permet de vérifier la présence d'une occurrence dans un élément
if('aya' in kayak):
    print("aya est dans kayak")