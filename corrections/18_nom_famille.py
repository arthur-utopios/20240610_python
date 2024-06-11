def main_menu():
    while True:
        print("=== MENU PRINCIPAL ===")
        print("1. Voir les noms de famille")
        print("2. Ajouter un nom de famille")
        print("3. Editer un nom de famille")
        print("4. Supprimer un nom de famille")
        print("0. Quitter le programme")
        choice = input("Votre choix : ")
        if choice in "12340" and len(choice) == 1:
            return choice
        else:
            print("Erreur, réessayez !\n")


# permet de gérer les choix, retourne un booleen pour savoir si on continue le programme
def handle_choice(choice, lastnames):
    match choice:
        case "1":
            display_lastnames(lastnames)
        case "2":
            lastnames.add(input_lastname())
        case "3":
            # #version 1
            # # on supprime le nom, peu importe si il existe ou non
            # lastnames.discard(input_lastname())
            # #on en saisi un nouveau
            # lastnames.add(input_lastname())

            #version 2
            ln = input_lastname()
            if ln not in lastnames: # on vérifie d'abord si il existe
                print("Nom non trouvé...")
            else:
                lastnames.discard(ln)
                lastnames.add(input_lastname())
        case "4":
            lastnames.discard(input_lastname())
        case "0":
            # si on s'arrête, on ne renvoie pas le set car c'est inutile
            return False, None
    # retourne la variable pour savoir si on continue 
    # ainsi que notre liste de noms de famille
    return True, lastnames

def display_lastnames(lastnames):
    print("=== LISTE NOMS DE FAMILLE ===")
    for lastname in lastnames:
        print(lastname)
    
    # même chose avec la list comprhension
    # [print(ln) for ln in lastnames]

def input_lastname():
    return input("Saisir un nom : ").upper()



def main():
    set_lastnames = set()
    suivant = True
    while suivant:
        choice = main_menu()
        suivant, set_lastnames = handle_choice(choice, set_lastnames)


if __name__ == "__main__":
    main()




# VERSION 2, avec plus de choses directement dans le main

# def main_menu():
#     while True:
#         print("=== MENU PRINCIPAL ===")
#         print("1. Voir les noms de famille")
#         print("2. Ajouter un nom de famille")
#         print("3. Editer un nom de famille")
#         print("4. Supprimer un nom de famille")
#         print("0. Quitter le programme")
#         choice = input("Votre choix : ")
#         if choice in "12340" and len(choice) == 1:
#             return choice
#         else:
#             print("Erreur, réessayez !\n")
    

# def print_lastnames(lastnames):
#     print("=== LISTE NOMS DE FAMILLE ===")
#     [print(ln) for ln in lastnames]


# def input_lastname():
#     return input("Saisir un nom de famille : ").upper()


# def main():
#     lastnames = set()
#     while True:
#         choice = main_menu()
#         match choice:
#             case "1":
#                 print_lastnames(lastnames)
#             case "2":
#                 lastnames.add(input_lastname())
#             case "3":
#                 ln = input_lastname()
#                 if ln not in lastnames:
#                     print("Nom non trouvé...")
#                 else:
#                     lastnames.discard(ln)
#                     lastnames.add(input_lastname())
#             case "4":
#                 lastnames.discard(input_lastname())
#             case "0":
#                 break


# if __name__ == '__main__':
#     main()