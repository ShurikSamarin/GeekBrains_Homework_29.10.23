import json
from datetime import datetime

def load_notes():
    try:
        with open('note.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

def save_notes(notes):
    with open('note.json', 'w') as file:
        json.dump(notes, file)

def add_note():
    title = input("Input note title: ")
    body = input("Input note text: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        'id': len(notes) + 1,
        'title': title,
        'body': body,
        'timestamp': timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Note added successfully")

def print_notes(notes):
    if not notes:
        print("Notes list is empty")
    else:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Title: {note['title']}")
            print(f"Text: {note['body']}")
            print(f"Date/time: {note['timestamp']}")
            print()

def edit_note():
    note_id = int(input("Input ID for editing: "))
    for note in notes:
        if note['id'] == note_id:
            new_title = input("Input new note title: ")
            new_body = input("Input new note text: ")
            note['title'] = new_title
            note['body'] = new_body
            note['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Note edited successfully")
            return
    print("ID not found")

def delete_note():
    note_id = int(input("Input ID for deleting: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Note deleted successfully")
            return
    print("ID not found")

def filter_notes_by_date():
    date_str = input("Input date for filtering (YYYY-MM-DD): ")
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        filtered_notes = [note for note in notes if datetime.strptime(note['timestamp'], "%Y-%m-%d %H:%M:%S").date() == date]
        print_notes(filtered_notes)
    except ValueError:
        print("Date format is incorrect")

notes = load_notes()

while True:
    print("=== MENU ===")
    print("1. Print notes")
    print("2. Add new note")
    print("3. Edit note")
    print("4. Delete note")
    print("5. Note filter by date")
    print("6. Quit")

    choice = input("Select your choice: ")

    if choice == '1':
        print_notes(notes)
    elif choice == '2':
        add_note()
    elif choice == '3':
        edit_note()
    elif choice == '4':
        delete_note()
    elif choice == '5':
        filter_notes_by_date()
    elif choice == '6':
        break
    else:
        print("Choice is incorrect, try again")