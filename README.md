# Simple Note Organizer

A basic Python note-taking app I built. Runs in the terminal and lets you save notes with images.

## What it does

- Create and save notes
- Attach image files to notes
- Search through your notes
- View attached images
- Delete notes when you don't need them

Everything saves automatically to a text file so your notes stick around.

## Setup

You just need Python installed. No other libraries or anything.

```bash
git clone https://github.com/yourusername/note-organizer.git
cd note-organizer
python note_organizer.py
```

That's all.

## Usage

Run it and you'll get a menu. Pick what you want to do:

1. Make a new note
2. See all your notes
3. Search for something
4. Open an image you attached
5. Delete a note
6. Quit

When you add an image, just paste the full file path. The app saves the path and can open it later.

## Storage

Notes get saved in `notes_data.txt` in the same folder. It's just plain text - you can open it yourself if you want to see how it works.

Images don't get copied anywhere, just their paths are saved. So don't move your images around after attaching them or the app won't be able to find them.

## Platforms

Should work fine on Windows, Mac, and Linux. I've tested it on Windows mostly but the image opening stuff should work cross-platform.

## TODO

Some things I might add later if I get around to it:
- Edit existing notes instead of having to delete and recreate
- Maybe add tags or categories?
- Export to markdown or something
- Better handling if image files get moved

Feel free to fork it and add whatever features you want!

## License

MIT - do whatever you want with it

---
