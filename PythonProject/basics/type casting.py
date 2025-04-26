""" Converting 1 datatype into another datatype is known as type casting """


name = "Vignesh"
age = 21
number = 12.9
d =12.453
print(type(name))
print(type(age))
print(type(number))
print(type(d))

b = "123"
print(type(b))
#this will show string  as inside " we have data

#     n = b + age   # since both are different data types
#      print(n)

# to change data type

b =int(b)
print(b)
print(type(b))

d = int(d)
print(d)
print(type(d))

change = "design567.9"
print(change)
print(type(change))

change = float(change[6:])  #extracting numerical part from string
print(change)
print(type(change))

# new examples
f = 'apple'
print(type(f))
f = float(f)
print(f)
print(type(f))

