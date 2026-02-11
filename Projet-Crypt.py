#Projet Final: Chiffrement de fichiers texte#

liste=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# --- BOUCLE DE VALIDATION DU MODE ---
mode = input("Voulez-vous (C)hiffrer ou (D)écrypter ? ").upper()

while mode not in ['C', 'D']:
    print("Erreur : Veuillez entrer uniquement 'C' pour chiffrer ou 'D' pour décrypter.")
    mode = input("Voulez-vous (C)hiffrer ou (D)écrypter ? ").upper()

# ------------------------------------

message = input('Entrez votre message : ').lower()
clef = int(input('Entrez votre clef : '))

# Si on décrypte, on inverse simplement la clé
if mode == 'D':
    clef = -clef

def chiffrage_lettre(lettre, liste, clef):
    if lettre == ' ':
        return ' '
    for i in range(len(liste)):
        if liste[i] == lettre:
            return str(liste[(i + clef) % 26])
    return '?'

message_final = ""

for lettre in message:
    message_final += chiffrage_lettre(lettre, liste, clef)

print(f"Résultat : {message_final}")