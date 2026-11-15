import os
import re

DIARY_FILE = "diary.txt"

def load_notes():
    notes = []
    if os.path.exists(DIARY_FILE):
        with open(DIARY_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(" | ", 1)
                if len(parts) == 2:
                    notes.append({"date": parts[0], "text": parts[1]})
    return notes

def save_notes(notes):
    with open(DIARY_FILE, "w") as f:
        for note in notes:
            f.write(f"{note['date']} | {note['text']}\n")

def add_note():
    date = input("Date: ").strip()
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
        print("Invalid date. Use YYYY-MM-DD.")
        return
    
    text = input("Text: ").strip()
    if not text:
        print("Note text cannot be empty.")
        return
        
    notes = load_notes()
    notes.append({"date": date, "text": text})
    save_notes(notes)
    print("Note saved.")
    print(f"{len(notes)} | {date} | {text}")

def view_all_notes():
    notes = load_notes()
    if not notes:
        print("No notes found. Your diary is empty.")
        return
    
    for i, note in enumerate(notes, 1):
        print(f"{i} | {note['date']} | {note['text']}")

def search_notes():
    keyword = input("Search: ").strip().lower()
    notes = load_notes()
    found = []
    
    for i, note in enumerate(notes, 1):
        if keyword in note['text'].lower() or keyword in note['date']:
            found.append((i, note))
            
    if found:
        print(f"Found {len(found)} notes:")
        for i, note in found:
            print(f"{i} | {note['date']} | {note['text']}")
    else:
        print("No matching notes found.")

def delete_note():
    try:
        note_num = int(input("Delete note number: ").strip())
    except ValueError:
        print("Note number not found.")
        return
        
    notes = load_notes()
    if 1 <= note_num <= len(notes):
        deleted = notes.pop(note_num - 1)
        save_notes(notes)
        print(f"Note {note_num} deleted. Notes left: {len(notes)}")
    else:
        print(f"Note number {note_num} not found.")

def main():
    while True:
        print("\nMenu: 1 Add, 2 View all, 3 Search, 4 Delete, 5 Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            add_note()
        elif choice == "2":
            view_all_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
