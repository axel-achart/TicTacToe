# INITIALISATION/

plateau = ['']*9
print(plateau)

# FONCTION D'AFFICHAGE DU PLATEAU/

def afficher_plateau():
    print('----------')
    print('|',plateau[0],'|',plateau[1],'|',plateau[2],'|')
    print('----------')
    print('|',plateau[3],'|',plateau[4],'|',plateau[5],'|')
    print('----------')
    print('|',plateau[6],'|',plateau[7],'|',plateau[8],'|')
    print('----------')
    print(afficher_plateau(plateau))

    # FONCTION A VERIFIER SI UN JOUEUR GAGNE
# VERIFICATION DES LIGNES,COLONNES,DIAGONALES

    def verifier_victoire(joueur):
        return((plateau[0]==plateau[1]==plateau[2]) or
        (plateau[3]==plateau[4]==plateau[5]) or
        (plateau[6]==plateau[7]==plateau[8]) or
        (plateau[0]==plateau[3]==plateau[6]) or
        (plateau[1]==plateau[4]==plateau[7]) or
        (plateau[2]==plateau[5]==plateau[8]) or
        (plateau[0]==plateau[4]==plateau[8]) or
        (plateau[2]==plateau[4]==plateau[6]))
print(verifier_victoire(joueur))

# FONCTION POUR LE TOUR DU JOUEUR

def tour_joueur(joueur):
    while True:
     position = int(input(f"joueur{joueur},choissisez une position(1-9):")) -1
     if 0 <= position <= 8 and plateau [position] == '':
                plateau [position] = joueur
                break
        else: 
                print("position invalide.réessayer.")
        except ValueError:
        print("entrée invalide,veuillez entrz un nombre entre 1 et 9.")



    
