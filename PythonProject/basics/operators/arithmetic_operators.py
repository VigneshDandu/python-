print(3+5)
print(19%4)
''' for power to any base'''
print(5**4)
''' for getting quotient we use floor divion'''
print(9.3//4.0)

'''comparison opeerators'''

print(8>4)
print(8>9)
print(8==7)
print(8!=7)
print(3>=3)


"""logical operator (and,or, not)"""

print(4>9 and 7<6) #this will return false as for "and" both should be true"""
print(8>7 or 6>7) # if any one is true than true otherwise false"""
print(3>4 or 4<5)  #this will return true """
""" BUT """
print(not(3>4 or 4<5))  # not changes from true to false and false to true

# assignment operator ( = , += , -= , *=)

x = 4
print(x)
x +=4
print(x)
# x is now 8
b=0
b-=2
print(b)

x *=4
print(x)


# binary number
print(bin(-123))
print(bin(10))


a = 15
b = 16

print( a & b)



#Check if a number is even or odd using the modulo operator (%).


n =int(input("Enter a number: "))
print("even " + str(not bool(n % 2)))

