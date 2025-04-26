heroes=['spider man','superman','batman','hulk','spider man','witch','witch','hulk']
#to find the length of a list
print( len(heroes))
#to find the length of a particular element in a list  thus providing an index along with it
print(len(heroes[2]))

#to count an occurrence of a particular element
print(heroes.count('spider man'))

#to add to the list
heroes.append('ragnarok')
print("but this append method adds element to the last index of the list,to overcome or to add element to specific location we use insert method")

#to add element to a specific location
heroes.insert(3,'iron man',)
print(heroes)

#to remove an element
heroes.remove('spider man')
print(heroes)

#to remove an element from certain location
heroes.pop(3)
print(heroes)