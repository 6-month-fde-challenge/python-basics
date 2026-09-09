# Exercise 25 - File Organizer Using Packages and Modules

Eighteen files go into one folder. Fifteen come out sorted into seven category folders,
three are left alone because nothing knows what they are, and one fails — loudly, and
without leaving a mess behind.

```
photo.jpg   ->  Images/          notes.txt   ->  Text/
report.pdf  ->  Documents/       data.csv    ->  Data/
```

Every demo file is a **real file of its type**: `photo.jpg` is JPEG data, `report.pdf`
opens in a PDF viewer, `beep.wav` plays, `backup.zip` unzips. Sorting a file correctly
and producing a file that works are two different things, and it is easy to build a
demo that only tests the first.

---

## Project objective

Exercises 22 and 23 were built from loose **modules**. This one is built from a
**package** — a folder with an `__init__.py` that turns four files into one importable
thing:

```python
from organizer import detect, move, setup_logging
```

`main.py` is deliberately *outside* the package. `organizer/` could be copied into a
completely different project and would still work; `main.py` is the part that knows
about `sys.argv`, printing and exit codes. Getting that line in the right place is the
whole exercise.

The second half is that this program **destroys things**. Reading a file wrong wastes a
second; moving a file wrong loses it. Every guard in `mover.py` exists because of that.

---

## Project structure

```
25_file_organizer/
├── README.md
├── main.py                 the CLI - imports the package, owns argv and printing
├── make_demo.py            rebuilds demo_files/ so the demo is repeatable
├── demo_assets.py          real JPEG/PNG/GIF/PDF/WAV/ZIP bytes for the demo files
├── sample_output.txt       four runs, captured start to finish
├── organizer/              <- THE PACKAGE
│   ├── __init__.py             the front door: what the package offers
│   ├── errors.py               the exception vocabulary
│   ├── logger_config.py        where log records go
│   ├── detector.py             file detection - which folder does this belong in?
│   └── mover.py                file movement - put it there, safely
├── demo_files/             the folder being organized
├── organized/              where things end up
└── logs/
    ├── organizer.log       DEBUG and above - every operation, good and bad
    └── errors.log          ERROR and above - only what failed
```

Four modules for the four jobs the assignment names — **file detection, file movement,
logging, exception handling** — plus the `__init__.py` that makes them a package.

---

## How to execute the program

No installation is required — `os`, `shutil` and `logging` are all standard library.

```bash
python make_demo.py               # (re)build demo_files/ and organized/
python main.py                    # organize demo_files/ -> organized/
python main.py <folder>           # organize a different folder
python main.py --lock notes.txt   # hold a file open, to demo the permission error
python demo_assets.py             # check that every asset really decodes
```

or from the repo root:

```bash
python .\01_python_basics\25_file_organizer\main.py
```

Organizing is destructive, so run `make_demo.py` first — it deletes and recreates both
folders, which is what makes the demonstration repeatable. It finishes by checking each
binary file against its format's magic number, so a broken demo file is caught before
the demo rather than during it.
**Requires Python 3.6+.** Verified on Python 3.12.10.

### The options

There is nothing interactive here - no prompt to answer, so every choice is an argument.

| Argument | Accepts | Default |
|---|---|---|
| *(first bare word)* | the folder to organize | `demo_files/` |
| `--lock NAME` | a **filename inside the source folder** | none |

**`--lock` exists for one reason:** the assignment asks for permission errors to be
handled, and holding a file open is the only reliable way to produce one on Windows
without editing a single ACL.

```bash
python main.py --lock notes.txt     # -> ERROR, 14 of 18 moved, exit code 1
```

Any filename in the source folder works, binary included — `open(path, "r+")` only needs
the handle, it does not decode anything. A name that does not exist is logged and the
run continues normally. The handle is released in a `finally`, so running
`python main.py` again straight afterwards moves the file that failed.

---

## What makes it a package, not four files

| | Four loose modules | A package |
|---|---|---|
| import | `import detector` | `from organizer import detect` |
| internal imports | `from errors import ...` | `from .errors import ...` — relative |
| public surface | whatever happens to be defined | `__all__` in `__init__.py` |
| name collisions | your `errors.py` vs. everyone's | `organizer.errors` |
| moving it | copy four files and hope | copy one folder |

`__init__.py` is the front door. It re-exports the names a caller actually needs, so
`main.py` never has to know that `move` lives in `mover.py`:

