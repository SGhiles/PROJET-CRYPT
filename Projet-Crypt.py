# Projet Final: Chiffrement de fichiers texte (Modification directe)
liste = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

mode = input("(C)hiffrer ou (D)écrypter ? ").upper()
while mode not in ['C', 'D']:
    mode = input("(C)hiffrer ou (D)écrypter ? ").upper()

nom_fichier = input("Nom du fichier à modifier (.txt) : ")
clef = int(input('Entrez votre clef (1-25): '))

if mode == 'D':
    clef = -clef

def chiffrage(lettre, liste, clef):
    if lettre == ' ':
        return ' '
    if lettre in liste:
        for i in range(len(liste)):
            if liste[i] == lettre:
                return str(liste[(i + clef) % 26]) #le %26 : Permet de rester entre 0 et 25 (alphabet)
    return lettre


try:
    # 1. Lecture du contenu original
    with open(nom_fichier, 'r', encoding='utf-8') as f:
        contenu = f.read().lower()

    # 2. Transformation du texte
    message_final = ""
    for lettre in contenu:
        message_final += chiffrage(lettre, liste, clef)

    # 3. Écrasement du fichier original avec le nouveau message
    with open(nom_fichier, 'w', encoding='utf-8') as f:
        f.write(message_final)

    print(f"Le fichier '{nom_fichier}' a été mis à jour avec succès !")

except FileNotFoundError:
    print("Erreur : Impossible de trouver le fichier spécifié.")