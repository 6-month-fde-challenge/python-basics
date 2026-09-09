"""
main.py - the command-line front end for the organizer package
==============================================================
main.py is NOT part of the package. It imports it, the way any other
program would:

    from organizer import detect, move, setup_logging

That separation is the point of exercise 25. `organizer/` could be
copied into another project unchanged; this file is the part that knows
about argv, printing and exit codes.

RUN IT
    python main.py                   organize demo_files/ into organized/
    python main.py <folder>          organize a different folder
    python main.py --lock notes.txt  hold a file open, to demonstrate the
                                     permission-error branch

THE PER-FILE LOOP IS THE SAME SHAPE AS EXERCISE 23
    try / except FileOrganizerError / continue. One unmovable file costs
    one file, never the run.
"""
import os
import sys

from organizer import (
    FileOrganizerError,
    UnsupportedFileError,
    detect,
    get_logger,
    move,
    scan,
    setup_logging,
    start_run,
    summarise_categories,
)

log = get_logger("main")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SOURCE = os.path.join(BASE_DIR, "demo_files")
DEFAULT_DEST = os.path.join(BASE_DIR, "organized")

LINE = "=" * 72


def parse_args(argv):
    """
    Turn argv into (source, lock_name).

    Hand-parsed rather than argparse, because two options do not justify
    the dependency.
    """
    lock_name = None
    positional = []

    index = 0
    while index < len(argv):
        if argv[index] == "--lock" and index + 1 < len(argv):
            lock_name = argv[index + 1]
            index += 2
        else:
            positional.append(argv[index])
            index += 1

    source = positional[0] if positional else DEFAULT_SOURCE
    return source, lock_name


def organize(files, destination):
    """
    Detect and move every file. Return (moved, unsupported, failed).

    One try/except per file. `continue` is implicit - the loop simply
    reaches the next iteration - which is why each branch appends to a
    list before falling through.
    """
    moved = []
    unsupported = []
    failed = []

    for path in files:
        name = os.path.basename(path)

        try:
            category = detect(path)
            target = move(path, destination, category)

        except UnsupportedFileError as error:
            # Caught BEFORE the base class, because an unknown extension
            # is not a failure - it is a file this program has no opinion
            # about, and leaving it where it is, is the right answer.
            log.warning("SKIPPED     %s : %s", name, error.message)
            unsupported.append((name, error.extension or "none"))

        except FileOrganizerError as error:
            # Every other error the package raises: missing, locked,
            # destination unusable, no free name.
            log.error("FAILED      %s : %s", name, error.message)
            failed.append((name, type(error).__name__, error.message))

        except Exception as error:
            # Not one of ours, so it is a defect in this program.
            log.critical("FAILED      %s : unexpected %s",
                         name, type(error).__name__, exc_info=True)
            failed.append((name, type(error).__name__, str(error)))

        else:
            # The single record of a successful operation. Written here
            # rather than inside the package, so every outcome - moved,
            # skipped, failed - is logged by the same code at the same
            # level of detail, and the log counts match the report.
            log.info("MOVED  %s -> %s/%s",
                     name, category, os.path.basename(target))
            moved.append((name, category, os.path.basename(target)))

    return moved, unsupported, failed


def print_report(moved, unsupported, failed):
    """Print what happened, grouped so the eye can find it."""
    print()
    print(LINE)
    print("   MOVED")
    print(LINE)
    if not moved:
        print("   Nothing.")
    else:
        # Group by destination category, so the output mirrors the
        # folders the user is about to look at.
        by_category = {}
        for name, category, new_name in moved:
            by_category.setdefault(category, []).append((name, new_name))

        for category in sorted(by_category):
            print(f"   {category}/")
            for name, new_name in by_category[category]:
                arrow = f"{name}" if name == new_name else f"{name}  ->  {new_name}"
                print(f"      {arrow}")

    print()
    print(LINE)
    print("   LEFT ALONE - unsupported file type")
    print(LINE)
    if not unsupported:
        print("   None.")
    else:
        for name, extension in unsupported:
            print(f"   {name:<28} {extension}")

    print()
    print(LINE)
    print("   FAILED")
    print(LINE)
    if not failed:
        print("   None.")
    else:
        for name, kind, message in failed:
            print(f"   {name:<28} {kind:<22} {message}")


def print_summary(files, moved, unsupported, failed, destination):
    """Print the counts and where to look next."""
    print()
    print(LINE)
    print("   SUMMARY")
    print(LINE)
    print(f"   Files examined      : {len(files)}")
    print(f"   {'Moved':<20}: {len(moved)}")
    print(f"   Unsupported         : {len(unsupported)}")
    print(f"   Failed              : {len(failed)}")
    print(f"   Destination         : {os.path.relpath(destination, BASE_DIR)}")

    log.info("SUMMARY examined=%d moved=%d unsupported=%d failed=%d",
             len(files), len(moved), len(unsupported), len(failed))


def main(argv):
    """Scan, organize, report. Returns a process exit code."""
    parent = setup_logging()
    source, lock_name = parse_args(argv)
    destination = DEFAULT_DEST

    start_run(parent,
              os.path.relpath(source, BASE_DIR),
              os.path.relpath(destination, BASE_DIR))
    log.debug("Categories known: %s", summarise_categories())

    try:
        files = scan(source)
    except FileOrganizerError as error:
        # The source folder itself is missing. Nothing to be tolerant
        # about, so this is the one failure that ends the run.
        log.critical("Cannot start: %s", error)
        print(f"   Source folder not found: {source}")
        return 1

    if not files:
        log.warning("Nothing to organize in %s", source)
        print(f"   {source} contains no files.")
        return 0

    # --lock holds a file open for the duration of the run. On Windows an
    # open handle makes the move fail with PermissionError, which is how
    # the permission branch is demonstrated without changing any ACLs.
    handle = None
    if lock_name:
        lock_path = os.path.join(source, lock_name)
        try:
            handle = open(lock_path, "r+", encoding="utf-8")
            log.warning("Holding %s open for the whole run (--lock)", lock_name)
        except OSError as error:
            log.error("Could not lock %s: %s", lock_name, error)

    try:
        moved, unsupported, failed = organize(files, destination)
    finally:
        # `finally`, so the handle is released even if organize() raises.
        if handle is not None:
            handle.close()
            log.debug("Released the lock on %s", lock_name)

    print_report(moved, unsupported, failed)
    print_summary(files, moved, unsupported, failed, destination)

    print()
    print("   Logs: logs/organizer.log (every operation), logs/errors.log (failures)")
    log.info("RUN FINISHED")

    # Non-zero when something failed, so the exit code is usable in a
    # script. Unsupported files are not failures.
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