```python
from .detector import CATEGORIES, EXTENSION_MAP, detect, scan
from .errors import FileOrganizerError, UnsupportedFileError, ...
from .logger_config import get_logger, setup_logging, start_run
from .mover import ensure_folder, move, unique_destination

__all__ = ["detect", "scan", "move", "setup_logging", ...]
```

The **dot** in `from .errors import ...` is a relative import: "the `errors` module next
to me in this package", rather than "some module called `errors` somewhere on the
path". That is what lets the package be renamed or relocated without editing every file
inside it.

**Import order is dependency order.** `errors.py` and `logger_config.py` import nothing
of ours; `detector.py` and `mover.py` import those two; `main.py` imports the package.
Nothing imports upwards, so there are no circular imports.

---

## The category map, written once and inverted

```python
CATEGORIES = {
    "Images":    [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".ico"],
    "Text":      [".txt", ".md", ".rtf", ".log"],
    "Documents": [".pdf", ".doc", ".docx", ".odt", ".ppt", ".pptx"],
    "Data":      [".csv", ".xlsx", ".xls", ".json", ".xml", ".yaml", ".yml", ".db"],
    "Audio":     [".mp3", ".wav", ".flac", ".m4a", ".ogg"],
    "Video":     [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "Archives":  [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code":      [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".sh"],
}

EXTENSION_MAP = {}                          # ".jpg" -> "Images"
for category, extensions in CATEGORIES.items():
    for extension in extensions:
        EXTENSION_MAP[extension] = category
```

`CATEGORIES` is the version a human edits — one line per destination folder.
`EXTENSION_MAP` is the version the lookup needs — one entry per extension, so finding a
category is a single dictionary step instead of scanning eight lists. Building the
second from the first means they can never disagree, and adding `.webp` to Images is a
one-word change.

Two edge cases the lookup handles:

- `screenshot.PNG` — `os.path.splitext` preserves case, so the extension is lower-cased
  before the lookup.
- `.editorconfig` — a dotfile. The tempting assumption is that it splits into
  `("", ".editorconfig")` and so needs special handling. It does not:

```python
splitext("photo.jpg")      -> ("photo", ".jpg")
splitext("README")         -> ("README", "")
splitext(".editorconfig")  -> (".editorconfig", "")   # a leading dot is ignored
splitext("archive.tar.gz") -> ("archive.tar", ".gz")  # only the LAST extension
```

A dotfile already comes back with an **empty extension** — the same answer as a file
with no extension at all — so a single `if not extension` covers both, and the special
case written for it turned out to be dead code. Checking beats assuming.

---

## Every situation the assignment asks about

| Situation | Handled by | Result |
|---|---|---|
| file does not exist | `detector.detect` / `mover.move` | `SourceNotFoundError`, logged, next file |
| destination folder missing | `mover.ensure_folder` | created, logged `WARNING` |
| destination name taken by a *file* | `mover.ensure_folder` | `DestinationError` |
| duplicate filename | `mover.unique_destination` | renamed `photo (1).jpg`, logged `WARNING` |
| permission error | `mover.move` | `FileAccessError`, cleaned up, logged `ERROR` |
| unsupported file type | `detector.detect` | `UnsupportedFileError`, left alone, `WARNING` |
| source folder missing | `main` | `CRITICAL`, exit code 1 — the only fatal one |

### The exception hierarchy

```
Exception
 └── FileOrganizerError          base - one except clause catches every one below
      ├── UnsupportedFileError       extension has no category
      ├── SourceNotFoundError        the file or folder is not there
      ├── DestinationError           the target folder cannot be used
      ├── DuplicateFileError         no free name after 999 tries
      └── FileAccessError            the OS refused
```

`UnsupportedFileError` is the class the assignment names, and it is caught **before**
the base class, because it is not a failure:

```python
except UnsupportedFileError as error:
    log.warning("SKIPPED  %s : %s", name, error.message)   # left where it is
    unsupported.append(...)

except FileOrganizerError as error:
    log.error("FAILED   %s : %s", name, error.message)     # could not be moved
    failed.append(...)

except Exception as error:
    log.critical("FAILED   %s : unexpected %s", name, ..., exc_info=True)
```

An unknown extension is a gap in the category map, not a broken program — so it is a
`WARNING`, the file is left exactly where it was, and the exit code stays 0. That
ordering matters: `FileOrganizerError` first would have swallowed it.

---

## The two guards that protect the user's files

**1. Nothing is ever overwritten.** `shutil.move(src, dst)` silently replaces `dst`. For
a program whose entire job is relocating files, that is the one behaviour that must not
happen — the duplicate `photo.jpg` would destroy the original and the log would
cheerfully record a success. So a free name is found *first*:

