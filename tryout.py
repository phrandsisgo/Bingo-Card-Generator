import openpyxl
from openpyxl.styles import Alignment # Import für die Textausrichtung
import shutil
import os


sentences = [ 
    "Find 3 people with the same band shirt as you",
    "Sing Karaoke with a stranger",
    "Dance Battle with stranger",
    "Stack 20 cans of beer",
    "Help a stranger set up their tent",
    #"Spontaneously dress up with festival findings",
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
    "Find someone with the same name as you"
    "Invent a secret handshake with a friend",
    "Help someone who dropped something",
    "Try 5 different food stands",
    "discover a new band or artist",
    "Find someone who knows your favorite band",
    "Give someone water who drank too much alcohol",
    "Eat a fruit or vegetable (it's healthy!)",
    "Selfie during Sziget Special (Main Stage)",
]

def fill_excel_template(template_path, output_directory, data):
    """
    Kopiert eine Excel-Vorlage, füllt bestimmte Felder aus und speichert sie.
    Setzt zudem automatischen Zeilenumbruch für angegebene Zellen.

    Args:
        template_path (str): Der Pfad zur Excel-Vorlagendatei.
        output_directory (str): Das Verzeichnis, in dem die ausgefüllte Datei gespeichert werden soll.
        data (dict): Ein Dictionary mit den Daten, wobei der Schlüssel der Zellname
                     (z.B. 'A1', 'B5') und der Wert die einzufügenden Daten sind.
    """

    if not os.path.exists(template_path):
        print(f"Fehler: Vorlagendatei nicht gefunden unter {template_path}")
        return

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        print(f"Verzeichnis '{output_directory}' erstellt.")

    # 1. Vorlage kopieren
    # Erstelle einen Dateinamen für die neue Rechnung (z.B. basierend auf der Rechnungsnummer)
    # Annahme: 'invoice_number' ist ein Schlüssel in deinem 'data'-Dictionary
    invoice_number = data.get('B2', 'UNKNOWN') # Annahme: Rechnungsnummer ist in Zelle B2
    output_filename = f"Mappe1.xlsx"
    output_path = os.path.join(output_directory, output_filename)

    try:
        shutil.copy(template_path, output_path)
        print(f"Vorlage kopiert nach: {output_path}")
    except Exception as e:
        print(f"Fehler beim Kopieren der Vorlage: {e}")
        return

    # 2. Kopie laden
    try:
        workbook = openpyxl.load_workbook(output_path)
        sheet = workbook.active # Nimm das aktive (erste) Arbeitsblatt
    except Exception as e:
        print(f"Fehler beim Laden der Arbeitsmappe: {e}")
        return

    # Liste der Zellen, für die ein Zeilenumbruch erzwungen werden soll
    # Füge hier alle Zellen hinzu, für die du automatischen Zeilenumbruch wünschst
    cells_to_wrap = ['B11', 'D11', 'F11', 'H11', 'J11']

    # 3. Zellen befüllen und Formatierung anwenden
    for cell_address, value in data.items():
        try:
            cell = sheet[cell_address]
            cell.value = value
            print(f"Zelle {cell_address} mit '{value}' befüllt.")

            # Setze Zeilenumbruch für die gewünschten Zellen
            if cell_address in cells_to_wrap:
                cell.alignment = Alignment(wrap_text=True)
                print(f"Zeilenumbruch für Zelle {cell_address} gesetzt.")

        except Exception as e:
            print(f"Fehler beim Befüllen/Formatieren der Zelle {cell_address}: {e}")

    # 4. Speichern
    try:
        workbook.save(output_path)
        print(f"Erfolgreich gespeichert: {output_path}")
    except Exception as e:
        print(f"Fehler beim Speichern der Arbeitsmappe: {e}")

# --- Beispielhafte Nutzung ---
if __name__ == "__main__":
    # Pfad zu deiner leeren Excel-Vorlagendatei
    # ACHTUNG: Passe diesen Pfad an!
    template_excel_file = "C:/Users/YourUser/Documents/Rechnungsvorlage.xlsx"

    # Verzeichnis, in dem die ausgefüllten Rechnungen gespeichert werden sollen
    # ACHTUNG: Passe diesen Pfad an!
    output_dir = "C:/Users/YourUser/Documents/Ausgefuellte_Rechnungen"

    # Die Daten, die du in die Excel-Felder einfügen möchtest.
    # Der Schlüssel ist die Zelladresse (z.B. 'A1', 'B2'), der Wert sind die Daten.
    # Du müsstest wissen, welche Zellen in deiner Vorlage befüllt werden sollen.
    invoice_data = {
        'B2': '2025-001',        # Rechnungsnummer (Beispiel)
        'B3': '28. Juli 2025',   # Datum (Beispiel)
        'A6': 'Mustermann GmbH', # Kundenname (Beispiel)
        'A7': 'Musterstraße 1',  # Kundenadresse Teil 1
        'A8': '12345 Musterstadt',# Kundenadresse Teil 2
        'C4': 'Dies ist ein sehr langer Text, der hoffentlich einen automatischen Zeilenumbruch in Zelle C4 auslösen wird, damit der gesamte Inhalt sichtbar ist und die Zeile sich automatisch anpasst.', # Neue Zelle mit langem Text
        'E4': 'Kurzer Text hier', # Neue Zelle
        'B12': 'Dies ist ein weiterer sehr langer beschreibender Text für ein Produkt oder eine Dienstleistung in Zelle B12, der definitiv umgebrochen werden sollte, um die Lesbarkeit zu gewährleisten.', # Neue Zelle
        'A12': 'Produkt X',      # Artikelbeschreibung 1
        'B12': 2,                # Menge 1
        'C12': 50.00,            # Einzelpreis 1
        'D12': 100.00,           # Gesamtpreis 1 (könnte auch eine Formel sein, s. unten)
        'A13': 'Dienstleistung Y',# Artikelbeschreibung 2
        'B13': 1,
        'C13': 75.00,
        'D13': 75.00,
        'D15': 175.00            # Gesamtbetrag (könnte auch eine Formel sein)
    }

    fill_excel_template(template_excel_file, output_dir, invoice_data)

    # Beispiel für eine zweite Rechnung
    invoice_data_2 = {
        'B2': '2025-002',
        'B3': '29. Juli 2025',
        'A6': 'Beispiel AG',
        'A7': 'Beispielweg 10',
        'A8': '67890 Beispielhausen',
        'C4': 'Ein anderer Text, der auch umgebrochen werden sollte.',
        'E4': 'Noch ein kurzer Text.',
        'B12': 'Dies ist die Beschreibung für die zweite Rechnung. Auch hier ist der Text absichtlich sehr lang, um den Zeilenumbruch zu testen.',
        'A12': 'Consulting',
        'B12': 5,
        'C12': 100.00,
        'D12': 500.00,
        'D15': 500.00
    }
    # fill_excel_template(template_excel_file, output_dir, invoice_data_2)