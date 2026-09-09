# Exercise 22 - Application Activity Logger

A menu-driven application whose real subject is not the menu. Every activity a user
performs is recorded to disk at the right severity, and no single failure is allowed
to end the session.

---

## Project objective

Exercise 21 ended with menu-driven applications that used `print()` to say what was
happening. `print()` has no severity, no timestamp, no origin, and vanishes when the
window closes. This exercise replaces it with the `logging` module.

Five activities — **Login, Calculate, Read a File, Write a File, Logout** — each
produce log records at levels chosen to match what actually happened, written to two
files with two different thresholds.

The second requirement is that **an error in one operation must not terminate the
application**. That is why every activity returns rather than raises, and why the
dispatcher sits underneath them all with a net.

---

## Project structure

```
22_application_activity_logger/
├── README.md
├── 00_concepts.py          READ FIRST - logging and file handling, demonstrated
├── main.py                 entry point - configure logging, run the loop, stop
├── menu.py                 the screen and the dispatcher
├── auth.py                 Login / Logout, and the session state
├── calculator.py           Calculate
├── file_handler.py         Read a File / Write a File
├── logger_config.py        the one place that decides where log records go
├── demo_input.txt          26 answers, so a full demo run is reproducible
├── sample_output.txt       captured from a real run
├── data/
│   ├── notes.txt           a file with content   -> INFO
│   ├── empty.txt           a file with none      -> WARNING
│   └── output.txt          written by activity 4
└── logs/
    ├── application.log     DEBUG and above - the full story
    └── error.log           ERROR and above  - only what went wrong
```

`main.py` is 80 lines and contains no application logic at all. That is the point of
the assignment's "instead of writing everything in main.py".

---

## How to execute the program

No installation is required — `logging` is in the standard library.

**Start with the concepts file.** It is a plain top-to-bottom script with no functions
in it, and it deletes the two files it creates on the way out:

```bash
python 00_concepts.py
```

Then the application itself:

```bash
python main.py
```

or from the repo root:

```bash
python .\01_python_basics\22_application_activity_logger\main.py
```

To replay the exact run in `sample_output.txt`:

```bash
python main.py < demo_input.txt
```

**Requires Python 3.6+.** Verified on Python 3.12.10.

---

## Login credentials

Menu option **1. Login** asks for a username and password. Two accounts exist:

| Username | Password |
|---|---|
| `admin` | `python123` |
| `rahul` | `learner2026` |

```
   Choose an activity : 1
   Username : admin
   Password : python123
   Welcome, admin.
```

Options **2, 3 and 4** (Calculate, Read a File, Write a File) are **gated** — reaching
them without logging in first is refused and logged as a `WARNING`:

```
[WARNING] Activity 'Calculate' blocked: no user is logged in
```

That refusal is deliberate demo material, not an obstacle: an unauthenticated user
reaching for a protected activity is exactly the kind of thing an activity log exists to
record. `demo_input.txt` opens by pressing `2` before logging in for that reason, then
logs in with the wrong password (another `WARNING`), then succeeds.

The accounts live in one dictionary at the top of [auth.py](auth.py):

```python
USERS = {
    "admin": "python123",
    "rahul": "learner2026",
}
```

Plain-text passwords in a source file are of course not how real authentication works —
a real one stores a salted hash and never the password itself. This exercise is marked
on **logging**, so the user store is deliberately the least interesting part of it. What
matters here is that a wrong password produces a `WARNING` and a correct one produces an
`INFO`, and that the log records *which* username was tried either way.

---

## The menu, and what to type at every prompt

```
========================================================
   APPLICATION ACTIVITY LOGGER      [ not logged in ]
========================================================
   1. Login
   2. Calculate
   3. Read a File
   4. Write a File
   5. Logout
   --------------------------------------------------
   6. Simulate an unexpected failure   (CRITICAL demo)
   0. Exit
========================================================
   Choose an activity :
```

The header shows the current session — `[ not logged in ]` or `[ admin ]`.

Options 1-5 are the five activities the assignment specifies. **6** and **0** are extra:
`6` raises a `KeyError` on purpose, because every other `CRITICAL` in this application
needs a real bug to appear and the fifth log level has to be demonstrable on demand.

