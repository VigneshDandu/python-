heroes=['spider man','superman','batman','hulk','spider man','witch','witch','hulk']
#to create a copy of a list
#b = heroes[:]
b = heroes.copy()
print(b)

#to access an element

print(heroes.index("spider man"))

#to extend the list

c = ['iron man','black panther']
heroes.extend(c)
print(heroes)

#to reverse the list

heroes.reverse()
print(heroes)

#to sort the list
heroes.sort()
print(heroes)

d= [1,1,3,4,53,34]
d.sort()
print(d)

#to clear all the data from the list
heroes.clear()
print(heroes)
