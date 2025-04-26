# Introduction to break and continue statements

# The `break` statement is used to immediately exit a loop, regardless of its current iteration.
# It is commonly used to terminate a loop when a specific condition is met.
# Syntax:
#   break

# Example of a break statement:
for i in range(5):
    if i == 3:
        break  # Exits the loop when i equals 3
    print(i)  # Prints 0, 1, 2

# The `continue` statement is used to skip the rest of the code inside a loop for the current iteration 
# and continue with the next iteration.
# Syntax:
#   continue

# Example of a continue statement:
for i in range(5):
    if i == 3:
        continue  # Skips the current iteration when i equals 3
    print(i)  # Prints 0, 1, 2, 4

for m in range(7):
    if m == 4:
        continue
    print(m)

for n in range (7):
    if n ==4:
        break
    print("my fav song ", n)