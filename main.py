import os
import csv
import random

# --- Deine Challenge-Listen ---
# WICHTIG: Ersetze dies durch deine tatsächlichen Listen von Challenges.
# Stelle sicher, dass du genügend Challenges in jeder Kategorie hast,
# besonders in 'hardChallange' und 'easyChallange', da sie obligatorisch sind.
impossibleChallenge = [
    "Find 3 people with the same shirt as you",
    "Roundtrip to Auchan and back with a purchase under 25 minutes",
    "photograph the K bridge while it's empty",
    'photograph the "before I die" wall while it is empty and open',
    "Stand on the main Stage",

]
hardChallenge = [ 
    "Find 3 people with the same band shirt as you",
    "Sing Karaoke with a stranger",
    "Dance Battle with stranger",
    "Stack 20 cans of beer",
    "Help a stranger set up their tent",
    "Start a conga line through the audience",
    "Get Autographs from 10 Szitizens",
    "Build a human tower with 5 people",
    "Give someone a 'festival survival tip'",
    "Wear 3 different types of hats",
    "Play a song on an improvised instrument",
    "Take the role of a photographer for 5 minutes",
    "Find someone with a Animal costume",
    "Dance to music you've never heard before",
    "Find a 'Lost & Found' item",
    "Exchange a drinking vessel with someone",
    "Create a 'group selfie' with 10 strangers",
    "Build a small sculpture from trash",
    "Get a Szitizenship at the immigration office",
    "Learn a new dance step from a stranger",
    "Learn a sentence in a new language",
    "Find Szitizens from 10 different countries",
    "Share some food/drink with a stranger",
    "Take a selfie with a Dresseed up person",
    "High-5 someone younger than 10 Years old",
    "high-5 someone older than 60 Years old",
    "Find someone with the same name as you",
    "Invent a secret handshake with a friend",
    "Help someone who dropped something",
    "Try 5 different food stands",
    "discover a new band or artist",
    "Find someone who knows your favorite band",
    "Give someone water who drank too much alcohol",
    "Eat a fruit or vegetable (it's healthy!)",
    "Selfie during Sziget Special (Main Stage)",
]

mediumChallenge = [
    "Draw a picture",
    "Do a sportive activity",
    "Collect 3 different drink cups",
    "Take a photo of your favorite decoration",
    "Surprise someone with a small gift"

]

easyChallenge = [
    "Explore a part of the venue where you've never been",
    "Find a festival staff member and take a selfie",
    "Give someone a high-five and ask for their name",
    "Drink a glass of water",
    "Find a blue object",
    "Smile at 5 different people",
    "Eat something new",
    "Find a green meadow",
    "Listen to a song completely",
    "Charge your phone",
    "Take a photo of a flower",
    "Find someone who's laughing",
    "Count 10 different T-shirt colors",
    "Close your eyes for 2 min and just relax",
    "Take a deep breath",
    "Give a friend a compliment",
    "Find an object with at least 3 colors",
    "Draw a simple symbol in the sand",
    "Apply sunscreen",
    "Watch the clouds for a minute"
]

# --- Konfiguration ---
BINGO_SIZE = 5  # Für eine 5x5 Bingo-Karte
OUTPUT_FOLDER = "output"

