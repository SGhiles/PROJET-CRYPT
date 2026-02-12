# Chiffrement / déchiffrement César sur un fichier texte #

alphabet = "abcdefghijklmnopqrstuvwxyz"

action = input("(C)hiffrer ou (D)écrypter ? ").upper()
if action != "C" and action != "D":
    print("Erreur : vous devez taper C ou D.")
    raise SystemExit

nom_fichier = input("Nom du fichier a modifier (.txt) : ")

cle = int(input("Entrez une clef (1-25): "))
if action == "D":
    cle = -cle


read = open(nom_fichier, "r") #lecture du ficher#
texte = read.read().lower()
read.close()

resultat = ""
for car in texte:
    if car in alphabet:
        i = alphabet.index(car)
        resultat += alphabet[(i + cle) % 26]
    else:
        resultat += car


write = open(nom_fichier, "w") #ecriture du fichier#
write.write(resultat)
write.close()

print("Succès !")