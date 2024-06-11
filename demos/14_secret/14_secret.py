import os


def show_menu():
    while True : 
        print("""Faites votre choix :
        1 - Voir le secret, 
        2 - Modifier le secret,
        3 - Quitter le programme""")
        choix = input("Votre choix (1|2|3) : ")

        if choix in "123" and len(choix) == 1:
            return choix
        else:
            print("Erreur, réessayez !\n\n")


def lire_fichier(path):
    file = open(path, "r", encoding="UTF-8")
    texte_fichier = file.read()
    file.close()
    return texte_fichier


def ecrire_fichier(path, texte_a_ecrire):
    file = open(path, 'w', encoding="UTF-8")
    file.write(texte_a_ecrire)
    file.close()


def main():
    path = "./secret.txt"
    secret = ""
    if os.path.exists(path):
        secret = lire_fichier(path)
    else:
        print("Secret n'existe pas encore! Veuillez saisir un premier secret : ")
        secret = input()

    while True :
        choix = show_menu()

        match choix:
            case "1":
                print("Voici le secret : ")
                print(secret)
            case "2":
                print("Veuillez saisir le nouveau secret : ")
                secret = input()
            case "3": # pareil que <case _:> car on vérifie si 1,2 ou 3 dans show_menu
                print("On quitte le programme! Donc on sauvegarde le sercret...")
                ecrire_fichier(path, secret)
                break #ou exit() ou return
        

if __name__ == "__main__":
    main()