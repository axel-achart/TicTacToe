"""Faire des "grilles" (Pour IA/Dev Log)

# Si toutes les cases utilisés mais pas d'alignement =  match nul
# 3 cases alignés (horizontal, vertical, diagonal[2]) = match gagné

# Si tout le jeu est fini, faire le "bonus" :
# - qui joue le first coup (IA) : Dans un autre fichier

# Faire un tableau de jeu différent (en affichant les barres vertical)
# plateau = [''] * 9
# print(f"| {plateau[0]} |", f"| {plateau[1]} |", f"| {plateau[2]} |")
# print(f"| {plateau[3]} |", f"| {plateau[4]} |", f"| {plateau[5]} |")
# print(f"| {plateau[7]} |", f"| {plateau[8]} |", f"| {plateau[9]} |")"""




## FIRST VERSION (1V1)

# Dictionnaires définis
board=[" ",]*9
emplacement = {
    "E1" : ["1", "2", "3"],
    "E2" : ["4", "5", "6"],
    "E3" : ["7", "8", "9"]
}

# Afficher le tableau de jeu vide
print()
def whiteboard():
    print("Tableau de jeu TicTacToe :")
    print(board[0], " | ", board[1], " | ", board[2])
    print("-------------")
    print(board[3], " | ", board[4], " | ", board[5])
    print("-------------")
    print(board[6], " | ", board[7], " | ", board[8])
whiteboard()
print()

#---------------------------------------------------------------------------------------
# Demande et affichage (ou non) du tableau avec les emplacements
question_1 = input("Si vous voulez afficher le tableau des emplacements, entrez 'o' pour OUI ou 'n' pour NON : ")
if question_1 == "o":
    print()
    print("Voici le tableau comportant les emplacements attribués :")
    print(emplacement["E1"])
    print(emplacement["E2"])
    print(emplacement["E3"])
    print()
elif question_1 == "n":
    print()
    print("Le tableau des emplacements ne s'affiche pas")
    print()
#---------------------------------------------------------------------------------------

# Fonction vérification si la grille est rempli ou non
def rempli():
    for i in board:
        if i == "":
            return False  # Si le tableau contient encore une/des cases vides
        else:
            return True  # Si le tableau ne contient plus de case vide

# Fonction Match Nul
def draw(board):
    if all(c != " " for row in board for c in row):
        return True
    return False

# Fonction pour gagner
def winable():
    if ((board[0] == board[1] == board[2] != "") or # WIN Lignes
            (board[3] == board[4] == board[5] != "") or
            (board[6] == board[7] == board[8] != "") or
            (board[0] == board[3] == board[6] != "") or # WIN Colonnes
            (board[1] == board[4] == board[7] != "") or
            (board[2] == board[5] == board[8] != "") or
            (board[0] == board[4] == board[8] != "") or # WIN Diagonales
            (board[6] == board[4] == board[2] != "")):
            whiteboard()
            print("Le joueur 2 a gagné")

# Proposition pour où jouer
for h in range(1):
    joueur_1 = input("Joueur 1 : Choisissez votre signe entre 'X' et 'O' : ")
    joueur_2 = ''
    if joueur_1 == 'X':
        joueur_2 = 'O'
        print()
        print("Alors le joueur 2 a le signe 'O'")
    elif joueur_1 == 'O':
        joueur_2 = 'X'
        print()
        print("Alors le joueur 2 a le signe 'X'")
    else:
        continue
    print()


# MAIN
while winable() == False:
    print()
    whiteboard()
    print()
    choix_1 = int(input("Joueur 1 : Où voulez-vous jouer ? "))
    if 1 <= choix_1 <= 9:    # Joueur  1
        for pas_à_pas in board:   
            board[choix_1 - 1] = joueur_1
    if ((board[0] == board[1] == board[2] != "") or # WIN Lignes
            (board[3] == board[4] == board[5] != "") or
            (board[6] == board[7] == board[8] != "") or
            (board[0] == board[3] == board[6] != "") or # WIN Colonnes
            (board[1] == board[4] == board[7] != "") or
            (board[2] == board[5] == board[8] != "") or
            (board[0] == board[4] == board[8] != "") or # WIN Diagonales
            (board[6] == board[4] == board[2] != "")):
            whiteboard()
            print("Le joueur 1 a gagné")
            
                
    whiteboard()
    print()
    choix_2 = int(input("Joueur 2 : Où voulez-vous jouer ? "))
    if 1 <= choix_1 <= 9:    # Joueur  2
        for pas_à_pas in board:
            board[choix_2 - 1] = joueur_2
    if ((board[0] == board[1] == board[2] != "") or # WIN Lignes
            (board[3] == board[4] == board[5] != "") or
            (board[6] == board[7] == board[8] != "") or
            (board[0] == board[3] == board[6] != "") or # WIN Colonnes
            (board[1] == board[4] == board[7] != "") or
            (board[2] == board[5] == board[8] != "") or
            (board[0] == board[4] == board[8] != "") or # WIN Diagonales
            (board[6] == board[4] == board[2] != "")):
            whiteboard()
            print("Le joueur 2 a gagné")
           
                
    else:
        print("Coup non autorisé, réessayez avec un chiffre entre 1 et 9")