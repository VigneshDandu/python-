num = int(input("Enter a number: "))
rev = 0
temp = num
while num>0:
    dig = num%10
    rev = rev*10 +dig
    num = num//10

print("the reverse number will be ",rev)
if rev == temp:
    print("It is palindrome")
else:
    print("It is not palindrome")
