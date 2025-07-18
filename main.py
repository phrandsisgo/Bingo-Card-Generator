import os
import csv
import random

# --- Deine Challenge-Listen ---
# WICHTIG: Ersetze dies durch deine tatsächlichen Listen von Challenges.
# Stelle sicher, dass du genügend Challenges in jeder Kategorie hast,
# besonders in 'hardChallange' und 'easyChallange', da sie obligatorisch sind.
hardChallange = [
    "Finde 3 Leute mit dem gleichen Bandshirt wie du",
    "Singe auf der Open-Mic-Bühne",
    "Überrede jemanden zu einem spontanen Tanz-Battle",
    "Organisiere einen Gruppen-Jubel für einen Act",
    "Finde einen Künstler backstage und hol ein Autogramm",
    "Hilf einem fremden, sein Zelt aufzubauen",
    "Verkleide dich spontan mit Festival-Fundstücken",
    "Starte eine Polonaise durch das Publikum",
    "Finde jemanden, der noch nie auf einem Festival war und erzähl ihm vom besten Moment",
    "Baue einen menschlichen Turm mit 5 Personen",
    "Gebe jemandem einen 'Festival-Survival-Tipp'",
    "Finde 3 verschiedene Arten von Hüten",
    "Spiele ein Lied auf einem improvisierten Instrument",
    "Übernimm für 5 Minuten die Rolle eines Fotografen",
    "Finde jemanden mit einem Einhorn-Kostüm",
    "Tanze zu Musik, die du noch nie gehört hast",
    "Finde einen 'Lost & Found' Gegenstand",
    "Tausche ein Trinkgefäß mit jemandem",
    "Erstelle ein 'Gruppen-Selfie' mit 10 Fremden",
    "Baue eine kleine Skulptur aus Müll"
]

mediumChallange = [
    "Lerne einen neuen Tanzschritt von einem Fremden",
    "Tausche ein Armband mit jemandem",
    "Finde ein Objekt in der Farbe deiner Wahl und mach ein Foto",
    "Gib jemandem ein Kompliment",
    "Schreib einen positiven Satz auf eine Serviette und gib sie weiter",
    "Finde 5 Leute aus 5 verschiedenen Ländern",
    "Sammel 3 verschiedene Festival-Flyer",
    "Mach ein Selfie mit einem Festival-Maskottchen",
    "Finde den ältesten und den jüngsten Festival-Besucher",
    "Hilf jemandem, der etwas fallen gelassen hat",
    "Erkunde eine Ecke des Geländes, wo du noch nie warst",
    "Versuche 3 neue Essensstände aus",
    "Finde jemanden, der deine Lieblingsband kennt",
    "Erfinde einen geheimen Handshake mit einem Freund",
    "Zeichne ein kleines Bild auf den Boden mit Kreide",
    "Sammle 3 verschiedene Getränkebecher",
    "Mach ein Foto von deiner Lieblingsdeko",
    "Lerne ein Wort in einer neuen Sprache von einem Fremden",
    "Finde den lustigsten Festival-Hut",
    "Überrasche jemanden mit einem kleinen Geschenk"
]

easyChallange = [
    "Finde einen Festival-Mitarbeiter und mach ein Selfie",
    "Gib jemandem ein High-Five und frag nach dem Namen",
    "Trink ein Glas Wasser",
    "Finde einen blauen Gegenstand",
    "Lächle 5 verschiedenen Leuten zu",
    "Iss etwas Neues",
    "Finde eine grüne Wiese",
    "Höre dir einen Song komplett an",
    "Tanke dein Handy auf",
    "Mach ein Foto von einer Blume",
    "Finde jemanden, der lacht",
    "Zähl 10 verschiedene T-Shirt-Farben",
    "Schließ deine Augen für 30 Sekunden und hör zu",
    "Finde eine Sitzgelegenheit und ruh dich aus",
    "Nimm einen tiefen Atemzug",
    "Gib einem Freund ein Kompliment",
    "Finde ein Objekt mit mindestens 3 Farben",
    "Zeichne ein einfaches Symbol in den Sand",
    "Trage Sonnencreme auf",
    "Beobachte die Wolken für eine Minute"
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