dict_letters_lower = {}
dict_letters_upper = dict()

# for i in range(97, 97 + 26):
for i in range(ord('a'), ord('z')+1):
    dict_letters_lower[chr(i)] = i

# for i in range(65, 65 + 26):
for i in range(ord('A'), ord('Z')+1):
    dict_letters_upper[chr(i)] = i


print("=== ASCII lettres minuscules ===")
for cle, valeur in dict_letters_lower.items():
    print(f"{cle:^15}-{valeur:^15}")

print("=== ASCII lettres majuscules ===")
for cle, valeur in dict_letters_upper.items():
    print(f"{cle:^15}-{valeur:^15}")

char = input("Saisir un lettre minuscule : ")
print(f"{char}-{dict_letters_lower[char]}")