a= "hello"
b= "HELLO 123"
c = "123"
d = "hey123"
e = "hey123.45"
f = " "
g ="1.345"


#isalnum - Returns True if all characters in the string are alphanumeric

print(a,a.isalnum())
print(b,b.isalnum())
print(c,c.isalnum())
print(d,d.isalnum())
print(e,e.isalnum())
print(f,f.isalnum())
print(g,g.isalnum())
print()
#spaces or any symbols doesn't opt to alphanumeric


#isalpha - Returns True if all characters in the string are in the alphabet

print(a,a.isalpha())
print(b,b.isalpha())
print(c,c.isalpha())
print(d,d.isalpha())
print(e,e.isalpha())
print(f,f.isalpha())
print(g,g.isalpha())
print()

#isdecimal - Returns True if all characters in the string are decimals

print(a,a.isdecimal())
print(b,b.isdecimal())
print(c,c.isdecimal())
print(d,d.isdecimal())
print(e,e.isdecimal())
print(f,f.isdecimal())
print(g,g.isdecimal())
print()

#isdigit - Returns True if all characters in the string are digits

print(a,a.isdigit())
print(b,b.isdigit())
print(c,c.isdigit())
print(d,d.isdigit())
print(e,e.isdigit())
print(f,f.isdigit())
print(g,g.isdigit())
print()

#isnumeric - Returns True if all characters in the string are numeric

print(a,a.isnumeric())
print(b,b.isnumeric())
print(c,c.isnumeric())
print(d,d.isnumeric())
print(e,e.isnumeric())
print(f,f.isnumeric())
print(g,g.isnumeric())
print()

#islower - Converts a string into lower case

print(a,a.islower())
print(b,b.islower())
print(c,c.islower())
print(d,d.islower())
print(e,e.islower())
print(f,f.islower())
print(g,g.islower())
print()

#isupper - Returns True if all characters in the string are upper case

print(a,a.isupper())
print(b,b.isupper())
print(c,c.isupper())
print(d,d.isupper())
print(e,e.isupper())
print(f,f.isupper())
print(g,g.isupper())
print()

#isspace - Returns True if all characters in the string are whitespaces

print(a,a.isspace())
print(b,b.isspace())
print(c,c.isspace())
print(d,d.isspace())
print(e,e.isspace())
print(f,f.isspace())   #true
print(g,g.isspace())
print()


#istitle - Returns True if the string follows the rules of a title

print(a,a.istitle())
print(b,b.istitle())
print(c,c.istitle())
print(d,d.istitle())
print(e,e.istitle())
print(f,f.istitle())
print(g,g.istitle())
print()
m = "Hello"
print(m,m.istitle())

#endswith() - returns true if the string ends with the specified value

movie = " the matrix : resurrection "
print(movie, movie.endswith(" "))
print(movie, movie.endswith("x",0,11))

#startswith() - returns true if the string starts with the specified value

animal = "Donkey"
print(animal,animal.startswith("D"))
print(animal,animal.startswith("k",3))

#swapcase() - swaps cases, lower case becomes upper case and vice versa

build = "Mountain View"
print(build,build.isalpha())
print(build + " - ",build.swapcase())


#strip() - returns a trimmed version of a string

k = "         ******  hello vignesh  \\\\\            "
print(k.strip("*,\ "))


#split() - splits the string at the specified separator , and returns a list

a = "hey, my name is vignesh , i am 21 , lives in mumbai"
print(a)
print(a.split(","))

#ljust() - returns a left-justified version of the string in the specified width

fruit = "apple is an fruit"
l = fruit.ljust(20, "*")
print(l,"so eat ")

#rjust() -returns a right justified version of the string

nom = " crycillius is boring of work of day"
mon = nom.rjust(100,"@")
print("Since he is fed up with work of day , he will be ",mon)

#replace() - replaces a specified phrase with another specified phrase

text = "The sky is blue and the ocean is blue."
print(text.replace("blue", "green"))  # Replace all occurrences of 'blue' with 'green'
print(text.replace("blue", "green", 1))  # Replace only the first occurrence of 'blue'

# rfind() - returns the highest index of the substring if found, otherwise -1
text = "The sky is blue and the ocean is blue."
print(text.rfind("blue"))  # Finds the last occurrence of 'blue'
print(text.rfind("green"))  # Returns -1 because 'green' is not in the text

# rindex() - returns the highest index of the substring if found, otherwise raises a ValueError
print(text.rindex("blue"))  # Finds the last occurrence of 'blue'
print(text.rindex("green"))



