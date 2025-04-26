# This is an infinite loop that repeatedly prints "hello"

while True:
    n1 = int(input("Enter a number = "))
    n2 = int(input("Enter another number = "))
    print("The sum of the two numbers is ", n1 + n2)

    r = input("Do you want to continue? (y/n) ")
    if r == 'n':
        break
