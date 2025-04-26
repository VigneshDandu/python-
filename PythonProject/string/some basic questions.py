a = "Why fit in, when you are born to stand out!"
#program to find the length of the string given
b = len(a)
print("length of the given string is ", b)

# write a program to check how many times alphabet o has occured
c = a.count("o")
print("o has occured ", c, "times")

#write a program to convert the following string into lower and uppercase
d = a.lower()
e = a.upper()
print("lower case is ", d)
print("upper case is ", e)

print(d.count("o"))
print(e.count("O"))

#convert string to title
print(a.title())

#find index number of "fit in"
print(a.find("fit in"))