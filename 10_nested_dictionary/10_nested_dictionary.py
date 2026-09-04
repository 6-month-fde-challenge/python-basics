"""
Exercise 10 - Nested Dictionary Challenge
=========================================
Concepts practised: dictionaries, nested dictionaries, key access,
                    updating values, adding new keys, get()

CONSTRAINT: no loops. Every value is reached by direct key access.

HOW NESTED DICTIONARIES ARE ACCESSED
------------------------------------
A dictionary stores KEY : VALUE pairs. A value can itself be a dictionary -
that is what makes it "nested".

employee ---> "name"       : "Amit"
         ---> "department" : "Engineering"
         ---> "skills"     : ---> "language" : "Python"
                             ---> "database" : "PostgreSQL"
                             ---> "cloud"    : "AWS"
         ---> "salary"     : 80000

Lists use POSITIONS  -> students[1][2]
Dicts use KEY NAMES  -> employee["skills"]["language"]

The FIRST key opens the outer dictionary.
The SECOND key opens the inner dictionary that the first key returned.
"""

# ---------------------------------------------------------------------------
# Create the nested dictionary
# ---------------------------------------------------------------------------

employee = {
    "name": "Amit",
    "department": "Engineering",
    "skills": {
        "language": "Python",
        "database": "PostgreSQL",
        "cloud": "AWS"
    },
    "salary": 80000
}

print("Full employee record :")
print("  ", employee)
print()


# ---------------------------------------------------------------------------
# 1. Employee name -> one key, top level
# ---------------------------------------------------------------------------
print("1. Name                :", employee["name"])


# ---------------------------------------------------------------------------
# 2. Department -> one key, top level
# ---------------------------------------------------------------------------
print("2. Department          :", employee["department"])


# ---------------------------------------------------------------------------
# 3. The COMPLETE skills dictionary -> one key returns the whole inner dict
# ---------------------------------------------------------------------------
print("3. Skills dictionary   :", employee["skills"])
print("   Type of employee['skills'] :", type(employee["skills"]), "<- a dict inside a dict")
print()


# ---------------------------------------------------------------------------
# 4. Programming language -> TWO keys: outer "skills", then inner "language"
# ---------------------------------------------------------------------------
print("4. Language            :", employee["skills"]["language"])


# ---------------------------------------------------------------------------
# 5. Database -> outer "skills", then inner "database"
# ---------------------------------------------------------------------------
print("5. Database            :", employee["skills"]["database"])


# ---------------------------------------------------------------------------
# 6. Cloud technology -> outer "skills", then inner "cloud"
# ---------------------------------------------------------------------------
print("6. Cloud               :", employee["skills"]["cloud"])
print("   Type of the inner value    :", type(employee["skills"]["cloud"]), "<- now a string")
print()


# ===========================================================================
# UPDATING EXISTING VALUES
# ===========================================================================

print("=" * 62)
print("UPDATING EXISTING VALUES")
print("=" * 62)

# --- 7. Change the language (a value INSIDE the nested dictionary) ---------
print("7. Language before     :", employee["skills"]["language"])
employee["skills"]["language"] = "Python + JavaScript"
print("   Language after      :", employee["skills"]["language"])

# --- 8. Change the salary (a value at the TOP level) -----------------------
print("8. Salary before       :", employee["salary"])
employee["salary"] = 95000
print("   Salary after        :", employee["salary"])
print()


# ===========================================================================
# ADDING NEW KEYS
# ===========================================================================

print("=" * 62)
print("ADDING NEW KEYS")
print("=" * 62)
print("Same syntax as updating! If the key EXISTS it is changed.")
print("If the key DOES NOT exist it is CREATED. That is the whole rule.")
print()

# --- 9. Add "experience": 3 at the TOP level -------------------------------
print("9. Keys before  :", list(employee.keys()))
employee["experience"] = 3
print("   Keys after   :", list(employee.keys()))
print("   Experience   :", employee["experience"])

# --- 10. Add a new skill INSIDE the nested skills dictionary ---------------
print()
print("10. Skills before :", employee["skills"])
employee["skills"]["framework"] = "Django"
print("    Skills after  :", employee["skills"])
print("    New skill     :", employee["skills"]["framework"])


# ---------------------------------------------------------------------------
# The final updated record
# ---------------------------------------------------------------------------
print()
print("=" * 62)
print("FINAL EMPLOYEE RECORD")
print("=" * 62)
print(employee)
print()
print("Top level keys :", list(employee.keys()))
print("Skill keys     :", list(employee["skills"].keys()))
print("Skill values   :", list(employee["skills"].values()))


# ===========================================================================
# SAFE ACCESS - what happens when a key does not exist
# ===========================================================================

print()
print("=" * 62)
print("SAFE ACCESS : [] vs get()")
print("=" * 62)

# Square brackets CRASH on a missing key
try:
    print(employee["bonus"])
except KeyError as error:
    print("employee['bonus']            -> KeyError:", error, "(crashes)")

# get() returns None instead of crashing, and lets you supply a default
print("employee.get('bonus')        ->", employee.get("bonus"), "(no crash)")
print("employee.get('bonus', 0)     ->", employee.get("bonus", 0), "(with a default value)")
print("employee.get('name')         ->", employee.get("name"), "(works normally when the key exists)")
print()
print("Nested get() works too:")
print("employee['skills'].get('testing', 'Not listed') ->",
      employee["skills"].get("testing", "Not listed"))
