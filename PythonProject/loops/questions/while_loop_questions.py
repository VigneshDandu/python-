'''sum = 0
for i in range(51):
    if i%2==0:
       sum = sum +i
print(sum)

for m in range(1,21):
    print( str(m) + " * "  + str(m) + " = " + str(m**2))
    '''

'''n = 1
sum = 0
while n<=20:
    if n%2!=0:
       sum += n
    n +=1
print(sum)'''

while True:
    name = input("Enter your name: ")
    ph = int(input("Enter your phone number: "))
    total = 0
    while True:
         qty= int(input("Enter the quantity: "))
         amount = int(input("Enter the amount: "))
         total = total + qty*amount
         r = input("Do you want to add more products? (y/n) ")
         if r == "n":
             break
    print("total amount is ", total)
    a= input("another person (y/n) ")
    if a == "y":
     print(" details ")
    elif a== "n":
        print("thanks for shopping")
        break

