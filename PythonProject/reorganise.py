import os
import shutil

# ─────────────────────────────────────────────
#  Run this script from INSIDE your PythonProject folder:
#  cd PythonProject
#  python reorganise.py
# ─────────────────────────────────────────────

BASE = os.path.dirname(os.path.abspath(__file__))

moves = [

    # ── BASICS ───────────────────────────────
    ("basics/firstprogram.py",                  "basics/firstprogram.py"),
    ("basics/variables.py",                     "basics/variables.py"),
    ("basics/datatypes_and user input.py",      "basics/datatypes_and_user_input.py"),
    ("basics/type casting.py",                  "basics/type_casting.py"),
    ("basics/queastions.py",                    "basics/questions.py"),

    # ── BASICS / OPERATORS (new sub-folder) ──
    ("basics/operators and operands.py",        "basics/operators/arithmetic_operators.py"),
    ("basics/binary number.py",                 "basics/operators/binary_operators.py"),
    ("basics/membership operator.py",           "basics/operators/membership_operator.py"),

    # ── STRINGS ──────────────────────────────
    ("string/creation of string.py",            "strings/string_basics.py"),
    ("string/methods on string.py",             "strings/string_methods.py"),
    ("string/Python string methods used to check different properties of a string.py",
                                                "strings/string_check_methods.py"),
    ("string/string slicing.py",                "strings/string_slicing.py"),

    # ── STRINGS / QUESTIONS (new sub-folder) ─
    ("string/some basic questions.py",          "strings/questions/basic_questions.py"),
    ("string/q2.py",                            "strings/questions/prime_check.py"),
    ("string/q3.py",                            "strings/questions/palindrome.py"),
    ("string/q3 alt.py",                        "strings/questions/palindrome_alt.py"),
    ("string/questions.py",                     "strings/questions/fibonacci.py"),

    # ── CONDITIONALS (new folder) ────────────
    ("basics/conditional statements.py",        "conditionals/conditional_statements.py"),
    ("problems/problems.py",                    "conditionals/questions/problems.py"),
    ("problems/problems 2.py",                  "conditionals/questions/problems2.py"),

    # ── LOOPS ────────────────────────────────
    ("loops/loops.py",                          "loops/for_loop.py"),
    ("loops/while loop.py",                     "loops/while_loop.py"),
    ("loops/while true.py",                     "loops/while_true.py"),
    ("loops/nested loops.py",                   "loops/nested_loops.py"),
    ("loops/break and continue statement.py",   "loops/break_and_continue.py"),

    # ── LOOPS / QUESTIONS ────────────────────
    ("loops/for loop with conditional stmt.py", "loops/questions/for_loop_questions.py"),
    ("loops/problems 3 in loop .py",            "loops/questions/while_loop_questions.py"),

    # ── LISTS ────────────────────────────────
    ("lists/lists.py",                          "lists/lists_basics.py"),
    ("lists/list function.py",                  "lists/list_functions.py"),
    ("lists/list function2.py",                 "lists/list_functions2.py"),
    ("lists/list iteration.py",                 "lists/list_iteration.py"),
    ("lists/slicing lists.py",                  "lists/list_slicing.py"),

    # ── LISTS / QUESTIONS ────────────────────
    ("lists/problems.py",                       "lists/questions/list_problems.py"),

    # ── PATTERNS (new folder) ────────────────
    ("problems/pat...py",                       "patterns/pattern1.py"),
    ("problems/pat2.py",                        "patterns/pattern2.py"),
    ("problems/pat3.py",                        "patterns/pattern3.py"),
    ("problems/pat4.py",                        "patterns/pattern4.py"),
    ("problems/pat5.py",                        "patterns/pattern5.py"),

    # ── FUNCTIONS ────────────────────────────
    ("functions/begin.py",                      "functions/functions_basics.py"),
    ("functions/arg&para.py",                   "functions/arguments_and_parameters.py"),

    # ── TUPLES ───────────────────────────────
    ("tuple/tuple.py",                          "tuples/tuples.py"),

    # ── PROJECTS ─────────────────────────────
    ("projects/weight convertor.py",            "projects/weight_converter.py"),
]

print("🗂  Starting reorganisation...\n")

for src_rel, dst_rel in moves:
    src = os.path.join(BASE, src_rel)
    dst = os.path.join(BASE, dst_rel)

    if not os.path.exists(src):
        print(f"  ⚠️  Not found (skip): {src_rel}")
        continue

    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.move(src, dst)
    print(f"  ✅  {src_rel}  →  {dst_rel}")

# Add __init__.py to every package folder
print("\n📦  Adding __init__.py files...")
for root, dirs, files in os.walk(BASE):
    # skip hidden folders
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    init = os.path.join(root, "__init__.py")
    if not os.path.exists(init):
        open(init, "w").close()
        rel = os.path.relpath(init, BASE)
        print(f"  ✅  Created {rel}")

print("\n🎉  Done! Your project is now organised.\n")
print("""
New Structure:
PythonProject/
├── basics/
│   ├── firstprogram.py
│   ├── variables.py
│   ├── datatypes_and_user_input.py
│   ├── type_casting.py
│   ├── questions.py
│   └── operators/
│       ├── arithmetic_operators.py
│       ├── binary_operators.py
│       └── membership_operator.py
├── strings/
│   ├── string_basics.py
│   ├── string_methods.py
│   ├── string_check_methods.py
│   ├── string_slicing.py
│   └── questions/
│       ├── basic_questions.py
│       ├── prime_check.py
│       ├── palindrome.py
│       ├── palindrome_alt.py
│       └── fibonacci.py
├── conditionals/
│   ├── conditional_statements.py
│   └── questions/
│       ├── problems.py
│       └── problems2.py
├── loops/
│   ├── for_loop.py
│   ├── while_loop.py
│   ├── while_true.py
│   ├── nested_loops.py
│   ├── break_and_continue.py
│   └── questions/
│       ├── for_loop_questions.py
│       └── while_loop_questions.py
├── lists/
│   ├── lists_basics.py
│   ├── list_functions.py
│   ├── list_functions2.py
│   ├── list_iteration.py
│   ├── list_slicing.py
│   └── questions/
│       └── list_problems.py
├── patterns/
│   ├── pattern1.py  →  pattern5.py
├── functions/
│   ├── functions_basics.py
│   └── arguments_and_parameters.py
├── tuples/
│   └── tuples.py
└── projects/
    └── weight_converter.py
""")
