a = " hello dear vignesh "
print(len(a))
print(a.count("l"))
print(a.capitalize())
print(a.lower())
print(a.title())
print(a.capitalize())
print(a.find("vignesh"))
print(a.index("o"))



name = "vignesh"
age = 20
b = "my name is ", name, " and my age is ", age
print(b)
"""
output:
('my name is ', 'vignesh', ' and my age is ', 20)
"""
c = "my name is {} and my age is {} "
print(c.format(name,age))
"""
outputs:
my name is vignesh and my age is 20 
"""

#centre method in string
print(name.center(28,"*"))
