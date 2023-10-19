import random # importation de random, pour les evenements aléatoires
import time # Pour pas qu'il se ferme soudainement à la fin
# Dictionnaire de verbes et de leurs formes
verbes = {
    "Respecter / se conformer à ": ["abide", "abode", "abode"],
    "Survenir": ["arise", "arose", "arisen"],
    "Engendrer": ["beget", "begot", "begotten"],
    "Déposséder / Priver": ["bereave", "bereaved", "bereaved"],
    "gronder": ["chide", "chid", "chiden"],
    "s'accrocher": ["cling", "clung", "clung"],
    "ramper": ["creep", "crept", "crept"],
    "distribuer": ["deal", "dealt", "dealt"],
    "habiter": ["dwell", "dwelt", "dwelt"],
    "lancer": ["fling", "flung", "flung"],
    "abandonner": ["forsake", "forsook", "forsaken"],
    "prévoir / présentir": ["forsee", "foresaw", "foresawn"],
    "tenir": ["hold", "held", "held"],
    "poser": ["lay", "laid", "laid"],
    "s'allonger": ["lie", "lay", "lain"],
}

# Liste pour suivre les verbes déjà utilisés
verbes_utilises = []

# Fonction pour obtenir un nouveau verbe non utilisé
def obtenir_nouveau_verbe():
    verbes_disponibles = [verbe for verbe in verbes.keys() if verbe not in verbes_utilises]
    if verbes_disponibles:
        return random.choice(verbes_disponibles)
    else:
        print("WOOHOO ! Bien joué ! Tu as fini les 88 verbes !")
        return None

# Fonction pour obtenir toutes les formes d'un verbe donné
def obtenir_formes(verbe):
    return verbes.get(verbe, ["Verbe introuvable"])

# Jeu principal
print("Bienvenue dans le jeu des verbes irréguliers !")
print("Vous devez deviner toutes les formes d'un verbe donné. Tu peux quitter en écrivant --> quit")
print("Forme 1 : Infinitif (sans le to); Forme 2 : Prétérit (past simple); Forme 3 : Participe passé (past continuous)")
while True: # Boucle principale
    verbe = obtenir_nouveau_verbe()
    if verbe is None:
        time.sleep(3)
        break  # Tous les verbes ont été utilisés
    print(f"\nTrouvez les trois formes du verbe : {verbe}")
    verbes_utilises.append(verbe)  # Ajouter le verbe à la liste des verbes utilisés
    formes = obtenir_formes(verbe)
    for i, formes in enumerate(formes):
        guess = input(f"Forme {i+1}: ")  
        if guess == formes: #Vérification de la réponse.
            print("Correct !")
        elif guess.lower() == 'quit':
            print("Merci d'avoir joué !")
            time.sleep(3)
            break
        else:
            print(f"Désolé, la réponse correcte était : {formes}")

