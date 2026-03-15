#to check if prime or not
n = int(input("Enter a number: "))
for i in range(2,n):
    if n%i==0:
        print("Not a prime number")
        print(i,"times",n//i,"is",n)
        break
else:
    print("Prime number")