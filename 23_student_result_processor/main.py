"""
main.py - process every student, skip the broken ones, report at the end
========================================================================
The whole assignment turns on one sentence: "instead of stopping when an
error occurs, the program should log the error and continue processing
the remaining students."

That is this loop, and nothing else:

    for row in rows:
        try:
            student = student_ops.build_student(row)
            result = result_calc.process(student)
        except StudentDataError as error:
            log.error(...)          <- write it down
            skipped.append(...)     <- remember it
            continue                <- and carry on
        results.append(result)

`continue` is the entire fault-tolerance mechanism. Everything else -
the exception classes, the two log files, the summary table - exists to
make that one line safe to rely on.

FOUR MODULES, FOUR JOBS
    exceptions.py      the vocabulary for failure
    student_ops.py     reading and validating records
    result_calc.py     total, percentage, grade, pass/fail
    logger_config.py   where log records go

RUN IT
    python main.py                 process data/students.csv
    python main.py <path.csv>      process a different file
"""
import logging
import os
import sys

import result_calc
import student_ops
from exceptions import StudentDataError
from logger_config import get_logger, setup_logging, start_run

log = get_logger("main")

LINE = "=" * 78


def process_all(rows):
    """
    Process every raw row. Return (results, skipped).

    Each iteration is wrapped on its own, so the loop is the unit of
    fault tolerance: one bad row costs one row.
    """
    results = []
    skipped = []

    for position, row in enumerate(rows, start=1):
        label = (row.get("roll") or f"row {position}").strip() or f"row {position}"

        try:
            student = student_ops.build_student(row)
            result = result_calc.process(student)

        except StudentDataError as error:
            # Every one of our own exception types lands here: missing
            # info, bad marks, out of range, wrong subject count, failed
            # arithmetic. The record is logged and abandoned.
            log.error("SKIPPED %s - %s: %s",
                      label, type(error).__name__, error.message)
            skipped.append((label, type(error).__name__, error.message))
            continue

        except Exception as error:
            # Not one of ours, so it is a defect rather than bad data.
            # CRITICAL and a traceback - but still `continue`, because
            # the other students are not at fault.
            log.critical("SKIPPED %s - unexpected %s",
                         label, type(error).__name__, exc_info=True)
            skipped.append((label, type(error).__name__, str(error)))
            continue

        else:
            results.append(result)

        finally:
            log.debug("Finished with %s", label)

    return results, skipped


def print_results(results):
    """Print the result sheet for every student that made it through."""
    print()
    print(LINE)
    print("   RESULT SHEET")
    print(LINE)

    if not results:
        print("   No student could be processed.")
        return

    header = (f"   {'ROLL':<6} {'NAME':<16} {'TOTAL':>8} {'PERCENT':>8} "
              f"{'GRADE':>6}  STATUS")
    print(header)
    print("   " + "-" * (len(header) - 3))

    for r in results:
        print(f"   {r['roll']:<6} {r['name']:<16} "
              f"{r['total']:>4.0f}/{r['maximum']:<3} {r['percentage']:>7.2f}% "
              f"{r['grade']:>6}  {r['status']}")
        if r["status"] == "FAIL":
            print(f"   {'':<6} -> {r['reason']}")


def print_skipped(skipped):
    """Print the records that could not be processed, and why."""
    print()
    print(LINE)
    print("   SKIPPED RECORDS")
    print(LINE)

    if not skipped:
        print("   None - every record was usable.")
        return

    for label, kind, message in skipped:
        print(f"   {label:<8} {kind:<24} {message}")


def print_summary(results, skipped, rows):
    """Print the counts, and the class statistics over what survived."""
    print()
    print(LINE)
    print("   SUMMARY")
    print(LINE)

    passed = [r for r in results if r["status"] == "PASS"]
    failed = [r for r in results if r["status"] == "FAIL"]

    print(f"   Records read        : {len(rows)}")
    print(f"   Processed           : {len(results)}")
    print(f"   Skipped (logged)    : {len(skipped)}")
    print(f"   Passed / Failed     : {len(passed)} / {len(failed)}")

    if results:
        # Guarded because dividing by len(results) with nothing in it is
        # the same ZeroDivisionError the calculator protects against.
        average = sum(r["percentage"] for r in results) / len(results)
        best = max(results, key=lambda r: r["percentage"])
        print(f"   Class average       : {average:.2f}%")
        print(f"   Highest             : {best['name']} ({best['percentage']:.2f}%)")

    log.info("Summary: read=%d processed=%d skipped=%d pass=%d fail=%d",
             len(rows), len(results), len(skipped), len(passed), len(failed))


def main(argv):
    """Load, process, report. Returns a process exit code."""
    # setup_logging() returns the PARENT logger ("results"); the module
    # level `log` above is its child ("results.main"). Kept in separate
    # names so the banner is written once, by the parent.
    parent = setup_logging(console_level=logging.WARNING)

    paths = [a for a in argv if not a.startswith("--")]
    source = paths[0] if paths else student_ops.DATA_FILE

    start_run(parent, os.path.basename(source))

    try:
        rows = student_ops.load_rows(source)

    except OSError:
        # load_rows already logged this CRITICAL. There is nothing to
        # process, so this is the one failure that does end the run.
        print("   The student data file could not be read. See logs/error.log")
        return 1

    results, skipped = process_all(rows)

    print_results(results)
    print_skipped(skipped)
    print_summary(results, skipped, rows)

    print()
    print("   Logs: logs/application.log (everything), logs/error.log (failures)")
    log.info("RUN FINISHED")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
