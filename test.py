# Chiffrement / déchiffrement César sur un fichier texte (version simple)

alphabet = "abcdefghijklmnopqrstuvwxyz"

mode = input("(C)hiffrer ou (D)écrypter ? ").upper()
while mode != "C" and mode != "D":
    mode = input("(C)hiffrer ou (D)écrypter ? ").upper()

nom_fichier = input("Nom du fichier à modifier (.txt) : ")

clef = int(input("Entrez votre clef (1-25): "))
if mode == "D":
    clef = -clef

try:
    with open(nom_fichier, "r", encoding="utf-8") as f:
        texte = f.read().lower()

    resultat = ""
    for car in texte:
        if car in alphabet:
            i = alphabet.index(car)
            resultat += alphabet[(i + clef) % 26]
        else:
            resultat += car  # garde espaces, ponctuation, chiffres, etc.

    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(resultat)

    print("Fichier modifié avec succès !")

except FileNotFoundError:
    print("Erreur : fichier introuvable.")
    
