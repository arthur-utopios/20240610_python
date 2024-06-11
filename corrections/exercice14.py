def note_valide() -> float:
    """
    Saisir une note entre 0 et 20
    """
    note = float(input("Saisir note: "))
    while note < 0 or note > 20:
        print("La note doit être comprise entre 0 et 20")
        note = float(input("Saisir note: "))
    return note


def saisie_nombre_notes():
    nombre_notes = int(input("Combien de notes: "))
    notes = []

    # Lorsque l'itérateur n'est pas utilisé, on peut le nommer '_'
    for _ in range(0, nombre_notes):
        notes.append(note_valide())
    return notes


def saisie_notes_negatives_stop():
    notes = []
    while True:
        note = float(input("Saisir note: "))

        if note < 0 or note > 20:
            break

        notes.append(note)

    return notes


def mode_menu():
    print("Mode de notes")
    print("[1] nombre note défini")
    print("[2] nombre note infini")
    choix = input("Choix: ")

    match choix:
        case "1":
            notes = saisie_nombre_notes()
            min_max_moyenne(notes)
        case "2":
            notes = saisie_notes_negatives_stop()
            min_max_moyenne(notes)
        case _:
            exit()


def min_max_moyenne(notes: list):
    print("Note minimale:", min(notes))
    print("Note maximale:", max(notes))
    print("Moyenne des notes:", round(sum(notes) / len(notes), 2))


if __name__ == "__main__":
    mode_menu()
