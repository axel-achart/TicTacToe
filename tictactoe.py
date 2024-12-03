""" WINABLE OU NON
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
        break
elif rempli() == True:
    print("Match nul")"""


## FIRST VERSION (1V1)

board = [" "] * 9
emplacement = {
    "E1": ["1", "2", "3"],
    "E2": ["4", "5", "6"],
    "E3": ["7", "8", "9"]
}


# Afficher le tableau de jeu
def whiteboard():
    print("Tableau de jeu TicTacToe :")
    print(board[0], " | ", board[1], " | ", board[2])
    print("-------------")
    print(board[3], " | ", board[4], " | ", board[5])
    print("-------------")
    print(board[6], " | ", board[7], " | ", board[8])


# Vérifie si un joueur a gagné ou si c'est un match nul
def check_winner():
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
                            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
                            [0, 4, 8], [2, 4, 6]]            # Diagonales

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]  # Retourne le gagnant ('X' ou 'O')
    if " " not in board:
        return "draw"  # Match nul
    return None  # Pas encore de gagnant, ça rejoue

print()
whiteboard()
print()

# Demande des emplacements
question_1 = input("Si vous voulez afficher le tableau des emplacements, entrez 'o' pour OUI ou 'n' pour NON : ")
if question_1 == "o" or question_1 == "O" or question_1 == "OUI" or question_1 == "oui":
    print("Voici le tableau comportant les emplacements attribués :")
    print(emplacement["E1"])
    print(emplacement["E2"])
    print(emplacement["E3"])
    print()
elif question_1 == "n" or question_1 == "N" or question_1 == "NON" or question_1 == "non":
    print("Le tableau des emplacements ne s'affiche pas\n")


# Choix des signes pour les joueurs
joueur_1 = input("Joueur 1 : Choisissez votre signe entre 'X' et 'O' : ").upper()
while joueur_1 not in ['X', 'O']:
    joueur_1 = input("Choix invalide. Choisissez 'X' ou 'O' : ").upper()

if joueur_1 == 'X':
    joueur_2 = 'O'  
else: 
    joueur_2 = 'X'
print(f"Le joueur 2 a le signe '{joueur_2}'")


# Boucle principale du jeu
current_player = joueur_1
for turn in range(9):
    whiteboard()
    print(f"C'est au tour du joueur avec le signe '{current_player}'")
    while True:
        try:
            choix = int(input("Où voulez-vous jouer (1-9) ? ")) - 1
            if choix < 0 or choix > 8 or board[choix] != " ":
                raise ValueError     # permet à l'utilisateur de lever lui‑même l'exception de son choix, ici "l'erreur"
            board[choix] = current_player
            break
        except ValueError:  # la clause except traite non seulement la classe d'exception qu'elle mentionne, mais aussi toutes les classes dérivées de cette classe
            print("Entrée invalide ou case déjà occupée. Réessayez.")

    # Vérifie s'il y a un gagnant ou un match nul
    result = check_winner()
    if result:
        whiteboard()
        if result == "draw":
            print("Match nul !")
        else:
            print(f"Le joueur avec le signe '{result}' a gagné !")
        break

    # Change de joueur
    if current_player == joueur_1:
        current_player = joueur_2 
    else: 
        current_player = joueur_1

# Si personne n'a gagné après les 9 tours
if not result:
    whiteboard()
    print("Match nul !")