#write a program to get fibonacci series upto 10 numbers
a = 0
b = 1
print(a)
print(b)
for i in range (20):
    c = a + b
    print(c)
    a = b
    b = c