```
Images/photo.jpg        already there
Images/photo (1).jpg    already there
Images/photo (2).jpg    free -> use this
```

**2. A failed move leaves nothing behind.** This one was a real bug, found by running
the demo twice.

`shutil.move` is not one operation. Same drive, it renames — which either happens or
does not. When the rename is refused it falls back to **copy, then delete**. If the
*delete* is the part that fails, the copy has already succeeded: the move reports
`PermissionError` while the destination file now exists and the source is still there.

The first version therefore reported `FAILED notes.txt` while quietly leaving a copy in
`Text/`. The next run then found a duplicate it had created itself and produced
`notes (1).txt` — two copies of a file the program had said it failed to move.

```python
def undo_partial(source, target):
    if not os.path.exists(target):  return False
    if not os.path.exists(source):  return False   # move DID complete - do not delete
    os.remove(target)
    log.warning("Removed the half-finished copy left at %s by a failed move", ...)
```

The second guard is the important one: if the source is gone, the move actually
completed, and deleting the target would destroy the only remaining copy.

---

## Verified run

`sample_output.txt` captures four runs back to back.

**With `notes.txt` held open** (`--lock notes.txt`). On Windows an open handle makes the
move fail with `WinError 32` — the permission branch, demonstrated without touching an
ACL:

```
[WARNING] Created destination folder: Archives
[WARNING] Duplicate name in Images: photo.jpg -> photo (2).jpg
[WARNING] Removed the half-finished copy left at Text/notes.txt by a failed move
[ERROR]   FAILED  notes.txt : Access denied by the operating system:
                  The process cannot access the file because it is being used by another process

Files examined      : 18
Moved               : 14
Unsupported         : 3
Failed              : 1
exit code: 1
```

**Run it again**, with nothing holding the file. `notes.txt` lands as `notes.txt` — not
`notes (1).txt` — which is the proof that the cleanup worked:

```
Files examined      : 4      (.editorconfig, README, mystery.xyz, notes.txt)
Moved               : 1
Unsupported         : 3      left alone a second time, not moved by accident
```

**A source folder that does not exist** — the only failure that ends the run:

```
[CRITICAL] Cannot start: Source does not exist [no_such_folder]
exit code: 1
```

`logs/organizer.log` after all four: 1 `CRITICAL`, 1 `ERROR`, 15 `WARNING`, 27 `INFO`,
62 `DEBUG`. `logs/errors.log` is two lines long.

Final layout:

```
organized/Archives/backup.zip       organized/Images/logo.gif
organized/Audio/beep.wav            organized/Images/photo.jpg
organized/Code/index.html           organized/Images/photo (1).jpg
organized/Code/script.py            organized/Images/photo (2).jpg   <- renamed
organized/Data/config.json          organized/Images/screenshot.PNG
organized/Data/data.csv             organized/Text/debug.log
organized/Data/sales.xml            organized/Text/notes.txt
organized/Documents/invoice.pdf     organized/Text/todo.md
organized/Documents/report.pdf

demo_files/.editorconfig  demo_files/README  demo_files/mystery.xyz   <- untouched
demo_files/subfolder/                                                <- never entered
```

All 17 are checked by opening them, not by trusting the extension: the images decode,
both PDFs report one page and the right title, the WAV reports 0.35s at 8000Hz, and the
ZIP lists its two members and passes `testzip()`.

The three `photo*.jpg` files are three genuinely **different** pictures - a sunset and a
dusk scene that were already filed, plus the hills-and-sun photo that arrived during the
run and became `photo (2).jpg`. Open all three side by side and the no-overwrite
guarantee is visible rather than asserted.

---

## Concepts used

**Packages**
- `__init__.py`, and what it adds over a plain folder of modules
- Relative imports — `from .errors import ...` — inside the package
- `__all__` as an explicit public surface
- `__version__`
- Dependency order as import order, so there are no circular imports
- The application (`main.py`) living outside the package it uses

**Custom exceptions**
- A base class plus five subclasses, so one `except` can be broad or narrow
- `UnsupportedFileError`, as the assignment requires
- Catching the specific case *before* the base class, because the two mean different
  things
- Wrapping `PermissionError` in `FileAccessError` while keeping the original on
  `.cause` — the new type is clearer, and losing the OS reason would be the usual
  mistake
- `raise ... from error` to keep the chain

