"""
00_concepts.py - the basics behind exercise 22
==============================================
Run this first:

    python 00_concepts.py

A plain top-to-bottom script - no functions, nothing clever. Read it
from the first line to the last and you will know enough to read the
application in this folder.

    1  print() vs logging
    2  the five levels
    3  sending the log to a file
    4  writing and reading a file
    5  when the file is missing
"""
import logging
import os
import sys


# ===========================================================
print()
print("1. print() vs logging")
print("=" * 50)

# print just writes text.
print("print('File was empty')  ->  File was empty")

# A logger also says how serious it is.
log = logging.getLogger("demo")
log.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter("%(levelname)-8s %(message)s"))
log.addHandler(handler)

print("log.warning('File was empty')  ->")
log.warning("File was empty")


# ===========================================================
print()
print("2. The five levels")
print("=" * 50)

log.debug("a detail for the developer")
log.info("something normal happened")
log.warning("odd, but the program carries on")
log.error("this operation failed")
log.critical("the program is in trouble")

print()
print("In this exercise:")
print("   INFO      User logged in")
print("   WARNING   File was empty")
print("   ERROR     File could not be opened")


# ===========================================================
print()
print("3. Sending the log to a file")
print("=" * 50)

# A FileHandler writes to a file instead of the screen.
file_log = logging.getLogger("demo.file")
file_log.setLevel(logging.DEBUG)
file_log.propagate = False              # do not also print on screen
file_handler = logging.FileHandler("demo.log", encoding="utf-8")
file_handler.setFormatter(logging.Formatter("%(levelname)-8s %(message)s"))
file_log.addHandler(file_handler)

file_log.info("User logged in")
file_log.error("File could not be opened")

print("Nothing appeared on screen. demo.log now holds:")
print()
with open("demo.log", encoding="utf-8") as f:
    print(f.read())

print("This exercise uses two files:")
print("   logs/application.log   everything")
print("   logs/error.log         only the failures")


# ===========================================================
print()
print("4. Writing and reading a file")
print("=" * 50)

# "w" writes, and empties the file first.
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("first line\n")

# "a" adds to the end.
with open("demo.txt", "a", encoding="utf-8") as f:
    f.write("second line\n")

# "r" reads.
with open("demo.txt", "r", encoding="utf-8") as f:
    contents = f.read()

print("the file now holds:", repr(contents))
print()
print("   'r'  read")
print("   'w'  write - empties the file first")
print("   'a'  append - adds to the end")
print("   `with`  closes the file for you")


# ===========================================================
print()
print("5. When the file is missing")
print("=" * 50)

try:
    with open("nope.txt", encoding="utf-8") as f:
        f.read()
except FileNotFoundError:
    print("FileNotFoundError - but the program is still running.")

print()
print("Without the try, the program would stop here.")
print("file_handler.py catches this and logs it as an ERROR.")


# ===========================================================
# Tidy up the two files this script made.
# logging.shutdown() closes demo.log first - Windows will not delete a
# file that is still open.
logging.shutdown()
os.remove("demo.log")
os.remove("demo.txt")

print()
print("Next: read logger_config.py, then run `python main.py`.")
print()