| Prompt | Type | Notes |
|---|---|---|
| `Choose an activity` | `0`-`6` | anything else → `WARNING Invalid menu choice` |
| `Username` / `Password` | see the table above | blank username → `WARNING` |
| `Choose an operation` | `1`-`6` | see the operations table below |
| `First number` / `Second number` | any number | `12`, `-5`, `3.5` all fine; text is re-asked |
| `File to read` | `notes.txt` | see the files table below |
| `File to write` | any name, e.g. `output.txt` | created in `data/`, **overwrites** |
| `Text to store` | anything | blank → `WARNING Writing empty content` |

### Calculate — the six operations

```
   OPERATIONS
      1. +          4. /
      2. -          5. %
      3. *          6. **
   Choose an operation : 4
   First number       : 10
   Second number      : 0
   Cannot divide by zero.
```

Type the **number**, not the symbol. `4` then `10` then `0` is the quickest way to
produce an `ERROR` on camera; `6` with `2` and `10` gives `1024`.

### Read a File / Write a File — what to type

A bare filename is looked for in `data/` first, so you do not have to type a path. A
name containing `/` or `\` is used exactly as given.

| Type this | What happens | Level |
|---|---|---|
| `notes.txt` | 6 lines printed | `INFO` |
| `empty.txt` | opens, but has no content | `WARNING File was empty` |
| anything else | `No such file.` | `ERROR ... not found` |
| a folder — `data/` or `./data` | `Permission denied.` on Windows | `ERROR` |

So three reads — `notes.txt`, `empty.txt`, `missing.txt` — produce an `INFO`, a
`WARNING` and an `ERROR` in that order, which is exactly what `demo_input.txt` does.

Note the **`/`** in that last row. A bare name is resolved inside `data/`, so typing
`data` becomes `data/data` and reports *not found* rather than *is a folder*. Only a
name containing a separator is used as given.

And the folder case exposes a platform difference worth knowing:

```
open("data", "r")     Windows -> PermissionError   (errno 13, EACCES)
                      Linux   -> IsADirectoryError (errno 21, EISDIR)
```

`read_file()` catches both, so the behaviour is right either way — but it means the
`except IsADirectoryError` clause is **unreachable on Windows**, and the `ERROR` line
you will actually see on this machine says "permission denied". Worth saying out loud in
the video rather than being surprised by it: the same code produces a different
exception on a different operating system, which is precisely why the handler names four
of them separately instead of trusting one.

**`Write a File` uses mode `"w"`, which truncates.** Typing `notes.txt` at the write
prompt replaces the sample file. Use `output.txt`, or restore `notes.txt` from git
afterwards.

### The shortest run that produces all five levels

```
2              -> WARNING  Calculate blocked, not logged in
1 admin nope   -> WARNING  wrong password
1 admin python123  -> INFO  logged in
2 1 12 abc 8   -> WARNING  "abc" rejected, then INFO  calculation completed
2 4 10 0       -> ERROR    division by zero
3 empty.txt    -> WARNING  file was empty
3 missing.txt  -> ERROR    could not be opened
6              -> CRITICAL simulated failure, with traceback
5 then 0       -> INFO     logout, exit
```

That is `demo_input.txt`. Run it with `python main.py < demo_input.txt` rather than
typing it.

---

## The five levels, and what earns each one

| Level | Value | Means | Example from this application |
|---|---|---|---|
| `DEBUG` | 10 | detail only a developer wants | `Parsed '12' as 12.0` |
| `INFO` | 20 | something normal happened | `User logged in: admin` |
| `WARNING` | 30 | odd, but the app carries on | `File was empty: data\empty.txt` |
| `ERROR` | 40 | this operation failed | `Division by zero attempted: 10.0 / 0.0` |
| `CRITICAL` | 50 | the application itself is hurt | `Unexpected application failure during 'Simulate failure'` |

The distinctions that took the most thought:

- **A wrong password is `WARNING`, not `ERROR`.** Nothing broke. The application did
  exactly what it is supposed to do. `ERROR` is reserved for an operation that could
  not be completed at all.
- **"File was empty" is `WARNING`; "file could not be opened" is `ERROR`.** They look
  similar on screen and mean opposite things: one says check the data, the other says
  check the path.
- **`CRITICAL` is never raised by bad input.** It only appears when an exception
  reaches a handler that did not expect it — that is, when there is a bug.

---

## Where the records go

`logger_config.py` attaches three handlers to one logger named `app`:

| Destination | Threshold | Why |
|---|---|---|
| `logs/application.log` | `DEBUG` | the complete history, appended across runs |
| `logs/error.log` | `ERROR` | short enough to actually be read |
| the console | `WARNING` | so the menu output stays legible |

Two gates decide whether a record is written:

```
logger.setLevel(DEBUG)      <- gate 1: the logger, set to the LOWEST level
handler.setLevel(ERROR)     <- gate 2: each handler filters down from there
```

A handler never sees a record the logger already blocked. Setting the logger to `INFO`
would mean no handler ever receives a `DEBUG` record, no matter what the handler's own
level says.

Every module calls `get_logger("auth")`, which returns `logging.getLogger("app.auth")`.
The **dot** makes it a child: it inherits the parent's handlers, so the handlers are
created exactly once, and the `name` column in every line identifies the module that
produced it.

Format:

```
2026-09-09 08:11:31 | WARNING  | app.file_handler | read_file:100 | File was empty: data\empty.txt
     when            how bad      which module      where exactly    what happened
