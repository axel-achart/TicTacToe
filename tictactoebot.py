## VERSION (1 VS bot)

import random

# Initialisation
board = [" "] * 9
places = {
    "E1": ["1", "2", "3"],
    "E2": ["4", "5", "6"],
    "E3": ["7", "8", "9"]
}

def whiteboard():
    print("Tableau de jeu TicTacToe :")
    print(board[0], " | ", board[1], " | ", board[2])
    print("-------------")
    print(board[3], " | ", board[4], " | ", board[5])
    print("-------------")
    print(board[6], " | ", board[7], " | ", board[8])

def check_winner():
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
                            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
                            [0, 4, 8], [2, 4, 6]]            # Diagonales

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]  # Retourne le gagnant ('X' ou 'O')
    if " " not in board:
        return "draw"  # Match nul
    return None  # Pas encore de gagnant

# Fonction qui fait jouer le bot
def bot_move(bot_sign, player_sign):
    # Vérifie si le bot peut gagner
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        values = [board[i] for i in combo]
        if values.count(bot_sign) == 2 and values.count(" ") == 1:
            return combo[values.index(" ")]

    # Vérifie si le bot doit bloquer le joueur
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        values = [board[i] for i in combo]
        if values.count(player_sign) == 2 and values.count(" ") == 1:
            return combo[values.index(" ")]

    # Si aucune action critique, joue la première case libre
    for i in range(9):
        if board[i] == " ":
            return i

print()
print("Vous allez jouer contre un bot")
print()
whiteboard()
print()

question_1 = input("Si vous voulez afficher le tableau des emplacements, entrez 'o' pour OUI ou 'n' pour NON : ")
print()
if question_1.lower() in ["o", "oui"]:
    print("Voici le tableau comportant les emplacements attribués :")
    print(places["E1"])
    print(places["E2"])
    print(places["E3"])
    print()
else:
    print("Le tableau des emplacements ne s'affiche pas")

player_sign = input("Joueur : Choisissez votre signe entre 'X' et 'O' : ").upper()
while player_sign not in ['X', 'O']:
    player_sign = input("Choix invalide. Choisissez 'X' ou 'O' : ").upper()

if player_sign == 'X':
    bot_sign = 'O' 
else:
    bot_sign = 'X'
print(f"Le bot joue avec le signe '{bot_sign}'")

def main():
    current_player = "player"
    for turn in range(9):
        whiteboard()
        print()

        if current_player == "player":
            print("C'est votre tour !")
            while True:
                try:
                    choice = int(input("Où voulez-vous jouer (1-9) ? ")) - 1
                    if choice < 0 or choice > 8 or board[choice] != " ":
                        raise ValueError
                    board[choice] = player_sign
                    break
                except ValueError:
                    print("Entrée invalide ou case déjà occupée. Réessayez.")
        else:
            print("C'est au tour du bot...")
            bot_choice = bot_move(bot_sign, player_sign)
            board[bot_choice] = bot_sign

        result = check_winner()
        if result:
            whiteboard()
            if result == "draw":
                print("Match nul !")
            else:
                winner = "Le joueur" if result == player_sign else "Le bot"
                print(f"{winner} a gagné !")
            break

        current_player = "bot" if current_player == "player" else "player"

main()

print()

while True:
    replay = input("Voulez-vous rejouer ? (o/n) : ")
    if replay.lower() in ["o", "oui"]:
        board = [" "] * 9
        main()
    else:
        print("Au revoir !")
        break
