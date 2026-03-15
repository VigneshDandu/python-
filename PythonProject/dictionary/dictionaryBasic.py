# Empty dictionary
d = {}

# With data
student = {
    "name": "Vignesh",
    "age": 21,
    "city": "Mumbai",
    "marks": [85, 90, 78]   # value can be any datatype!
}

# Using dict()
person = dict(name="Vignesh", age=21)
print(person)
print(student)


#Accessing values

print(student["name"])
#print(student["Gender"])
print(student.get("Gender")) # returns none as default value if not present or
print(student.get("Gender","no such key"))

#addind or say updating a key

student["Gender"] = "Male"

print(student)

#update method
student["age"] = 22
print(student)

student.update({"age": 23, "city": "Pune"})
print(student)

print(student.keys())   # returns a view object of keys
print(student.values()) # returns a view object of values
print(student.items())  # returns a view object of (key, value) pairs

#deleting a key

del student["marks"]
print(student)

student.pop("city")
print(student)      


