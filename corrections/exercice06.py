nombre_table = int(input("Nombre tables: "))

while nombre_table <= 0:
    print("/!\\ nombre inférieur à zéro !!!")
    nombre_table = int(input("Nombre tables: "))

# Boucle qui gère le nombre de table
for table in range(1, nombre_table + 1):
    print(f"== TABLE DE {table} ==")
    for multiplicateur in range(1, 11):
        print(f"{table} x {multiplicateur} = {table * multiplicateur}")
    print()