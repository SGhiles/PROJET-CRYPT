# Chiffrement et déchiffrement César sur un fichier .txt #

alphabet = "abcdefghijklmnopqrstuvwxyz"

choix = input("(C)hiffrer ou (D)écrypter ? ").upper()
if choix != "C" and choix != "D":
    print("Erreur : vous devez taper C ou D. ")
    exit()

nom_fichier = input("Nom du fichier a modifier (.txt) : ")

cle = int(input("Entrez une clef (1-25): "))
if choix == "D":
    cle = -cle


read = open(nom_fichier, "r") #lecture du ficher#
texte = read.read().lower()
read.close()

backup = nom_fichier.replace(".txt", "") + "_backup.txt"

backup = open(backup, "w") # sauvegarde le contenu lu#
backup.write(texte)   
backup.close()

resultat = ""
for elm in texte:
    if elm in alphabet:
        i = alphabet.index(elm)
        resultat += alphabet[(i + cle) % 26]
    else:
        resultat += elm


write = open(nom_fichier, "w") #ecriture du fichier#
write.write(resultat)
write.close()

print("Succès !")