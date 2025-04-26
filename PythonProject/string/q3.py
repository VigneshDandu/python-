#palindrome
n = input("Enter the number of words : ")
print(n.isnumeric())
if n.isnumeric()==True:
 print(n[::-1])