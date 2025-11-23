import os


DATA_FILE = "notes_data.txt"
my_notes = []

def load_stuff():
    global my_notes
    if not os.path.exists(DATA_FILE):
        return
    
    try:
        file = open(DATA_FILE, 'r')
        lines = file.readlines()
        file.close()
        
        i = 0
        while i < len(lines):
            if lines[i].startswith("ID:"):
                note_id = int(lines[i].split(":")[1].strip())
                title = lines[i + 1].split(":", 1)[1].strip()
                cont = lines[i + 2].split(":", 1)[1].strip()
                img_path = lines[i + 3].split(":", 1)[1].strip()
                
                if img_path == "None":
                    img_path = None
                
                temp_note = {
                    'id': note_id,
                    'title': title,
                    'content': cont,
                    'image': img_path
                }
                my_notes.append(temp_note)
                i += 5
            else:
                i += 1
        print(f"Hey! I found {len(my_notes)} of your old notes and loaded them up.\n")
    except Exception as e:
        print("Hmm, had a little trouble reading your notes. No worries, we'll start fresh!\n")

# saving in file
def save_stuff():
    try:
        f = open(DATA_FILE, 'w')
        for note in my_notes:
            f.write(f"ID:{note['id']}\n")
            f.write(f"Title:{note['title']}\n")
            f.write(f"Content:{note['content']}\n")
            f.write(f"Image:{note['image']}\n")
            f.write("---\n")
        f.close()
        print("Great! Your notes are safely saved.")
    except:
        print("Oops! Something went wrong while saving. Try again?")

def create_new_note():
    print("\nAlright, let's create a new note!")
    note_title = input("What should we call this note? ")
    note_content = input("What do you want to write? ")
    img = input("Got a picture to attach? (Just hit Enter if not): ").strip()
    
    if img == "":
        img = None
    elif not os.path.exists(img):
        print(f"Hmm, I can't find that image at '{img}', but I'll save the path anyway in case you move it there later.")
    
    # get the next available ID - kinda hacky but works
    if len(my_notes) == 0:
        next_id = 1
    else:
        next_id = max([note['id'] for note in my_notes]) + 1
    
    new_note = {
        'id': next_id,
        'title': note_title,
        'content': note_content,
        'image': img
    }
    my_notes.append(new_note)
    save_stuff()
    print(f"\nAwesome! Your note '{note_title}' has been saved!\n")

def show_all():
    if len(my_notes) == 0:
        print("\nYou don't have any notes yet. Want to create one?\n")
        return
    
    print("\n--- Here are all your notes ---")
    for note in my_notes:
        print(f"\n#{note['id']} - {note['title']}")
        print(f"{note['content']}")
        if note['image']:
            print(f"📷 {note['image']}")
        print("-" * 40)
    print()

def search_notes():
    search_term = input("\nWhat are you looking for? ").lower()
    results = []
    
    # Search function
    for note in my_notes:
        title_lower = note['title'].lower()
        content_lower = note['content'].lower()
        
        if search_term in title_lower or search_term in content_lower:
            results.append(note)
    
    if len(results) == 0:
        print(f"\nSorry, couldn't find anything with '{search_term}'. Maybe try different words?\n")
        return
    
    print(f"\n--- Found {len(results)} note(s) matching '{search_term}' ---")
    for note in results:
        print(f"\n#{note['id']} - {note['title']}")
        print(f"{note['content']}")
        if note['image']:
            print(f"📷 {note['image']}")
        print("-" * 40)
    print()

def open_image():
    if len(my_notes) == 0:
        print("\nNo notes available yet!\n")
        return
    
    try:
        note_num = int(input("\nWhich note's picture do you want to see? (Enter note #): "))
        found_it = False
        
        for note in my_notes:
            if note['id'] == note_num:
                found_it = True
                if note['image'] and os.path.exists(note['image']):
                    print(f"Opening up {note['image']} for you...")
                    # different OS need different commands
                    if os.name == 'nt':  # windows
                        os.system(f'start "" "{note["image"]}"')
                    elif os.name == 'posix':  # mac/linux
                        if os.uname().sysname == 'Darwin':
                            os.system(f'open "{note["image"]}"')
                        else:
                            os.system(f'xdg-open "{note["image"]}"')
                elif note['image']:
                    print(f"I've got the path ({note['image']}) but can't find the actual image file. Did you move it?")
                else:
                    print("This note doesn't have a picture attached.")
                break
        
        if not found_it:
            print(f"\nHmm, I don't see a note with that number. Try again?\n")
    except ValueError:
        print("\nThat doesn't look like a valid number. Let's try again!\n")


def delete_note():
    if len(my_notes) == 0:
        print("\nYou don't have any notes to delete yet.\n")
        return
    
    try:
        note_id = int(input("\nWhich note do you want to delete? (Enter note #): "))
        deleted = False
        
        # deletion or finding
        for idx in range(len(my_notes)):
            if my_notes[idx]['id'] == note_id:
                deleted_note = my_notes[idx]
                my_notes.pop(idx)
                save_stuff()
                print(f"\nAlright, I've deleted '{deleted_note['title']}' for you.\n")

                deleted = True
                break
        
        if not deleted:
            print(f"\nCouldn't find a note with that number. Double-check and try again?\n")
    except ValueError:

        print("\nOops! That doesn't look like a valid number.\n")

def show_menu():
    print("\n╔════════════════════════════════╗")
    print("║     Your Note Organizer 📝     ║")
    print("╠════════════════════════════════╣")
    print("║  1. Create a new note          ║")
    print("║  2. Show me all my notes       ║")
    print("║  3. Search for something       ║")
    print("║  4. Open a picture             ║")
    print("║  5. Delete a note              ║")
    print("║  6. I'm done for now           ║")
    print("╚════════════════════════════════╝")

def main():
    print("\n👋 Welcome back to your personal note space!")
    load_stuff()

    
    while True:
        show_menu()
        choice = input("\nWhat would you like to do? (1-6): ").strip()
        
        if choice == '1':
            create_new_note()
        elif choice == '2':
            show_all()
        elif choice == '3':
            search_notes()
        elif choice == '4':
            open_image()
        elif choice == '5':
            delete_note()
        elif choice == '6':
            print("\n✨ Thanks for using your note organizer! See you next time!\n")
            break
        else:
            print("\nHmm, that's not one of the options. Pick a number between 1 and 6!")



# completion....
if __name__ == "__main__":
    main()