def create_bingo_card(hard_challenges, medium_challenges, easy_challenges):
    """
    Erstellt eine einzelne, einzigartige Bingo-Karte mit den vorgegebenen Regeln.
    Jede Reihe muss mindestens eine schwere und eine einfache Challenge enthalten.
    """
    card = [["" for _ in range(BINGO_SIZE)] for _ in range(BINGO_SIZE)]
    
    # Mache Kopien der Listen, um Challenges zu entfernen, sobald sie verwendet wurden
    # und um die Original-Listen für weitere Karten unangetastet zu lassen.
    available_hard = list(hard_challenges)
    available_medium = list(medium_challenges)
    available_easy = list(easy_challenges)
    
    random.shuffle(available_hard)
    random.shuffle(available_medium)
    random.shuffle(available_easy)

    # Stelle sicher, dass wir genug Challenges haben
    if len(available_hard) < BINGO_SIZE or len(available_easy) < BINGO_SIZE:
        raise ValueError("Nicht genügend schwere oder einfache Challenges für alle Reihen verfügbar.")
    
    used_challenges = set()

    for r in range(BINGO_SIZE):
        row_challenges = []
        
        # 1. Eine schwere Challenge auswählen
        while True:
            if not available_hard:
                # Falls alle schweren Challenges aufgebraucht sind, mischen wir die verwendeten
                # schweren Challenges und nutzen sie erneut, um sicherzustellen, dass jede Reihe
                # eine schwere Challenge hat. Im Kontext eines einzigartigen Sets pro Karte
                # ist das ein Kompromiss. Realistisch solltest du genug Challenges haben.
                print("Warnung: Nicht genug einzigartige schwere Challenges. Nutze bereits verwendete.")
                available_hard = list(hard_challenges) # Re-use for the sake of the rule
                random.shuffle(available_hard)
            
            challenge = available_hard.pop()
            if challenge not in used_challenges:
                row_challenges.append(challenge)
                used_challenges.add(challenge)
                break

        # 2. Eine einfache Challenge auswählen
        while True:
            if not available_easy:
                print("Warnung: Nicht genug einzigartige einfache Challenges. Nutze bereits verwendete.")
                available_easy = list(easy_challenges) # Re-use
                random.shuffle(available_easy)

            challenge = available_easy.pop()
            if challenge not in used_challenges:
                row_challenges.append(challenge)
                used_challenges.add(challenge)
                break
        
        # 3. Restliche Felder der Reihe mit zufälligen Challenges füllen
        # Wir kombinieren alle verbleibenden ungenutzten Challenges und mischen sie.
        # Wichtig: Vermeide Dopplungen auf der gleichen Karte.
        
        # Erstelle eine temporäre Liste aller noch nicht verwendeten Challenges
        all_remaining = [c for c in hard_challenges + medium_challenges + easy_challenges if c not in used_challenges]
        random.shuffle(all_remaining)

        while len(row_challenges) < BINGO_SIZE:
            if not all_remaining:
                # Sollte nicht passieren, wenn genügend Challenges insgesamt vorhanden sind
                print("Warnung: Nicht genügend einzigartige Challenges, um die Karte zu füllen. Nutze bereits verwendete.")
                # Hier könnte man eine Strategie implementieren, um bereits verwendete aber nicht in dieser Reihe
                # vorhandene Challenges zu verwenden, oder die Schleife beenden.
                break 

            challenge = all_remaining.pop()
            if challenge not in used_challenges: # Doppelte Prüfung, sollte aber durch `all_remaining` schon abgedeckt sein
                row_challenges.append(challenge)
                used_challenges.add(challenge)
        
        # Mische die Challenges in der aktuellen Reihe, um die Positionen von hart/einfach zu randomisieren
        random.shuffle(row_challenges)
        card[r] = row_challenges

    return card

def save_card_to_csv(card, card_number, output_dir):
    """Speichert die generierte Bingo-Karte in einer CSV-Datei."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_name = os.path.join(output_dir, f"bingo_karte_{card_number:03d}.csv")
    
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Schreibe Zeilen in die CSV
        for row in card:
            writer.writerow(row)
    print(f"Karte {card_number:03d} gespeichert in: {file_name}")

if __name__ == "__main__":
    # Zähler für die Kartennummer
    card_counter_file = os.path.join(OUTPUT_FOLDER, "card_counter.txt")
    
    current_card_number = 1
    if os.path.exists(card_counter_file):
        with open(card_counter_file, 'r') as f:
            try:
                current_card_number = int(f.read().strip()) + 1
            except ValueError:
                current_card_number = 1 # Fallback, wenn Datei leer oder korrupt

    print(f"Generiere Bingo-Karte Nummer {current_card_number}...")
    try:
        new_card = create_bingo_card(hardChallange, mediumChallange, easyChallange)
        save_card_to_csv(new_card, current_card_number, OUTPUT_FOLDER)
        
        # Aktualisiere den Zähler für die nächste Ausführung
        with open(card_counter_file, 'w') as f:
            f.write(str(current_card_number))
            
    except ValueError as e:
        print(f"Fehler beim Generieren der Karte: {e}")
        print("Bitte stelle sicher, dass du genügend Challenges in deinen Listen hast.")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")