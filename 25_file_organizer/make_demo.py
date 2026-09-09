"""
make_demo.py - rebuild the demo folder so the run is repeatable
===============================================================
Organizing is destructive: run main.py once and demo_files/ is empty,
which makes the second demonstration rather short. This script deletes
demo_files/ and organized/ and recreates them from scratch.

    python make_demo.py       reset, then run `python main.py`

EVERY FILE IT WRITES IS A REAL FILE OF ITS TYPE
    photo.jpg really is JPEG data, report.pdf really opens in a PDF
    viewer, beep.wav really plays, backup.zip really unzips. The bytes
    come from demo_assets.py.

    The first version of this script wrote `photo.jpg` containing the
    words "a photograph". The organizer filed it into Images/ perfectly
    - and then nothing could open it, because a .jpg holding text is not
    a picture. Sorting a file correctly and producing a file that works
    are two different things, and only one of them was being tested.

WHAT IT CREATES, AND WHY EACH FILE IS THERE
    18 files across 7 categories                the happy path
    screenshot.PNG                              an upper-case extension
    mystery.xyz, README, .editorconfig          unsupported types
    organized/Images/photo.jpg (pre-existing)   forces a duplicate rename
    demo_files/subfolder/                       proves scan() does not
                                                descend into folders

It is deliberately NOT part of the organizer package - the package
organizes files, it does not invent them.
"""
import os
import shutil

import demo_assets

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(BASE_DIR, "demo_files")
DEST = os.path.join(BASE_DIR, "organized")


# Text formats. A text file with these extensions is genuinely a valid
# file of that type, so the content can just be written as-is.
TEXT_FILES = {
    # -> Text
    "notes.txt": "The quick brown fox jumps over the lazy dog.\n"
                 "Exercise 25 - organizing files by extension.\n",
    "todo.md": "# To do\n\n- [x] detect the category\n- [x] move the file\n"
               "- [ ] record every operation in the log\n",
    "debug.log": "2026-09-09 08:00:01 INFO  started\n"
                 "2026-09-09 08:00:02 INFO  finished\n",
    # -> Data
    "data.csv": "id,name,city\n1,Rahul,Pune\n2,Priya,Kochi\n3,Aman,Indore\n",
    "config.json": '{\n  "debug": false,\n  "retries": 3,\n'
                   '  "categories": ["Images", "Text", "Documents", "Data"]\n}\n',
    "sales.xml": '<?xml version="1.0" encoding="UTF-8"?>\n<sales>\n'
                 '  <item name="Laptop" units="3" />\n'
                 '  <item name="Mouse" units="11" />\n</sales>\n',
    # -> Code
    "script.py": '"""A file for the organizer to move."""\n\n\n'
                 'def main():\n    print("hello from script.py")\n\n\n'
                 'if __name__ == "__main__":\n    main()\n',
    "index.html": "<!doctype html>\n<html>\n  <head><title>Demo</title></head>\n"
                  "  <body><h1>File organizer demo</h1></body>\n</html>\n",
    # -> nowhere: no category for these
    "mystery.xyz": "There is no category for a .xyz file.\n",
    "README": "A file with no extension at all.\n",
    ".editorconfig": "# A dotfile. splitext() gives it an EMPTY extension,\n"
                     "# not an extension of '.editorconfig'.\nroot = true\n",
}


def binary_files():
    """
    Return {filename: bytes} for the formats that are not text.

    Built by a function rather than a module-level dict so the WAV
    samples and the PDF are only generated when the demo is actually
    being rebuilt.
    """
    return {
        # -> Images
        "photo.jpg": demo_assets.image_bytes(demo_assets.PHOTO_JPEG),
        "screenshot.PNG": demo_assets.image_bytes(demo_assets.SCREENSHOT_PNG),
        "logo.gif": demo_assets.image_bytes(demo_assets.LOGO_GIF),
        # -> Documents
        "report.pdf": demo_assets.pdf_bytes(
            "Quarterly Report",
            ["Prepared for the file organizer demo.",
             "Exercise 25 - packages and modules.",
             "This is a real PDF, so it really opens."]),
        "invoice.pdf": demo_assets.pdf_bytes(
            "Invoice 2026-114",
            ["Laptop      x1     70,000",
             "Mouse       x2        900",
             "Total              70,900"]),
        # -> Audio
        "beep.wav": demo_assets.wav_bytes(frequency=523, milliseconds=350),
        # -> Archives
        "backup.zip": demo_assets.zip_bytes({
            "backup/readme.txt": "A real ZIP archive, with two members.\n",
            "backup/rows.csv": "id,value\n1,10\n2,20\n",
        }),
    }


# Files placed in the destination BEFORE the run, so the duplicate-name
# branch is exercised rather than merely described. Both are real JPEGs
# of different scenes, so the rename can be seen to have preserved two
# genuinely different pictures.
def pre_existing():
    """Return {relative path inside organized/: bytes}."""
    return {
        os.path.join("Images", "photo.jpg"):
            demo_assets.image_bytes(demo_assets.PHOTO_ALT1_JPEG),
        os.path.join("Images", "photo (1).jpg"):
            demo_assets.image_bytes(demo_assets.PHOTO_ALT2_JPEG),
    }


def reset():
    """Delete and rebuild both folders. Returns the counts written."""
    for folder in (SOURCE, DEST):
        if os.path.isdir(folder):
            shutil.rmtree(folder)

    os.makedirs(SOURCE, exist_ok=True)

    for name, text in TEXT_FILES.items():
        with open(os.path.join(SOURCE, name), "w", encoding="utf-8") as handle:
            handle.write(text)

    for name, data in binary_files().items():
        # "wb" - these are bytes, and opening in text mode would mangle
        # every 0x0A in the image into a CRLF on Windows.
        with open(os.path.join(SOURCE, name), "wb") as handle:
            handle.write(data)

    # A sub-folder, to show that scan() lists files only.
    os.makedirs(os.path.join(SOURCE, "subfolder"), exist_ok=True)
    with open(os.path.join(SOURCE, "subfolder", "ignored.txt"), "w",
              encoding="utf-8") as handle:
        handle.write("scan() does not descend into folders\n")

    already = pre_existing()
    for relative, data in already.items():
        full = os.path.join(DEST, relative)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "wb") as handle:
            handle.write(data)

    return len(TEXT_FILES) + len(binary_files()), len(already)


def verify():
    """
    Check that each file really begins with its format's magic number.

    The first bytes of a file are the only honest evidence that it is
    what its extension claims. This is the check the first version of
    the demo would have failed.
    """
    MAGIC = {
        ".jpg": b"\xff\xd8\xff", ".png": b"\x89PNG", ".gif": b"GIF8",
        ".pdf": b"%PDF", ".wav": b"RIFF", ".zip": b"PK\x03\x04",
    }
    checked = 0
    for name in sorted(os.listdir(SOURCE)):
        extension = os.path.splitext(name)[1].lower()
        if extension not in MAGIC:
            continue
        with open(os.path.join(SOURCE, name), "rb") as handle:
            head = handle.read(8)
        ok = head.startswith(MAGIC[extension])
        print(f"      {name:<18} {'OK' if ok else 'WRONG MAGIC NUMBER'}")
        checked += 1
    return checked


if __name__ == "__main__":
    created, already = reset()
    print(f"   demo_files/  {created} files + 1 sub-folder")
    print(f"   organized/   {already} pre-existing file(s), to force a rename")
    print()
    print("   Verifying that the binary files are what their names claim:")
    print(f"   {verify()} checked")
    print()
    print("   Now run:  python main.py --dry-run")
    print("        and: python main.py")
