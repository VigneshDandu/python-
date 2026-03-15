A = ["ross", "rachel", "Monica", "Joe"]
#write a program to swap first and forth element
print(A)
temp = A[0]
A[0]=A[3]
A[3]= temp
print(A)

#method 2 (Easier method)
A[0],A[3]=A[3],A[0]
print(A)
print()

#write a program to add a new value at second position
A.insert(1,"ruth")
print(A)

#write a program to delete a value from 3rd position
A.pop(2)
print(A)

del A[2]
print(A)

A.append('Carol')
A.append('Dave')
print(A)

b =[13,7,12,10]
#write a program to multiply all the numbers in the list
multilply = 1
for i in (b):
    multilply*=i
print(multilply)

#get largest element
b.sort()
print(b[-1])

#smallest value
print(b[0])