```

---

## Exception handling — three layers, deepest first

**Layer 1 — the activity modules** handle what they can predict, log it, and return a
value instead of raising:

```python
except ZeroDivisionError:
    log.error("Division by zero attempted: %s %s %s", a, symbol, b)
    return None
```

`file_handler.read_file()` handles `FileNotFoundError`, `PermissionError`,
`IsADirectoryError`, `UnicodeDecodeError` and the general `OSError` separately, because
a log that says only "could not read file" cannot tell you which of those five to fix.

**Layer 2 — `menu.dispatch()`** is the net underneath. A broad `except Exception` is
normally poor practice; at the top of a menu loop it is exactly right, because the
alternative is a traceback on screen and a dead application:

```python
except Exception:
    log.critical("Unexpected application failure during %r", name, exc_info=True)
    print("   Unexpected application failure - see logs/error.log")
finally:
    log.debug("Activity %r finished", name)
```

`exc_info=True` appends the full traceback to the log file — the difference between a
log that says something failed and a log you can debug from.

**Layer 3 — `main()`** catches anything that escapes even the dispatcher, and its
`finally` guarantees an `Application stopped` line. A log with a start line and no stop
line is itself a signal: the process was killed.

`KeyboardInterrupt` is caught separately at both layers, because Ctrl+C is a user
decision, not a fault — inside an activity it cancels the activity, at the menu prompt
it ends the application.

---

## Verified run

`python main.py < demo_input.txt` produced 55 records in `application.log` and 3 in
`error.log`:

```
CRITICAL   1        Simulate failure -> KeyError, with traceback
ERROR      2        division by zero; missing.txt not found
WARNING    5        no login; wrong password; "abc"; empty file; invalid choice
INFO       8        started, login, calculation, read, write, logout, exit, stopped
DEBUG     39        arguments, parsed values, activity start/finish
```

`error.log` in full:

```
2026-09-09 08:11:31 | ERROR    | app.calculator   | calculate:67  | Division by zero attempted: 10.0 / 0.0
2026-09-09 08:11:31 | ERROR    | app.file_handler | read_file:73  | File could not be opened - not found: data\missing.txt
2026-09-09 08:11:31 | CRITICAL | app.menu         | dispatch:145  | Unexpected application failure during 'Simulate failure'
Traceback (most recent call last):
  ...
