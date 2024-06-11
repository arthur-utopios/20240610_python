import json, os

file_path = './dogs.json'

def load_dogs():
    dogs = []

    if os.path.exists(file_path):
        file = open(file_path, 'rt')
        dogs = json.load(file)
        file.close()
    else:
        file = open(file_path, 'w')
        file.close()
        
    return dogs

def save_dogs(dogs):
    file = open(file_path, 'w')
    json.dump(dogs, file, indent=4)
    file.close()

if __name__ == '__main__':
    dogs = load_dogs()

    while True:
        print('\n=== MENU PRINCIPAL ===\n')
        print('1. Voir les chiens')
        print('2. Ajouter un chien')
        print('0. Quitter le programme')

        main_choice = int(input('Veuilliez choisir une fonctionnalité : '))

        if main_choice == 1:
            print("\nListe des chiens")
            for dog in dogs:
                print(f"  - {dog}")
        elif main_choice == 2:
            dog_name = input("Veuilliez donner le nom du chien : ")
            dogs.append(dog_name)
            print(f"{dog_name} ajouté à la liste des chiens")
        elif main_choice == 0:
            save_dogs(dogs)
            break
        else: 
            print("Ce choix n'est pas valide !")