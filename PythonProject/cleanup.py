import os
import shutil

# ─────────────────────────────────────────────
#  Run this from INSIDE PythonProject folder:
#  cd PythonProject
#  python cleanup.py
# ─────────────────────────────────────────────

BASE = os.path.dirname(os.path.abspath(__file__))

print("🧹 Starting cleanup...\n")

# ── 1. RENAME long-named list files ──────────
long_name_moves = [
    (
        "lists/ Sum of a List Write a program to find the sum of all numbers in this list without UsingSum().py",
        "lists/questions/sum_of_list.py"
    ),
    (
        "lists/Reverse a List Reverse this list without using .reverse() or [::-1].py",
        "lists/questions/reverse_list.py"
    ),
    (
        "string/Count Vowels Write a program that iterates through a string and counts how many vowels are in it.py",
        "strings/questions/count_vowels.py"
    ),
]

for src_rel, dst_rel in long_name_moves:
    src = os.path.join(BASE, src_rel)
    dst = os.path.join(BASE, dst_rel)
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.move(src, dst)
        print(f"  ✅  Renamed: {os.path.basename(src_rel)}")
        print(f"       →  {dst_rel}")
    else:
        print(f"  ⚠️   Not found (skip): {src_rel}")

# ── 2. REMOVE old empty/leftover folders ─────
folders_to_remove = [
    "string",       # old string folder (files already moved)
    "tuple",        # old tuple folder (replaced by tuples/)
    "problems",     # now empty after reorganise
]

print()
for folder in folders_to_remove:
    path = os.path.join(BASE, folder)
    if os.path.exists(path):
        # Only remove if truly empty (or only has __init__.py / __pycache__)
        all_files = []
        for root, dirs, files in os.walk(path):
            for f in files:
                if f not in ("__init__.py",):
                    all_files.append(f)
        if not all_files:
            shutil.rmtree(path)
            print(f"  🗑️   Removed empty folder: {folder}/")
        else:
            print(f"  ⚠️   Skipped (not empty): {folder}/ → contains {all_files}")
    else:
        print(f"  ⚠️   Folder not found (skip): {folder}/")

# ── 3. MOVE AI_DS_Notes OUT of PythonProject ─
print()
ai_notes_src = os.path.join(BASE, "AI_DS_Notes")
# Move one level up (sibling of PythonProject)
parent = os.path.dirname(BASE)
ai_notes_dst = os.path.join(parent, "AI_DS_Notes")

if os.path.exists(ai_notes_src):
    if not os.path.exists(ai_notes_dst):
        shutil.move(ai_notes_src, ai_notes_dst)
        print(f"  ✅  Moved AI_DS_Notes/ out of PythonProject/")
        print(f"       →  Now at: ../AI_DS_Notes/")
    else:
        print(f"  ⚠️   AI_DS_Notes/ already exists outside. Merge manually.")
else:
    print(f"  ⚠️   AI_DS_Notes/ not found inside PythonProject/")

# ── 4. Ensure __init__.py in all new folders ─
print("\n📦  Checking __init__.py files...")
for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
    init = os.path.join(root, "__init__.py")
    if not os.path.exists(init):
        open(init, "w").close()
        rel = os.path.relpath(init, BASE)
        print(f"  ✅  Created {rel}")

print("\n🎉  Cleanup done!\n")
print("""
Final clean structure:
─────────────────────────────────────
 PythonProject/                  ← Python course files only
 ├── basics/
 │   ├── operators/
 │   └── ...
 ├── strings/
 │   └── questions/
 │       ├── count_vowels.py     ← moved from string/
 │       ├── basic_questions.py
 │       ├── prime_check.py
 │       ├── palindrome.py
 │       ├── palindrome_alt.py
 │       └── fibonacci.py
 ├── conditionals/
 ├── loops/
 ├── lists/
 │   └── questions/
 │       ├── list_problems.py
 │       ├── sum_of_list.py      ← renamed from long name
 │       └── reverse_list.py     ← renamed from long name
 ├── patterns/
 ├── functions/
 ├── tuples/
 └── projects/

 AI_DS_Notes/                    ← moved OUT of PythonProject
 ├── Module_1_Introduction_to_AI.md
 ├── Module_2_Search_Techniques.md
 └── Question_Bank_Module_1_and_2.md
─────────────────────────────────────
""")
