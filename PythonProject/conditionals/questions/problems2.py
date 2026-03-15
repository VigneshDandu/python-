# write a program to check if a number is positive
number = int(input("enter a number = "))
if number < 0:
    print("Entered number is negative")
else:
    print("Entered number is positive")

# write a program to check whether a number is odd or even

numb = int(input("enter a number = "))
if numb % 2 ==0:
     print("The number is even")
else:
     print("Entered number is odd")

# write a program to create an area calculator

print("\nArea Calculator")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = int(input("Choose a shape (1-3): "))

if choice == 1:
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14159 * radius * radius
    print(f"Area of the circle = {area} ")
elif choice == 2:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"Area of the rectangle = {area}")
elif choice == 3:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"Area of the triangle = {area}")
else:
    print("Invalid choice, exiting the program.")

# write a program to check whether the passed letter is a vowel or not

letter= input(" Enter a letter =")
if letter in "aeiouAEIOU" :
    print("Entered letter is a vowel")
else:
    print("Entered letter is consonant")

# write a program to check if a number is a single digit number, 2 digit  ,... upto 5 digits
print("********Number Checker*********M1")
num = int(input("Enter a number ="))
if 0<num<9:
    print("Entered number is a single digit number")
elif 10<num<99:
    print("Entered number is 2 digit number")
elif 100<num<999:
    print("Entered number is 3 digit number")
elif 1000<num<9999:
    print("Entered number is 4 digit number")
elif 100000<num<999999:
    print("Entered number is 5 digit number")

#incorrect code below
"""print("********Number Checker*********M2")
no = int(input("Enter a number ="))
if no %10 <=0:
    print("entered number is single digit")
elif no %100 <=0:
    print("entered number is double digit")
elif no %1000 <=0:
    print("entered number is triple digit")
elif no%10000<=0:
    print("Entered number is four digit")
elif no%100000<= 0:
    print("Entered number if five digit")"""





