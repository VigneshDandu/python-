# Example tasks/questions using loops and conditional statements:
# 1. Print all even numbers between 1 and 50.
for m in range (1,101):
    if m%2==0:
        print(m)

# 2. Identify numbers between 1 and 100 that are divisible by both 3 and 9.

for n in range (1,101):
    if n%3==0 and n%9==0:
        print(n)

# 3. Write a loop to calculate the sum of all odd numbers between 1 and 100.
sum = 0
for f in range (1,101):
    if f%2!=0:
        sum = sum +f
print(sum)

# 4. Create a pattern, e.g., print a square or triangle of '*' based on input size.
k = int(input("Enter the number of rows:"))
s = int(input("Enter the number of columns:"))
for x in range (k):
    for y in range (s):
         print("*", end ="")
    print("")

for i in range(1, 101):
    # Task: Print numbers between 1 and 100 that are divisible by both 2 and 19.
    if i % 2 == 0 and i % 19 == 0:
        print(i)


