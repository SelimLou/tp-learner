import random # importation de random, pour les evenements aléatoires
import time # Pour pas qu'il se ferme soudainement à la fin
# Dictionnaire de verbes et de leurs formes
verbes = {
    "Respecter / se conformer à ": ["abide", "abode", "abode"],
    "Survenir": ["arise", "arose", "arisen"],
    "Se réveiller": ["awake", "awoke", "awoken"],
    "Être": ["be", "was/were", "been"],
    "Porter / Supporter / Naître": ["bear", "bore", "born"],
    "Battre": ["beat", "beat", "beaten"],
    "Devenir": ["become", "became", "become"],
    "Engendrer": ["beget", "begot", "begotten"],
    "Commencer": ["begin", "began", "begun"],
    "Plier": ["bend", "bent", "bent"],
    "Déposséder / Priver": ["bereave", "bereaved", "bereaved"],
    "Parier": ["bet", "bet", "bet"],
    "Enchérir": ["bid", "bid", "bid"],
    "Saigner": ["bleed", "bled", "bled"],
    "Souffler": ["blow", "blew", "blown"],
    "Casser": ["break", "broke", "broken"],
    "Élever (des animaux)": ["breed", "bred", "bred"],
    "Apporter": ["bring", "brought", "brought"],
    "Émettre": ["broadcast", "broadcast", "broadcast"],
    "Construire": ["build", "built", "built"],
    "Brûler": ["burn", "burnt", "burnt"],
    "Éclater": ["burst", "burst", "burst"],
    "Acheter": ["buy", "bought", "bought"],
    "Pouvoir": ["can", "could", "could"],
    "Jeter / Distribuer des rôles": ["cast", "cast", "cast"],
    "Attraper": ["catch", "caught", "caught"],
    "gronder": ["chide", "chid", "chiden"],
    "choisir": ["choose", "chose", "chosen"],
    "s'accrocher": ["cling", "clung", "clung"],
    "habiller / recouvrir": ["clothe", "clothed", "clothed"],
    "venir": ["come", "came", "come"],
    "coûter": ["cost", "cost", "cost"],
    "ramper": ["creep", "crept", "crept"],
    "couper": ["cut", "cut", "cut"],
    "distribuer": ["deal", "dealt", "dealt"],
    "creuser": ["dig", "dug", "dug"],
    "plonger": ["dive", "dived", "dived"],
    "faire": ["do", "did", "done"],
    "dessiner / tirer": ["draw", "drew", "drawn"],
    "rêver": ["dream", "dreamt", "dreamt"],
    "boire": ["drink", "drank", "drunk"],
    "conduire": ["drive", "drove", "driven"],
    "habiter": ["dwell", "dwelt", "dwelt"],
    "manger": ["eat", "ate", "eaten"],
    "tomber": ["fall", "fell", "fallen"],
    "nourrir": ["feed", "fed", "fed"],
    "se sentir / ressentir": ["feel", "felt", "felt"],
    "se battre": ["fight", "fought", "fought"],
    "trouver": ["find", "found", "found"],
    "s'enfuir": ["flee", "fled", "fled"],
    "lancer": ["fling", "flung", "flung"],
    "voler (avion)": ["fly", "flew", "flown"],
    "interdire": ["forbid", "forbade", "forbidden"],
    "prévoir": ["forecast", "forecast", "forecast"],
    "oublier": ["forget", "forgot", "forgot"],
    "pardonner": ["forgive", "forgave", "forgiven"],
    "abandonner": ["forsake", "forsook", "forsaken"],
    "prévoir / présentir": ["forsee", "foresaw", "foresawn"],
    "geler": ["freeze", "froze", "frozen"],
    "obtenir": ["get", "got", "got"],
    "donner": ["give", "gave", "given"],
    "aller": ["go", "went", "gone"],
    "moudre / opprimer": ["grind", "ground", "ground"],
    "grandir / pousser": ["grow", "grew", "grown"],
    "tenir / pendre": ["hang", "hung", "hung"],
    "avoir": ["have", "had", "had"],
    "entendre": ["hear", "heard", "heard"],
    "cacher": ["hide", "hid", "hidden"],
    "taper / appuyer": ["hit", "hit", "hit"],
    "tenir": ["hold", "held", "held"],
    "blesser": ["hurt", "hurt", "hurt"],
    "garder": ["keep", "kept", "kept"],
    "s'agenouiller": ["kneel", "knelt", "knelt"],
    "connaître / savoir": ["know", "knew", "known"],
    "poser": ["lay", "laid", "laid"],
    "mener / guider": ["lead", "led", "led"],
    "s'incliner / se pencher": ["lean", "leant", "leant"],
    "sauter / bondir": ["leap", "leapt", "leapt"],
    "apprendre": ["learn", "learnt", "learnt"],
    "laisser / quitter / partir": ["leave", "left", "left"],
    "prêter": ["lend", "lent", "lent"],
    "permettre / louer": ["let", "let", "let"],
    "s'allonger": ["lie", "lay", "lain"],
    "allumer": ["light", "lit", "lit"],
    "perdre": ["lose", "lost", "lost"],
    "fabriquer": ["make", "made", "made"],
    "signifier": ["mean", "meant", "meant"],
    "rencontrer": ["meet", "met", "met"],
    "tondre": ["mow", "mowed", "mown"]
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

