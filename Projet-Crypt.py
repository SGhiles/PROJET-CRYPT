# Chiffrement / déchiffrement César sur un fichier texte #

alphabet = "abcdefghijklmnopqrstuvwxyz"

type = input("(C)hiffrer ou (D)écrypter ? ").upper()
if type != "C" and type != "D":
    print("Erreur : vous devez taper C ou D. ")
    exit

nom_fichier = input("Nom du fichier a modifier (.txt) : ")

cle = int(input("Entrez une clef (1-25): "))
if type == "D":
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