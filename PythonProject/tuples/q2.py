#Q2. Write a function circle_info(radius) that returns both the area and circumference of a circle as a tuple. Print both values using unpacking.
#(area = π × r², circumference = 2 × π × r, use 3.14159 for π)

radius = int(input("enter radius : "))

def circle_info(radius):
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference

area_value, circumference_value = circle_info(radius)
print(area_value, circumference_value)