**The standard library**
- `os.path.splitext`, `basename`, `dirname`, `isdir`, `isfile`, `exists`, `relpath`
- `os.listdir` and `os.makedirs(..., exist_ok=True)`
- `shutil.move`, and what it actually does when the rename fails
- `logging` with two file handlers at two thresholds
- In `demo_assets.py`, for building files that are genuinely valid: `base64` for the
  image bytes, `wave` and `struct` for a playable WAV, `zipfile` for a real archive,
  `io.BytesIO` so every builder returns bytes rather than writing a path, and magic
  numbers (`ÿØÿ`, `PNG`, `%PDF`, `RIFF`, `PK`) to verify the
  result

**Design**
- Category map written one way, inverted for lookup
- One log line per file, written in one place — logging inside both the package and the
  caller is how a log ends up with two lines for one failure and counts that disagree
  with the report
- An exit code that is non-zero on failure but zero for unsupported files

---

## Learning / outcomes

1. **A package is a boundary, not a folder.** The useful question is not "how do I make
   `__init__.py`" but "what is inside the boundary and what is outside". `argv` and
   `print()` are outside; detecting and moving are inside. That single decision is what
   makes `organizer/` reusable and `main.py` disposable.

2. **`shutil.move` is two operations wearing one name.** It renames when it can and
   copies-then-deletes when it cannot, and only the second one can fail halfway. Every
   destructive operation deserves the question "what if this fails in the middle?" —
   and the answer is rarely "it cannot".

3. **Not every problem is an error.** An unsupported file is a `WARNING`, exit code 0,
   file untouched. A locked file is an `ERROR`, exit code 1. A missing source folder is
   `CRITICAL` and stops everything. Three severities, three completely different
   responses, and choosing between them is the actual design work.

4. **Log the operation once, in one place.** The first version logged failures in both
   `mover.py` and `main.py`, so `errors.log` had two lines per failure and the counts in
   the summary no longer matched the log. The package describes what happened; the
   application decides what it means and records it.

5. **Write the map the way a human reads it, then transform it.** Eight readable lines
   in `CATEGORIES` become forty-eight lookup entries in `EXTENSION_MAP` at import time.
   Maintaining the readable one and generating the fast one beats maintaining either
   alone.

### Challenges faced

- **The demo files were not real files.** The first `make_demo.py` created `photo.jpg`
  by writing the words *"a photograph"* into a text file. The organizer filed it into
  `Images/` perfectly, every test passed, the log said `MOVED photo.jpg -> Images/` —
  and then double-clicking the result did nothing, because a `.jpg` holding text is not
  a picture. **Sorting a file correctly and producing a file that works are two
  different things, and only one of them was being tested.** `demo_assets.py` now holds
  real JPEG/PNG/GIF bytes as base64, builds a real PDF with a correct `xref` table,
  writes a real WAV with the `wave` module and a real ZIP with `zipfile`, and
  `make_demo.py` verifies each one against its format's magic number before the demo
  starts. `.docx`, `.xlsx`, `.mp3` and `.mp4` were dropped from the demo entirely,
  because a valid file of those types cannot be produced from the standard library —
  better an honest demo of seven categories than a broken demo of nine.
- **The failed move that succeeded anyway.** Described above — found only because the
  demo was run twice and produced a `notes (1).txt` nobody asked for. It is the best
  argument in this exercise for running your own program more than once.
- **`str(PermissionError)` prints the whole absolute path**, so every error line
  contained the same 80-character path twice. `error.strerror` is the OS explanation on
  its own, which is the only part the reader did not already have.
- **A dotfile edge case that did not exist.** `get_extension()` carried a special
  branch for dotfiles, written on the assumption that
  `os.path.splitext(".editorconfig")` returns `("", ".editorconfig")`. It returns
  `(".editorconfig", "")` — splitext ignores a leading period — so the branch never
  once executed. Two lines of dead code defending against nothing, removed only after
  the assumption was actually run in the interpreter.
- **Recursion was tempting and wrong.** An early `scan()` walked sub-folders, which
  meant the second run happily descended into `organized/Images/` and organized it
  again. `scan()` now lists files only and logs the folders it skipped.
- **Demonstrating a permission error on Windows** without changing ACLs. Holding the
  file open in the same process turned out to be enough — `--lock` exists purely to make
  that branch reproducible on camera.

---

## YouTube demonstration link

<your-youtube-video-link>

---

## Submission links

- **GitHub Repository:** `<your-public-github-repository-link>`
- **YouTube Explanation:** `<your-youtube-video-link>`
