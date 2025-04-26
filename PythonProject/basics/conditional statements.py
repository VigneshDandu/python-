# if statement
a = 19
a= int(input("enter your desired number "))
if a <20 :
    print( "a is less thn condition")

print("thank u") # this will execute always

#if-else statement

b = input("enter a string ")
if "a" in b:
    print(" memeber is present")
else :
    print("absent")
# 2nd
grades = int(input("enter grade :"))
if grades >=75:
    print("Eligible for examination")
else:
    print("Not Eligible for examination")

#if-elif-else statemnet

marks = float(input("enter your marks :"))

if marks >= 90 :
    print("grade A")
elif marks >= 80 and marks <90:
    print("grade B")
elif marks >=70 and marks < 80:
    print("grade C")
else:
    print("grade D")

# nested if

marks =87
if marks >= 70:
    print("you can have sweets")
    if marks >= 85:
        print("you can have mobile")
        if marks >= 90:
            print("you can have a trip")
else:
    print("you can not have sweets")

#short hand if statement

number = 56
if number >= 50 : print("more than half")

#short hand if-else statement

num = 90
print("more than 80") if num >= 80 else print("less than 80")