KeyError: 'this key does not exist'
```

Three activities failed during that run. The application still reached `Exit` normally.

---

## Concepts used

**The `logging` module**
- `getLogger(name)` and the dotted parent/child hierarchy
- `FileHandler` and `StreamHandler`, each with its own `setLevel()`
- `Formatter` with `%(asctime)s`, `%(levelname)s`, `%(name)s`, `%(funcName)s`, `%(lineno)d`
- `logger.exception()` and `exc_info=True` for tracebacks
- Lazy `%s` formatting — `log.debug("x=%s", x)`, not `log.debug(f"x={x}")`, so the
  string is only built if the record is actually going to be emitted
- The re-entry guard `if logger.handlers: return`, without which a second
  `setup_logging()` call would write every line twice

**Exception handling**
- `try` / `except` / `else` / `finally`, with `else` keeping the success path visibly
  separate from the failure paths
- Specific exceptions before general ones (`ZeroDivisionError` before `Exception`,
  `FileNotFoundError` before `OSError`)
- Catching `Exception` deliberately, in the one place where it is correct

**Modules**
- Six files, one job each; `main.py` holds no logic
- `from logger_config import get_logger` at the top of every module
- Module-level state (`auth.current_user`) with `global` to reassign it
- Dictionary dispatch (`ACTIONS`, `OPERATIONS`) instead of long `if`/`elif` chains
- `os.path.dirname(os.path.abspath(__file__))` so `logs/` and `data/` resolve relative
  to the code, not to wherever the user happened to run `python` from

---

## Learning / outcomes

1. **`print()` and `log` answer different questions.** `print()` tells the person at
   the keyboard what happened now. The log tells whoever reads it tomorrow what
   happened, when, how badly, and where in the code. This application does both, and
   they say different things on purpose.

2. **Choosing the level is the actual skill.** Writing `log.info(...)` is trivial.
   Deciding that a wrong password is `WARNING` and a missing file is `ERROR` is the
   part that makes a log worth keeping. Log everything at `INFO` and you have a diary;
   log everything at `ERROR` and you have noise.

3. **Two thresholds beat one file.** `application.log` is 55 lines after one short
   session. `error.log` is 3. When something breaks, the 3-line file is the one you
   open.

4. **`finally` is where the guarantees live.** The `Activity finished` and
   `Application stopped` lines are the only records the code promises to write on
   every route out — including the routes taken by an exception on its way past.

5. **A broad `except` is a design decision, not laziness.** It is wrong in a library
   and right at the top of a menu loop. Both statements are about the same three lines
   of code; only the position changed.

### Challenges faced

- **Every message logged twice.** Running `setup_logging()` from both `main.py` and a
  module added a second copy of all three handlers. Fixed with the `if logger.handlers`
  guard — and it is worth causing once, because the duplicated log file is a very
  confusing thing to debug from cold.
- **A module named `logging.py`.** The first version called the config module
  `logging.py`, which shadowed the standard library and made `import logging` import
  itself. Renamed to `logger_config.py`.
- **`DEBUG` messages vanishing.** The handler was set to `DEBUG` but the logger was
  still at its default `WARNING`, so the records never reached the handler at all.
  Two gates, not one.
- **Absolute paths in the log.** The first run wrote
  `C:\Users\...\22_application_activity_logger\data\notes.txt` on every line. A
  `display()` helper now shortens paths relative to the application folder — a log is
  read by a person, and only the part that varies is worth printing.
- **An off-by-one line count.** `content.count("\n") + 1` reported 7 lines for a
  6-line file, because the file ends with a newline. `len(content.splitlines())` is
  correct.

---

## `00_concepts.py` - the basics, before the application

A plain top-to-bottom script - **no functions**, nothing clever. Read it from the first
line to the last:

| # | Shows |
|---|---|
| 1 | `print()` vs logging |
| 2 | the five levels, DEBUG to CRITICAL |
| 3 | sending the log to a file |
| 4 | writing and reading a file: `r`, `w`, `a`, and `with` |
| 5 | when the file is missing - `FileNotFoundError` and `try` |

```bash
python 00_concepts.py
```

It imports nothing from this folder, and deletes the two files it creates
(`demo.log`, `demo.txt`) on the last three lines.

---

## YouTube demonstration link

<your-youtube-video-link>

---

## Submission links

- **GitHub Repository:** `<your-public-github-repository-link>`
- **YouTube Explanation:** `<your-youtube-video-link>`
